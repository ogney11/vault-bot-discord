"use client";

import { useEffect, useState } from "react";
import { apiFetch } from "../../../lib/api";
import { getAccessToken } from "../../../lib/auth";
import ProductCard from "../../../components/ProductCard";

export default function ProductsPage() {
  const [products, setProducts] = useState<any[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = getAccessToken();
    if (!token) return;
    apiFetch("/products", {}, token)
      .then(setProducts)
      .catch((e) => setError(e.message));
  }, []);

  if (error) return <div className="text-red-500">{error}</div>;
  if (products.length === 0) return <div>Loading...</div>;

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Products</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {products.map((p) => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  );
}
