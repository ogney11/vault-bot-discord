"use client";

import { useEffect, useState } from "react";
import { apiFetch } from "../../../lib/api";
import { getAccessToken } from "../../../lib/auth";

export default function OrdersPage() {
  const [orders, setOrders] = useState<any[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = getAccessToken();
    if (!token) return;
    apiFetch("/orders", {}, token)
      .then(setOrders)
      .catch((e) => setError(e.message));
  }, []);

  if (error) return <div className="text-red-500">{error}</div>;
  if (orders.length === 0) return <div>Loading...</div>;

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Orders</h2>
      <table className="min-w-full bg-white shadow rounded">
        <thead>
          <tr>
            <th className="py-2 px-4 text-left">Order #</th>
            <th className="py-2 px-4 text-left">Status</th>
            <th className="py-2 px-4 text-left">Total</th>
            <th className="py-2 px-4 text-left">Date</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id} className="border-t">
              <td className="py-2 px-4">{order.order_number}</td>
              <td className="py-2 px-4">{order.status}</td>
              <td className="py-2 px-4">
                {order.total_minor / 100} {order.currency}
              </td>
              <td className="py-2 px-4">
                {new Date(order.created_at).toLocaleDateString()}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
