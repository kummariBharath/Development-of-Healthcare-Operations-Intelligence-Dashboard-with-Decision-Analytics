import React, { useState } from 'react';
import type { TimeframeOption, RoleType } from './types';
import { Header } from './components/layout/Header';
import { Sidebar, type ModuleId } from './components/layout/Sidebar';
import { AICopilotDrawer } from './components/copilot/AICopilotDrawer';

// Modules
import { ExecutiveCommandCenter } from './components/modules/ExecutiveCommandCenter';
import { PatientOperations } from './components/modules/PatientOperations';
import { DoctorStaffIntelligence } from './components/modules/DoctorStaffIntelligence';
import { BillingRevenueIntelligence } from './components/modules/BillingRevenueIntelligence';
import { InsuranceClaimsAutomation } from './components/modules/InsuranceClaimsAutomation';
import { MedicalCodingDocumentation } from './components/modules/MedicalCodingDocumentation';
import { AIPredictiveIntelligence } from './components/modules/AIPredictiveIntelligence';
import { WorkflowAutomationEngine } from './components/modules/WorkflowAutomationEngine';
import { PharmacyInventory } from './components/modules/PharmacyInventory';
import { LaboratoryDiagnostics } from './components/modules/LaboratoryDiagnostics';
import { EmergencyCriticalOperations } from './components/modules/EmergencyCriticalOperations';
import { QualityCompliance } from './components/modules/QualityCompliance';
import { PatientExperience } from './components/modules/PatientExperience';
import { SupplyChainVendor } from './components/modules/SupplyChainVendor';
import { FinancialIntelligence } from './components/modules/FinancialIntelligence';
import { MedicalOpsAIAgentTab } from './components/modules/MedicalOpsAIAgentTab';
import { PowerBIDashboardHub } from './components/modules/PowerBIDashboardHub';
import { SecurityGovernance } from './components/modules/SecurityGovernance';
import { IntegrationsHub } from './components/modules/IntegrationsHub';
import { AutomationPipelineVisualizer } from './components/modules/AutomationPipelineVisualizer';
import { AWSCloudServicesHub } from './components/modules/AWSCloudServicesHub';

// Modals
import { EnterpriseDrilldownModal } from './components/modals/EnterpriseDrilldownModal';
import { CustomKPIBuilderModal } from './components/modals/CustomKPIBuilderModal';
import { AlertsModal } from './components/modals/AlertsModal';

