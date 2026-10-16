import React from 'react';
import { X, Bell, Info } from 'lucide-react';

interface AlertsModalProps {
  isOpen: boolean;
  onClose: () => void;
  onExecuteAction?: (actionId: string, payload?: any) => void;
}

export const AlertsModal: React.FC<AlertsModalProps> = ({
  isOpen,
  onClose
}) => {
  if (!isOpen) return null;

  const alertItems = [
    {
      id: 'ALT-101',
      title: 'High Claim Denial Spike Alert (88% Risk)',
      desc: 'Medicare Part B claim #CLM-2026-9042 flagged for missing prior-authorization token.',
      severity: 'Critical',
      time: '4 mins ago',
      statusLabel: 'Rule Active · Continuous Denial Monitoring',
      color: 'border-rose-200 bg-rose-50 text-rose-900'
    },
    {
      id: 'ALT-102',
      title: 'ED Door-to-Doctor SLA Breach Warning',
      desc: 'Wait time at Metro General ED reached 38.4 mins (+18 mins over 20 min SLA target).',
      severity: 'High',
      time: '12 mins ago',
      statusLabel: 'SLA Monitor · Active Threshold Rule',
      color: 'border-amber-200 bg-amber-50 text-amber-900'
    },
    {
      id: 'ALT-103',
      title: 'Pharmacy Stock Low Level Alert',
      desc: 'Propofol Injectable emulsion down to 45 units (Predicted depletion in 2 days).',
      severity: 'Medium',
      time: '1 hour ago',
      statusLabel: 'Inventory Rule · Automated Depletion Tracking',
      color: 'border-cyan-200 bg-cyan-50 text-cyan-900'
    }
  ];

  return (
    <div className="fixed inset-0 bg-slate-950/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
      <div className="medops-modal-card bg-white border border-slate-200 rounded-2xl max-w-lg w-full p-6 space-y-4 shadow-2xl">
        <div className="flex items-center justify-between border-b border-slate-200 pb-3">
          <h3 className="text-base font-bold text-slate-900 flex items-center gap-2">
            <Bell className="w-5 h-5 text-amber-500" /> Operational Exception & SLA Notices ({alertItems.length})
          </h3>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-700 transition">
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl flex items-center gap-2 text-xs text-slate-600">
          <Info className="w-4 h-4 text-cyan-600 shrink-0" />
          <span>Automated outbound dispatch gateway is in standby mode. Notices reflect continuous analytical threshold monitoring.</span>
        </div>

        <div className="space-y-3">
          {alertItems.map((alt) => (
            <div key={alt.id} className={`p-4 border rounded-xl space-y-2 text-xs ${alt.color}`}>
              <div className="flex justify-between items-center font-bold">
                <span>{alt.title}</span>
                <span className="font-mono text-[10px] uppercase">{alt.severity}</span>
              </div>
              <p className="text-slate-700">{alt.desc}</p>
              <div className="pt-2 border-t border-slate-200/80 flex items-center justify-between">
                <span className="text-[10px] opacity-75">{alt.time}</span>
                <span className="px-2.5 py-0.5 bg-white border border-slate-200 rounded text-[10px] font-mono text-slate-600">
                  {alt.statusLabel}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
