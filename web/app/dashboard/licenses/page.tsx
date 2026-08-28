"use client";

import { useEffect, useState } from "react";
import { apiFetch } from "../../../lib/api";
import { getAccessToken } from "../../../lib/auth";

export default function LicensesPage() {
  const [licenses, setLicenses] = useState<any[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = getAccessToken();
    if (!token) return;
    apiFetch("/licenses", {}, token)
      .then(setLicenses)
      .catch((e) => setError(e.message));
  }, []);

  if (error) return <div className="text-red-500">{error}</div>;
  if (licenses.length === 0) return <div>Loading...</div>;

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Licenses</h2>
      <table className="min-w-full bg-white shadow rounded">
        <thead>
          <tr>
            <th className="py-2 px-4 text-left">License Key</th>
            <th className="py-2 px-4 text-left">Product</th>
            <th className="py-2 px-4 text-left">Status</th>
            <th className="py-2 px-4 text-left">Expires</th>
          </tr>
        </thead>
        <tbody>
          {licenses.map((lic) => (
            <tr key={lic.id} className="border-t">
              <td className="py-2 px-4">{lic.license_key}</td>
              <td className="py-2 px-4">{lic.product_name}</td>
              <td className="py-2 px-4">{lic.status}</td>
              <td className="py-2 px-4">
                {lic.expires_at ? new Date(lic.expires_at).toLocaleDateString() : "Never"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