export const App: React.FC = () => {
  const [activeModule, setActiveModule] = useState<ModuleId>('executive');
  const [selectedFacility, setSelectedFacility] = useState<string>('all');
  const [selectedTimeframe, setSelectedTimeframe] = useState<TimeframeOption>('realtime');
  const [selectedRole, setSelectedRole] = useState<RoleType>('Enterprise Executive');
  const [sidebarCollapsed, setSidebarCollapsed] = useState<boolean>(false);

  // Drawers & Modals
  const [isCopilotOpen, setIsCopilotOpen] = useState<boolean>(false);
  const [powerBiMode, setPowerBiMode] = useState<boolean>(false);
  const [isDrilldownOpen, setIsDrilldownOpen] = useState<boolean>(false);
  const [drilldownFacilityId, setDrilldownFacilityId] = useState<string>('all');
  const [isKPIBuilderOpen, setIsKPIBuilderOpen] = useState<boolean>(false);
  const [isAlertsOpen, setIsAlertsOpen] = useState<boolean>(false);

  // Notification Toast Banner
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const triggerToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => {
      setToastMessage(null);
    }, 4000);
  };

  const handleExecuteAction = (actionId: string, payload?: any) => {
    let actionDesc = `Executed action: ${actionId}`;
    if (actionId === 'trigger-auth-followup') actionDesc = '⚡ Triggered Automated Claim Authorization Follow-Up via EDI 278';
    else if (actionId === 'reassign-shift-kim') actionDesc = '📅 Re-assigned Cardiology Shift to Dr. David Kim';
    else if (actionId === 'dispatch-evs') actionDesc = '🧹 Dispatched Environmental Services (EVS) Bed Cleanup to Floor 3';
    else if (actionId === 'reroute-lab') actionDesc = '🧪 Rerouted STAT Blood Culture Samples to Northwest Diagnostic Center';
    else if (actionId === 'hold-denial-claims') actionDesc = '🛡️ Placed 14 High Denial Risk Claims on Pre-Submission Audit Hold';
    else if (actionId === 'download-ops-pdf') actionDesc = '📄 Generating Enterprise PDF Operations Digest...';
    else if (actionId === 'patient-registered') actionDesc = `✅ Onboarded Patient ${payload?.name || ''} to ${payload?.dept || ''} Queue`;
    else if (actionId === 'workflow-rule-created') actionDesc = `🤖 Created Automated Workflow Rule "${payload?.name || ''}"`;
    else if (actionId === 'generate-po') actionDesc = `🛒 Generated Automated Purchase Order for ${payload?.vendor || 'Vendor'}`;
    else if (actionId === 'export-analytics-pdf' || actionId === 'export-powerbi-pdf') actionDesc = `📄 Exported ${payload?.report || 'Executive Analytics'} Report to PDF`;
    else if (actionId === 'export-analytics-excel' || actionId === 'export-powerbi-excel') actionDesc = `📊 Exported ${payload?.report || 'Executive Analytics'} Data to Excel`;
    else if (actionId === 'refresh-analytics-dataset' || actionId === 'refresh-powerbi-dataset') actionDesc = '🔄 Refreshed Enterprise Semantic Data Analytics Model';
    else if (actionId === 'pipeline-simulation-completed') actionDesc = '🎉 Closed-Loop Data → AI → Decision → Automation Pipeline Executed Successfully!';
    else if (actionId === 'run-athena-query') actionDesc = '⚡ Executed SQL Query on AWS Athena via AWS Glue Data Catalog!';
    else if (actionId === 'trigger-glue-crawler-rescan') actionDesc = '🕷️ AWS Glue Crawler triggered: Re-scanning s3://medical-operations-core-v9-100k';

    triggerToast(actionDesc);
  };

  const handleOpenDrilldown = (facId: string) => {
    setDrilldownFacilityId(facId);
    setIsDrilldownOpen(true);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-cyan-500 selection:text-slate-950">
      {/* Action Toast Notification */}
      {toastMessage && (
        <div className="fixed top-16 right-6 z-50 bg-cyan-950 border border-cyan-500 text-cyan-200 px-4 py-3 rounded-2xl shadow-2xl text-xs font-semibold flex items-center gap-2 animate-bounce">
          <span className="w-2 h-2 rounded-full bg-cyan-400 animate-ping" />
          {toastMessage}
        </div>
      )}

      {/* Global Application Header */}
      <Header
        selectedFacility={selectedFacility}
        onFacilityChange={setSelectedFacility}
        selectedTimeframe={selectedTimeframe}
        onTimeframeChange={setSelectedTimeframe}
        selectedRole={selectedRole}
        onRoleChange={setSelectedRole}
        onToggleCopilot={() => setIsCopilotOpen(!isCopilotOpen)}
        isCopilotOpen={isCopilotOpen}
        powerBiMode={powerBiMode}
        onTogglePowerBi={() => {
          setPowerBiMode(!powerBiMode);
          if (!powerBiMode) setActiveModule('powerbi-hub');
        }}
        onOpenKPIBuilder={() => setIsKPIBuilderOpen(true)}
        onOpenAlertsModal={() => setIsAlertsOpen(true)}
        unreadAlertCount={3}
      />

      {/* Main Layout Area */}
      <div className="flex flex-1 relative">
        {/* Navigation Sidebar */}
        <Sidebar
          activeModule={activeModule}
          onSelectModule={(id) => setActiveModule(id)}
          collapsed={sidebarCollapsed}
          onToggleCollapse={() => setSidebarCollapsed(!sidebarCollapsed)}
        />

        {/* Dynamic Module Content View */}
        <main className="flex-1 p-4 lg:p-6 overflow-y-auto max-w-full">
          {activeModule === 'executive' && (
            <ExecutiveCommandCenter
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onOpenDrilldown={handleOpenDrilldown}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'patient-ops' && (
            <PatientOperations selectedFacility={selectedFacility} selectedTimeframe={selectedTimeframe} onExecuteAction={handleExecuteAction} />
          )}

          {activeModule === 'staff-intel' && (
            <DoctorStaffIntelligence selectedFacility={selectedFacility} selectedTimeframe={selectedTimeframe} onExecuteAction={handleExecuteAction} />
          )}

          {activeModule === 'billing-rev' && (
            <BillingRevenueIntelligence selectedFacility={selectedFacility} selectedTimeframe={selectedTimeframe} onExecuteAction={handleExecuteAction} />
          )}

          {activeModule === 'claims-auto' && (
            <InsuranceClaimsAutomation selectedFacility={selectedFacility} selectedTimeframe={selectedTimeframe} onExecuteAction={handleExecuteAction} />
          )}

          {activeModule === 'coding-doc' && (
            <MedicalCodingDocumentation
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'ai-predictive' && (
            <AIPredictiveIntelligence
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'workflow-auto' && (
            <WorkflowAutomationEngine
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'pharmacy-inv' && (
            <PharmacyInventory selectedFacility={selectedFacility} selectedTimeframe={selectedTimeframe} onExecuteAction={handleExecuteAction} />
          )}

          {activeModule === 'lab-diag' && (
            <LaboratoryDiagnostics selectedFacility={selectedFacility} selectedTimeframe={selectedTimeframe} onExecuteAction={handleExecuteAction} />
          )}

          {activeModule === 'emergency-ops' && (
            <EmergencyCriticalOperations
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'quality-compliance' && (
            <QualityCompliance
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'patient-exp' && (
            <PatientExperience
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'supply-chain' && (
            <SupplyChainVendor
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'financial-intel' && (
            <FinancialIntelligence
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'ai-copilot-tab' && (
            <MedicalOpsAIAgentTab 
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction} 
            />
          )}

          {activeModule === 'powerbi-hub' && (
            <PowerBIDashboardHub
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}

          {activeModule === 'security-gov' && (
            <SecurityGovernance onExecuteAction={handleExecuteAction} />
          )}

          {activeModule === 'integrations-hub' && (
            <IntegrationsHub onExecuteAction={handleExecuteAction} />
          )}

          {activeModule === 'automation-pipeline' && (
            <AutomationPipelineVisualizer
              selectedFacility={selectedFacility}
              selectedTimeframe={selectedTimeframe}
              onExecuteAction={handleExecuteAction}
            />
          )}
        </main>
      </div>

      {/* Slide-over AI Agent Copilot Drawer */}
      <AICopilotDrawer
        isOpen={isCopilotOpen}
        onClose={() => setIsCopilotOpen(false)}
        selectedFacility={selectedFacility}
        onExecuteAction={handleExecuteAction}
      />

      {/* Drill-down Matrix Modal */}
      <EnterpriseDrilldownModal
        isOpen={isDrilldownOpen}
        onClose={() => setIsDrilldownOpen(false)}
        initialFacilityId={drilldownFacilityId}
      />

      {/* KPI Builder Modal */}
      <CustomKPIBuilderModal
        isOpen={isKPIBuilderOpen}
        onClose={() => setIsKPIBuilderOpen(false)}
        onSaveKPI={(kpi) => triggerToast(`Added Custom KPI "${kpi.title}" to Command Center`)}
      />

      {/* Live Alerts Notification Drawer Modal */}
      <AlertsModal
        isOpen={isAlertsOpen}
        onClose={() => setIsAlertsOpen(false)}
        onExecuteAction={handleExecuteAction}
      />
    </div>
  );
};

export default App;
