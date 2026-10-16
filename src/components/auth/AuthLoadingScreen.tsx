import React from 'react';
import { ShieldCheck, Activity, Lock, RefreshCw } from 'lucide-react';

interface AuthLoadingScreenProps {
  message?: string;
  subMessage?: string;
}

export const AuthLoadingScreen: React.FC<AuthLoadingScreenProps> = ({
  message = 'Verifying Enterprise Healthcare Security Credentials...',
  subMessage = 'Connecting securely via Amazon Cognito OpenID Connect (PKCE)...'
}) => {
  return (
    <div className="min-h-screen bg-[#F8FAFC] flex flex-col items-center justify-center p-6 text-slate-800 font-sans selection:bg-cyan-500 selection:text-white relative overflow-hidden">
      {/* Central Medical Operations Security Card */}
      <div className="relative z-10 w-full max-w-md bg-white border border-slate-200 rounded-2xl shadow-xl p-8 flex flex-col items-center text-center">
        {/* Emblem */}
        <div className="relative mb-6">
          <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-cyan-600 via-teal-500 to-emerald-400 p-0.5 shadow-xl shadow-cyan-950/20 flex items-center justify-center">
            <div className="w-full h-full bg-slate-900 rounded-[14px] flex items-center justify-center">
              <Activity className="w-8 h-8 text-cyan-400 animate-pulse" />
            </div>
          </div>
          <div className="absolute -bottom-1 -right-1 w-6 h-6 rounded-full bg-emerald-50 border border-emerald-500/50 flex items-center justify-center">
            <Lock className="w-3 h-3 text-emerald-600" />
          </div>
        </div>

        {/* Title */}
        <h1 className="text-xl font-bold tracking-tight text-slate-900 mb-1">
          MediOps <span className="text-cyan-600 font-normal">Intelligence</span>
        </h1>
        <p className="text-xs text-slate-500 font-medium tracking-wide uppercase mb-6">
          Enterprise Medical Operations Command System
        </p>

        {/* Loading Spinner & Status */}
        <div className="flex items-center gap-3 bg-slate-50 border border-slate-200 rounded-xl px-4 py-3 w-full mb-4">
          <RefreshCw className="w-4 h-4 text-cyan-600 animate-spin flex-shrink-0" />
          <div className="text-left overflow-hidden">
            <p className="text-xs font-semibold text-slate-800 truncate">
              {message}
            </p>
            <p className="text-[11px] text-slate-500 truncate">
              {subMessage}
            </p>
          </div>
        </div>

        {/* Security badges */}
        <div className="flex items-center justify-center gap-4 text-[10px] text-slate-400 pt-2 border-t border-slate-200 w-full">
          <span className="flex items-center gap-1">
            <ShieldCheck className="w-3.5 h-3.5 text-teal-600" />
            HIPAA Compliant
          </span>
          <span>•</span>
          <span>AWS Cognito us-east-1</span>
          <span>•</span>
          <span>PKCE S256</span>
        </div>
      </div>
    </div>
  );
};
