import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-4">Vault</h1>
      <p className="text-lg mb-8">Digital product platform for Discord communities</p>
      <Link
        href="/login"
        className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
      >
        Login with Discord
      </Link>
    </main>
  );
}
