"use client";

import { useEffect, useState } from "react";
import { apiFetch } from "../../../lib/api";
import { getAccessToken } from "../../../lib/auth";

export default function DownloadsPage() {
  const [downloads, setDownloads] = useState<any[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = getAccessToken();
    if (!token) return;
    apiFetch("/downloads", {}, token)
      .then(setDownloads)
      .catch((e) => setError(e.message));
  }, []);

  if (error) return <div className="text-red-500">{error}</div>;
  if (downloads.length === 0) return <div>Loading...</div>;

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Downloads</h2>
      <table className="min-w-full bg-white shadow rounded">
        <thead>
          <tr>
            <th className="py-2 px-4 text-left">File</th>
            <th className="py-2 px-4 text-left">Downloaded At</th>
            <th className="py-2 px-4 text-left">IP</th>
          </tr>
        </thead>
        <tbody>
          {downloads.map((d) => (
            <tr key={d.id} className="border-t">
              <td className="py-2 px-4">{d.file_name}</td>
              <td className="py-2 px-4">
                {new Date(d.created_at).toLocaleString()}
              </td>
              <td className="py-2 px-4">{d.ip_address}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
