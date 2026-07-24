import { FiTrendingUp } from "react-icons/fi";

function DashboardCard({
  title,
  value,
  icon,
  color,
  change,
}) {
  return (
    <div className="group bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300">

      <div className="flex justify-between items-start">

        <div>

          <p className="text-slate-500 text-sm font-medium">
            {title}
          </p>

          <h2 className="text-4xl font-bold text-slate-800 mt-3">
            {value}
          </h2>

          <div className="flex items-center gap-2 mt-4 text-green-600 text-sm font-medium">

            <FiTrendingUp />

            {change}

          </div>

        </div>

        <div
          className={`${color} w-16 h-16 rounded-2xl flex items-center justify-center text-white text-3xl shadow-lg group-hover:scale-110 transition`}
        >
          {icon}
        </div>

      </div>

    </div>
  );
}

export default DashboardCard;