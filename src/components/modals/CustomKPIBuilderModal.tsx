import React, { useState } from 'react';
import { X, Sliders, Plus, Sparkles, CheckCircle2 } from 'lucide-react';

interface CustomKPIBuilderModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSaveKPI: (kpi: any) => void;
}

export const CustomKPIBuilderModal: React.FC<CustomKPIBuilderModalProps> = ({
  isOpen,
  onClose,
  onSaveKPI
}) => {
  const [title, setTitle] = useState('');
  const [formula, setFormula] = useState('SUM(Revenue) / COUNT(Encounters)');
  const [target, setTarget] = useState('$120 per patient');
  const [category, setCategory] = useState('Finance');

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;

    onSaveKPI({
      title,
      value: 'Custom Live',
      change: 4.2,
      status: 'positive',
      target,
      category
    });

    setTitle('');
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl max-w-md w-full p-6 space-y-4 shadow-2xl">
        <div className="flex items-center justify-between border-b border-slate-800 pb-3">
          <h3 className="text-base font-bold text-white flex items-center gap-2">
            <Sliders className="w-5 h-5 text-cyan-400" /> Custom Operational KPI Builder
          </h3>
          <button onClick={onClose} className="text-slate-400 hover:text-white">
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="space-y-3 text-xs">
          <div>
            <label className="text-slate-400 block mb-1">KPI Title</label>
            <input
              type="text"
              required
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g. Net Margin per Cardiac Encounters"
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-slate-200 outline-none focus:border-cyan-500"
            />
          </div>

          <div>
            <label className="text-slate-400 block mb-1">Semantic DAX / SQL Formula</label>
            <input
              type="text"
              value={formula}
              onChange={(e) => setFormula(e.target.value)}
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-slate-200 font-mono outline-none focus:border-cyan-500"
            />
          </div>

          <div>
            <label className="text-slate-400 block mb-1">Target Benchmark</label>
            <input
              type="text"
              value={target}
              onChange={(e) => setTarget(e.target.value)}
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-slate-200 outline-none focus:border-cyan-500"
            />
          </div>

          <div>
            <label className="text-slate-400 block mb-1">Pillar Category</label>
            <select
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-slate-200 outline-none focus:border-cyan-500"
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
              className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl transition"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-4 py-2 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold rounded-xl transition"
            >
              Add KPI to Command Scorecard
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
