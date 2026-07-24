import { FiBell, FiSearch, FiChevronDown } from "react-icons/fi";

function Navbar() {
  const today = new Date().toLocaleDateString("en-IN", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  });

  return (
    <header className="bg-white border-b border-slate-200 px-8 py-5 flex items-center justify-between">

      {/* Left Section */}
      <div>

        <h1 className="text-3xl font-bold text-slate-800">
          Dashboard
        </h1>

        <p className="text-slate-500 mt-1">
          Good Morning, Richa 👋
        </p>

      </div>

      {/* Right Section */}
      <div className="flex items-center gap-6">

        {/* Search */}
        <div className="hidden md:flex items-center bg-slate-100 rounded-xl px-4 py-3 w-80">

          <FiSearch className="text-slate-500" />

          <input
            type="text"
            placeholder="Search transactions..."
            className="bg-transparent outline-none ml-3 w-full text-sm"
          />

        </div>

        {/* Date */}
        <div className="hidden lg:block text-right">

          <p className="text-sm text-slate-500">
            Today
          </p>

          <p className="font-semibold text-slate-700">
            {today}
          </p>

        </div>

        {/* Notification */}
        <button className="relative p-3 rounded-xl bg-slate-100 hover:bg-slate-200 transition">

          <FiBell size={20} />

          <span className="absolute top-2 right-2 h-2.5 w-2.5 rounded-full bg-red-500"></span>

        </button>

        {/* User */}
        <button className="flex items-center gap-3 bg-slate-100 rounded-xl px-4 py-2 hover:bg-slate-200 transition">

          <div className="w-11 h-11 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold">

            R

          </div>

          <div className="text-left hidden md:block">

            <h3 className="font-semibold text-slate-800">
              Richa
            </h3>

            <p className="text-xs text-slate-500">
              Administrator
            </p>

          </div>

          <FiChevronDown className="text-slate-500 hidden md:block" />

        </button>

      </div>

    </header>
  );
}

export default Navbar;