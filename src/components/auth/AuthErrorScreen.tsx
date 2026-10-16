import React from 'react';
import { AlertTriangle, RotateCcw, LogIn, ShieldAlert } from 'lucide-react';

interface AuthErrorScreenProps {
  error: string;
  onRetry: () => void;
}

export const AuthErrorScreen: React.FC<AuthErrorScreenProps> = ({ error, onRetry }) => {
  return (
    <div className="min-h-screen bg-[#F8FAFC] flex flex-col items-center justify-center p-6 text-slate-800 font-sans selection:bg-rose-500 selection:text-white relative overflow-hidden">
      <div className="relative z-10 w-full max-w-lg bg-white border border-rose-200 rounded-2xl shadow-xl p-8 flex flex-col items-center text-center">
        {/* Error Emblem */}
        <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-rose-600 via-rose-500 to-amber-500 p-0.5 shadow-xl shadow-rose-950/20 flex items-center justify-center mb-6">
          <div className="w-full h-full bg-slate-900 rounded-[14px] flex items-center justify-center">
            <ShieldAlert className="w-8 h-8 text-rose-400" />
          </div>
        </div>

        {/* Title */}
        <h1 className="text-xl font-bold tracking-tight text-slate-900 mb-1">
          Authentication Exception
        </h1>
        <p className="text-xs text-rose-700 font-medium tracking-wide uppercase mb-6">
          Amazon Cognito Security Gateway
        </p>

        {/* Detailed Error Box */}
        <div className="w-full bg-rose-50 border border-rose-200 rounded-xl p-4 text-left mb-6">
          <div className="flex items-start gap-2.5">
            <AlertTriangle className="w-4 h-4 text-rose-600 flex-shrink-0 mt-0.5" />
            <div className="text-xs space-y-1">
              <span className="font-semibold text-rose-900">Security Notice:</span>
              <p className="text-rose-800 break-words leading-relaxed font-mono text-[11px]">
                {error}
              </p>
            </div>
          </div>
        </div>

        {/* Instructions */}
        <p className="text-xs text-slate-600 mb-6 max-w-sm">
          Please verify your Cognito credentials or retry logging in via the AWS Cognito Managed Login portal.
        </p>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row items-center gap-3 w-full">
          <button
            onClick={onRetry}
            className="w-full sm:flex-1 flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-gradient-to-r from-cyan-600 to-teal-600 hover:from-cyan-500 hover:to-teal-500 text-white font-semibold text-xs transition shadow-lg shadow-cyan-950/20 cursor-pointer"
          >
            <RotateCcw className="w-4 h-4" />
            <span>Retry Login</span>
          </button>
          
          <button
            onClick={() => {
              sessionStorage.clear();
              window.location.href = window.location.pathname;
            }}
            className="w-full sm:flex-1 flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold text-xs border border-slate-200 transition cursor-pointer"
          >
            <LogIn className="w-4 h-4" />
            <span>Reset Session</span>
          </button>
        </div>
      </div>
    </div>
  );
};
