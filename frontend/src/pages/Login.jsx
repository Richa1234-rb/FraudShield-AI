import { FiShield, FiLock, FiTrendingUp } from "react-icons/fi";

function Login() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 via-slate-100 to-indigo-100 flex">

      {/* Left Section */}
      <div className="hidden lg:flex w-1/2 items-center justify-center p-16">
        <div>
          <div className="flex items-center gap-3 mb-8">
            <FiShield className="text-blue-600 text-6xl" />
            <h1 className="text-5xl font-extrabold text-blue-700">
              FraudShield AI
            </h1>
          </div>

          <p className="text-gray-700 text-xl leading-9 max-w-xl">
            AI-powered fraud detection platform that helps banks and
            businesses identify suspicious transactions in real time.
          </p>

          <div className="mt-12 space-y-6">

            <div className="flex items-center gap-4">
              <FiTrendingUp className="text-green-500 text-3xl" />
              <span className="text-lg">
                Real-time Fraud Analytics
              </span>
            </div>

            <div className="flex items-center gap-4">
              <FiLock className="text-blue-600 text-3xl" />
              <span className="text-lg">
                Secure JWT Authentication
              </span>
            </div>

            <div className="flex items-center gap-4">
              <FiShield className="text-red-500 text-3xl" />
              <span className="text-lg">
                AI-based Risk Prediction
              </span>
            </div>

          </div>
        </div>
      </div>

      {/* Right Section */}
      <div className="w-full lg:w-1/2 flex items-center justify-center p-8">

        <div className="bg-white shadow-2xl rounded-3xl w-full max-w-md p-10">

          <h2 className="text-3xl font-bold text-center text-slate-800">
            Welcome Back 👋
          </h2>

          <p className="text-center text-gray-500 mt-2">
            Sign in to continue
          </p>

          <input
            type="email"
            placeholder="Email Address"
            className="w-full mt-8 p-4 rounded-xl border focus:ring-2 focus:ring-blue-500 outline-none"
          />

          <input
            type="password"
            placeholder="Password"
            className="w-full mt-5 p-4 rounded-xl border focus:ring-2 focus:ring-blue-500 outline-none"
          />

          <div className="flex justify-between mt-5 text-sm">

            <label className="flex items-center gap-2">
              <input type="checkbox" />
              Remember Me
            </label>

            <button className="text-blue-600 hover:underline">
              Forgot Password?
            </button>

          </div>

          <button className="w-full bg-blue-600 hover:bg-blue-700 text-white rounded-xl py-4 mt-8 font-semibold transition">
            Sign In
          </button>

        </div>

      </div>

    </div>
  );
}

export default Login;