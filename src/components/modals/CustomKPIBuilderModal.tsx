import React, { useState } from 'react';
import { X, Sliders, Info } from 'lucide-react';

interface CustomKPIBuilderModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSaveKPI?: (kpi: any) => void;
}

export const CustomKPIBuilderModal: React.FC<CustomKPIBuilderModalProps> = ({
  isOpen,
  onClose
}) => {
  const [title, setTitle] = useState('');
  const [formula, setFormula] = useState('SUM(Revenue) / COUNT(Encounters)');
  const [target, setTarget] = useState('$120 per patient');
  const [category, setCategory] = useState('Finance');

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-slate-950/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
      <div className="medops-modal-card bg-white border border-slate-200 rounded-2xl max-w-md w-full p-6 space-y-4 shadow-2xl">
        <div className="flex items-center justify-between border-b border-slate-200 pb-3">
          <h3 className="text-base font-bold text-slate-900 flex items-center gap-2">
            <Sliders className="w-5 h-5 text-cyan-600" /> Custom Operational KPI Builder
          </h3>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-700 transition">
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="p-3 bg-amber-50 border border-amber-200 rounded-xl flex items-start gap-2.5 text-xs text-amber-900">
          <Info className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
          <span>
            Custom KPI persistence is currently in development / read-only preview. User-defined semantic formulas cannot be committed to the database in this environment.
          </span>
        </div>

        <div className="space-y-3 text-xs">
          <div>
            <label className="text-slate-700 block mb-1 font-medium">KPI Title</label>
            <input
              type="text"
              disabled
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g. Net Margin per Cardiac Encounters"
              className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-600 outline-none cursor-not-allowed"
            />
          </div>

          <div>
            <label className="text-slate-700 block mb-1 font-medium">Semantic DAX / SQL Formula</label>
            <input
              type="text"
              disabled
              value={formula}
              onChange={(e) => setFormula(e.target.value)}
              className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-600 font-mono outline-none cursor-not-allowed"
            />
          </div>

          <div>
            <label className="text-slate-700 block mb-1 font-medium">Target Benchmark</label>
            <input
              type="text"
              disabled
              value={target}
              onChange={(e) => setTarget(e.target.value)}
              className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-600 outline-none cursor-not-allowed"
            />
          </div>

          <div>
            <label className="text-slate-700 block mb-1 font-medium">Pillar Category</label>
            <select
              disabled
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-600 outline-none cursor-not-allowed"
            >
              <option value="Operations">Operations</option>
              <option value="Finance">Finance</option>
              <option value="Clinical">Clinical</option>
              <option value="Compliance">Compliance</option>
            </select>
          </div>

          <div className="pt-3 flex items-center justify-end gap-2">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 rounded-xl transition font-medium"
            >
              Close
            </button>
            <button
              type="button"
              disabled
              className="px-4 py-2 bg-slate-100 text-slate-400 font-medium rounded-xl cursor-not-allowed border border-slate-200"
            >
              Persistence Disabled (Preview)
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
