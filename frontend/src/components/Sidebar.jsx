import {
  FiGrid,
  FiCreditCard,
  FiBarChart2,
  FiSettings,
  FiLogOut,
  FiShield,
} from "react-icons/fi";

function Sidebar() {
  return (
    <aside className="w-72 h-screen bg-white border-r border-slate-200 shadow-lg flex flex-col sticky top-0">

      {/* Logo */}
      <div className="px-8 py-8 border-b border-slate-200">

        <div className="flex items-center gap-3">

          <div className="w-12 h-12 rounded-xl bg-blue-600 flex items-center justify-center">

            <FiShield className="text-white text-2xl" />

          </div>

          <div>

            <h1 className="text-2xl font-bold text-slate-800">
              FraudShield
            </h1>

            <p className="text-sm text-slate-500">
              AI Dashboard
            </p>

          </div>

        </div>

      </div>

      {/* Navigation */}

      <nav className="flex-1 px-5 py-8 space-y-3">

        <button className="w-full flex items-center gap-4 rounded-xl bg-blue-600 text-white px-5 py-4 font-semibold shadow hover:bg-blue-700 transition">

          <FiGrid size={20} />

          Dashboard

        </button>

        <button className="w-full flex items-center gap-4 rounded-xl px-5 py-4 text-slate-600 hover:bg-slate-100 transition">

          <FiCreditCard size={20} />

          Transactions

        </button>

        <button className="w-full flex items-center gap-4 rounded-xl px-5 py-4 text-slate-600 hover:bg-slate-100 transition">

          <FiBarChart2 size={20} />

          Analytics

        </button>

        <button className="w-full flex items-center gap-4 rounded-xl px-5 py-4 text-slate-600 hover:bg-slate-100 transition">

          <FiSettings size={20} />

          Settings

        </button>

      </nav>

      {/* Footer */}

      <div className="border-t border-slate-200 p-6">

        <div className="mb-5 rounded-xl bg-slate-100 p-4">

          <p className="text-xs uppercase tracking-wide text-slate-500">
            Version
          </p>

          <h3 className="font-semibold text-slate-700">
            FraudShield AI v1.0
          </h3>

        </div>

        <button className="w-full flex items-center justify-center gap-3 rounded-xl border border-red-200 py-3 text-red-600 hover:bg-red-50 transition">

          <FiLogOut />

          Logout

        </button>

      </div>

    </aside>
  );
}

export default Sidebar;