import DashboardLayout from "../layouts/DashboardLayout";
import DashboardCard from "../components/DashboardCard";

import {
  FiUsers,
  FiCreditCard,
  FiAlertTriangle,
  FiPieChart,
} from "react-icons/fi";

function Dashboard() {
  return (
    <DashboardLayout>

      {/* Page Heading */}
      <div className="mb-8">

        <h2 className="text-2xl font-bold text-slate-800">
          Dashboard Overview
        </h2>

        <p className="text-slate-500 mt-1">
          Welcome back! Here's what's happening today.
        </p>

      </div>

      {/* Dashboard Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <DashboardCard
          title="Total Users"
          value="152"
          icon={<FiUsers />}
          color="bg-blue-600"
          change="+12% this month"
        />

        <DashboardCard
          title="Transactions"
          value="3,210"
          icon={<FiCreditCard />}
          color="bg-emerald-600"
          change="+8% today"
        />

        <DashboardCard
          title="Fraud Cases"
          value="32"
          icon={<FiAlertTriangle />}
          color="bg-red-600"
          change="-5% today"
        />

        <DashboardCard
          title="Fraud Rate"
          value="0.9%"
          icon={<FiPieChart />}
          color="bg-purple-600"
          change="Healthy"
        />

      </div>

    </DashboardLayout>
  );
}

export default Dashboard;