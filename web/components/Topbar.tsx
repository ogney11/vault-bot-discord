"use client";

import { useRouter } from "next/navigation";
import { clearAccessToken } from "../lib/auth";

export default function Topbar() {
  const router = useRouter();
  const handleLogout = () => {
    clearAccessToken();
    router.push("/login");
  };
  return (
    <header className="bg-white shadow p-4 flex justify-between items-center">
      <h1 className="text-lg font-semibold">Dashboard</h1>
      <button
        onClick={handleLogout}
        className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
      >
        Logout
      </button>
    </header>
  );
}
