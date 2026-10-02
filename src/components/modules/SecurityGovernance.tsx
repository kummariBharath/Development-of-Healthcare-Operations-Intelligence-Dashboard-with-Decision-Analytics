import React, { useState, useEffect } from 'react';
import { 
  Lock, 
  ShieldCheck, 
  Eye, 
  EyeOff, 
  FileText, 
  Database, 
  CheckCircle2, 
  Layers,
  Key,
  Loader2,
  AlertTriangle,
  Info
} from 'lucide-react';
import { fetchSecurityGovernanceIntelligence, type SecurityGovernanceResponse } from '../../services/apiService';

interface SecurityGovernanceProps {
  onExecuteAction: (actionId: string, payload?: any) => void;
}

export const SecurityGovernance: React.FC<SecurityGovernanceProps> = ({ onExecuteAction }) => {
  const [dataMaskingEnabled, setDataMaskingEnabled] = useState(true);
  const [data, setData] = useState<SecurityGovernanceResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let isMounted = true;
    setLoading(true);
    setError(null);

    fetchSecurityGovernanceIntelligence()
      .then((res) => {
        if (!isMounted) return;
        setData(res);
        setLoading(false);
      })
      .catch((err) => {
        if (!isMounted) return;
        console.error('Failed to fetch security governance posture:', err);
        setError(err.message || 'Failed to fetch security governance data');
        setLoading(false);
      });

    return () => {
      isMounted = false;
    };
  }, []);

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center p-12 bg-slate-900 border border-slate-800 rounded-2xl min-h-[400px]">
        <Loader2 className="w-8 h-8 text-cyan-400 animate-spin mb-3" />
        <p className="text-sm font-medium text-slate-300">Loading security posture & audit logs from backend...</p>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="flex flex-col items-center justify-center p-8 bg-rose-950/40 border border-rose-800/60 rounded-2xl text-rose-300 text-center min-h-[300px]">
        <AlertTriangle className="w-10 h-10 text-rose-400 mb-2" />
        <h3 className="text-base font-bold text-white mb-1">Security Governance API Error</h3>
        <p className="text-xs text-rose-200 max-w-md">{error || 'Unknown error'}</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-4 bg-slate-900 border border-slate-800 rounded-2xl p-5">
        <div>
          <div className="flex items-center gap-3">
            <h2 className="text-lg font-bold text-white flex items-center gap-2">
              <Lock className="w-5 h-5 text-emerald-400" /> Security, RBAC & Governance Center
            </h2>
            <span className="px-2.5 py-0.5 text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-800 font-mono font-bold rounded-full">
              Infrastructure Validated
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Zero-credential exposure posture, synthetic data boundary, TLS 1.3 / AES-256 encryption, and backend access audit logs
          </p>
        </div>

        {/* Data Masking Toggle */}
        <button
          onClick={() => {
            setDataMaskingEnabled(!dataMaskingEnabled);
            onExecuteAction('toggle-phi-masking', { enabled: !dataMaskingEnabled });
          }}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition ${
            dataMaskingEnabled
              ? 'bg-emerald-950 text-emerald-300 border border-emerald-800'
              : 'bg-rose-950 text-rose-300 border border-rose-800'
          }`}
        >
          {dataMaskingEnabled ? <EyeOff className="w-4 h-4 text-emerald-400" /> : <Eye className="w-4 h-4 text-rose-400" />}
          {dataMaskingEnabled ? 'Audit Resource Masking: ACTIVE' : 'Audit Resource Masking: OFF'}
        </button>
      </div>

      {/* Honest Compliance Notice Banner */}
      <div className="bg-slate-950 border border-slate-800 p-4 rounded-xl flex items-start gap-3">
        <Info className="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" />
        <div className="text-xs text-slate-400 leading-relaxed">
          <strong className="text-slate-200 block mb-0.5">Privacy Boundary & Credential Governance:</strong>
          All records in this system belong to a verified synthetic healthcare dataset (no human PHI). AWS IAM credentials and session tokens are strictly confined to backend environment variables and are never transmitted to the browser client.
        </div>
      </div>

      {/* Security Status Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 space-y-1">
          <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Encryption In Transit & Rest</span>
          <div className="text-xl font-bold text-emerald-400 font-mono">{data.posture.encryptionInTransit}</div>
          <p className="text-[10px] text-emerald-400 font-semibold">{data.posture.encryptionAtRest}</p>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 space-y-1">
          <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">RBAC Access Matrix</span>
          <div className="text-xl font-bold text-white font-mono">{data.posture.activeRbacRolesCount} Defined Roles</div>
          <p className="text-[10px] text-slate-400">Department-Level Granularity</p>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 space-y-1">
          <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Network Boundary Policy</span>
          <div className="text-xl font-bold text-cyan-400 font-mono">CORS Origin Restricted</div>
          <p className="text-[10px] text-slate-400">{data.posture.networkControls}</p>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 space-y-1">
          <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">AWS Cloud Session State</span>
          <div className="text-xl font-bold text-amber-400 font-mono">Auth Expired / Local Active</div>
          <p className="text-[10px] text-amber-300">Fail-safe local CSV active</p>
        </div>
      </div>

      {/* Defined RBAC Roles Grid */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-3">
        <h3 className="text-sm font-bold text-white">Defined Role-Based Access Control (RBAC) Archetypes</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {data.posture.rbacRoles.map((role, idx) => (
            <div key={idx} className="p-3 bg-slate-950 rounded-xl border border-slate-800/80 text-xs flex items-center gap-2">
              <Key className="w-4 h-4 text-cyan-400 shrink-0" />
              <span className="text-slate-300 font-medium">{role}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Data Lineage & Real Operational Audit Logs Stream */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <h3 className="text-sm font-bold text-white flex items-center gap-2">
          <Database className="w-4 h-4 text-cyan-400" /> Operational Security & Access Audit Stream
        </h3>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-slate-950 text-slate-400 uppercase text-[10px] tracking-wider border-b border-slate-800">
              <tr>
                <th className="py-3 px-3">Log ID</th>
                <th className="py-3 px-3">Timestamp</th>
                <th className="py-3 px-3">User Principal</th>
                <th className="py-3 px-3">Role</th>
                <th className="py-3 px-3">Action</th>
                <th className="py-3 px-3">Target Resource</th>
                <th className="py-3 px-3">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 font-mono">
              {data.auditLogs.map((log) => (
                <tr key={log.id} className="hover:bg-slate-800/40 transition">
                  <td className="py-3 px-3 font-bold text-white">{log.id}</td>
                  <td className="py-3 px-3 text-slate-400">{log.timestamp}</td>
                  <td className="py-3 px-3 text-cyan-400">{log.user}</td>
                  <td className="py-3 px-3 text-slate-300 font-sans">{log.role}</td>
                  <td className="py-3 px-3 text-white font-sans">{log.action}</td>
                  <td className="py-3 px-3 text-slate-400 font-sans">
                    {dataMaskingEnabled && log.resource.includes('.csv')
                      ? log.resource.replace(/\w+\.csv/, '******.csv')
                      : log.resource}
                  </td>
                  <td className="py-3 px-3 font-sans">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-950 text-emerald-400 border border-emerald-800">
                      {log.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
