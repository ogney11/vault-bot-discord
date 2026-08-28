export default function ProductCard({ product }: { product: any }) {
  return (
    <div className="bg-white rounded-lg shadow p-4">
      <h3 className="font-bold">{product.name}</h3>
      <p className="text-gray-600">{product.description}</p>
      <p className="mt-2 text-lg font-semibold">
        {product.price_minor / 100} {product.currency}
      </p>
    </div>
  );
}
