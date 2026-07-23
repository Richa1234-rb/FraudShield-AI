function Login() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <div className="bg-white rounded-2xl shadow-xl p-10 w-[400px]">
        <h1 className="text-3xl font-bold text-center text-blue-600">
          FraudShield AI
        </h1>

        <p className="text-center text-gray-500 mt-2">
          Sign in to continue
        </p>

        <input
          type="email"
          placeholder="Email"
          className="w-full mt-8 p-3 border rounded-lg"
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full mt-4 p-3 border rounded-lg"
        />

        <button className="w-full mt-6 bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition">
          Login
        </button>
      </div>
    </div>
  );
}

export default Login;