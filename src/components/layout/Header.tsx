import React from 'react';
import { 
  Building2, 
  Clock, 
  UserCheck, 
  Bot, 
  LayoutDashboard, 
  Bell, 
  Sliders, 
  Download,
  Activity,
  ShieldCheck
} from 'lucide-react';
import type { TimeframeOption, RoleType } from '../../types';
import { facilitiesData } from '../../data/mockData';
import { fetchFacilities, type Facility } from '../../services/apiService';
import { UserAccountMenu } from '../auth/UserAccountMenu';

interface HeaderProps {
  selectedFacility: string;
  onFacilityChange: (id: string) => void;
  selectedTimeframe: TimeframeOption;
  onTimeframeChange: (tf: TimeframeOption) => void;
  selectedRole: RoleType;
  onRoleChange: (role: RoleType) => void;
  onToggleCopilot: () => void;
  isCopilotOpen: boolean;
  powerBiMode: boolean;
  onTogglePowerBi: () => void;
  onOpenKPIBuilder: () => void;
  onOpenAlertsModal: () => void;
  unreadAlertCount: number;
}

export const Header: React.FC<HeaderProps> = ({
  selectedFacility,
  onFacilityChange,
  selectedTimeframe,
  onTimeframeChange,
  selectedRole,
  onRoleChange,
  onToggleCopilot,
  isCopilotOpen,
  powerBiMode,
  onTogglePowerBi,
  onOpenKPIBuilder,
  onOpenAlertsModal,
  unreadAlertCount
}) => {
  const [facilities, setFacilities] = React.useState<Facility[]>(facilitiesData);

  React.useEffect(() => {
    fetchFacilities()
      .then((data) => {
        if (data && data.length > 0) {
          setFacilities(data);
        }
      })
      .catch((err) => console.warn('Using default facilities list:', err));
  }, []);

  return (
    <header className="sticky top-0 z-30 bg-slate-900/95 backdrop-blur border-b border-slate-800 px-4 lg:px-6 py-3 flex flex-wrap items-center justify-between gap-4">
      {/* Brand & System Title */}
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-600 via-teal-500 to-emerald-400 p-0.5 shadow-lg shadow-cyan-950/50 flex items-center justify-center">
          <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
            <Activity className="w-5 h-5 text-cyan-400 animate-pulse" />
          </div>
        </div>
        <div>
          <div className="flex items-center gap-2">
            <h1 className="text-lg font-bold text-white tracking-tight">
              MediOps <span className="text-cyan-400 font-normal">Intelligence</span>
            </h1>
            <span className="px-2 py-0.5 text-[10px] font-semibold tracking-wide uppercase bg-cyan-950 text-cyan-400 border border-cyan-800/60 rounded-full">
              Enterprise v4.2
            </span>
          </div>
          <p className="text-xs text-slate-400 hidden sm:block">
            Medical Operations Intelligence & Automation Command System
          </p>
        </div>
      </div>

      {/* Global Slicers & Context Filters */}
      <div className="flex flex-wrap items-center gap-2.5">
        {/* Facility Selector */}
        <div className="flex items-center gap-1.5 bg-slate-950/80 border border-slate-800 rounded-lg px-2.5 py-1.5 text-xs text-slate-300">
          <Building2 className="w-3.5 h-3.5 text-cyan-400" />
          <select
            value={selectedFacility}
            onChange={(e) => onFacilityChange(e.target.value)}
            className="bg-transparent text-slate-200 border-none outline-none font-medium cursor-pointer"
          >
            <option value="all" className="bg-slate-900">All Facilities (Enterprise Group)</option>
            {facilities.map((fac) => (
              <option key={fac.id} value={fac.id} className="bg-slate-900">
                {fac.name}
              </option>
            ))}
          </select>
        </div>

        {/* Timeframe Selector */}
        <div className="flex items-center gap-1.5 bg-slate-950/80 border border-slate-800 rounded-lg px-2.5 py-1.5 text-xs text-slate-300">
          <Clock className="w-3.5 h-3.5 text-teal-400" />
          <select
            value={selectedTimeframe}
            onChange={(e) => onTimeframeChange(e.target.value as TimeframeOption)}
            className="bg-transparent text-slate-200 border-none outline-none font-medium cursor-pointer"
          >
            <option value="realtime" className="bg-slate-900">🔴 Real-Time Live Stream</option>
            <option value="today" className="bg-slate-900">Today (24 Hrs)</option>
            <option value="weekly" className="bg-slate-900">This Week</option>
            <option value="monthly" className="bg-slate-900">This Month (Sep 2026)</option>
            <option value="quarterly" className="bg-slate-900">Q3 2026</option>
            <option value="ytd" className="bg-slate-900">Year to Date (YTD)</option>
          </select>
        </div>

        {/* Role Switcher (RBAC) */}
        <div className="flex items-center gap-1.5 bg-slate-950/80 border border-slate-800 rounded-lg px-2.5 py-1.5 text-xs text-slate-300">
          <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
          <span className="text-slate-500 text-[11px]">Role:</span>
          <select
            value={selectedRole}
            onChange={(e) => onRoleChange(e.target.value as RoleType)}
            className="bg-transparent text-emerald-400 font-semibold border-none outline-none cursor-pointer"
          >
            <option value="Enterprise Executive" className="bg-slate-900">Enterprise Executive</option>
            <option value="Chief Medical Officer" className="bg-slate-900">Chief Medical Officer (CMO)</option>
            <option value="Chief Financial Officer" className="bg-slate-900">Chief Financial Officer (CFO)</option>
            <option value="Billing & Claims Lead" className="bg-slate-900">Billing & Claims Lead</option>
            <option value="Operations Director" className="bg-slate-900">Operations Director</option>
            <option value="Compliance Officer" className="bg-slate-900">Compliance Officer</option>
          </select>
        </div>
      </div>

      {/* Header Actions & Mode Toggles */}
      <div className="flex items-center gap-2">
        {/* Analytics Workspace Mode Toggle */}
        <button
          onClick={onTogglePowerBi}
          className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition border ${
            powerBiMode
              ? 'bg-amber-500/20 text-amber-300 border-amber-500/50 shadow-md shadow-amber-950/30'
              : 'bg-slate-800/80 text-slate-300 border-slate-700 hover:bg-slate-800'
          }`}
          title="Toggle Embedded Executive Analytics Mode"
        >
          <LayoutDashboard className="w-3.5 h-3.5 text-amber-400" />
          <span className="hidden sm:inline">Analytics Mode</span>
        </button>

        {/* Custom KPI Builder Modal trigger */}
        <button
          onClick={onOpenKPIBuilder}
          className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-800 text-slate-300 border border-slate-700 text-xs font-medium transition"
          title="Open Custom KPI Builder"
        >
          <Sliders className="w-3.5 h-3.5 text-cyan-400" />
          <span className="hidden md:inline">KPI Builder</span>
        </button>

        {/* Live Alerts Notification Feed */}
        <button
          onClick={onOpenAlertsModal}
          className="relative p-2 rounded-lg bg-slate-800/80 hover:bg-slate-800 text-slate-300 border border-slate-700 transition"
          title="Operational Exception Alerts"
        >
          <Bell className="w-4 h-4 text-amber-400" />
          {unreadAlertCount > 0 && (
            <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-rose-600 text-white text-[10px] font-bold flex items-center justify-center animate-bounce">
              {unreadAlertCount}
            </span>
          )}
        </button>

        {/* Dedicated AI Agent Copilot Drawer Trigger */}
        <button
          onClick={onToggleCopilot}
          className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-semibold transition border shadow-lg ${
            isCopilotOpen
              ? 'bg-cyan-500 text-slate-950 border-cyan-400 shadow-cyan-500/30'
              : 'bg-gradient-to-r from-cyan-600 to-teal-600 hover:from-cyan-500 hover:to-teal-500 text-white border-cyan-400/30'
          }`}
        >
          <Bot className="w-4 h-4 animate-spin-slow" />
          <span>AI Copilot</span>
        </button>

        {/* Divider & Enterprise User Account Profile */}
        <div className="h-6 w-px bg-slate-800 mx-1 hidden sm:block" />
        <UserAccountMenu />
      </div>
    </header>
  );
};
