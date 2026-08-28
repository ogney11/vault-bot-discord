"use client";

import { useEffect, useState } from "react";
import { apiFetch } from "../../lib/api";
import { getAccessToken } from "../../lib/auth";

export default function OverviewPage() {
  const [stats, setStats] = useState<any>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = getAccessToken();
    if (!token) return;
    apiFetch("/dashboard/overview", {}, token)
      .then(setStats)
      .catch((e) => setError(e.message));
  }, []);

  if (error) return <div className="text-red-500">{error}</div>;
  if (!stats) return <div>Loading...</div>;

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Overview</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-white p-4 rounded shadow">
          <h3 className="text-sm text-gray-500">Total Revenue</h3>
          <p className="text-2xl font-bold">${stats.revenue / 100}</p>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h3 className="text-sm text-gray-500">Orders</h3>
          <p className="text-2xl font-bold">{stats.orders}</p>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h3 className="text-sm text-gray-500">Active Licenses</h3>
          <p className="text-2xl font-bold">{stats.active_licenses}</p>
        </div>
      </div>
    </div>
  );
}
