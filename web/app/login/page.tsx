"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { loginWithDiscord } from "../../lib/auth";

export default function LoginPage() {
  const router = useRouter();

  useEffect(() => {
    // Check if we have a code in URL (from Discord redirect)
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get("code");
    if (code) {
      loginWithDiscord(code)
        .then(() => router.push("/dashboard"))
        .catch((err) => console.error(err));
    }
  }, [router]);

  const handleLogin = () => {
    const clientId = process.env.NEXT_PUBLIC_DISCORD_CLIENT_ID;
    const redirectUri = encodeURIComponent(
      process.env.NEXT_PUBLIC_DISCORD_REDIRECT_URI || window.location.origin + "/login"
    );
    window.location.href = `https://discord.com/api/oauth2/authorize?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=code&scope=identify%20email%20guilds`;
  };

  return (
    <div className="flex min-h-screen items-center justify-center">
      <button
        onClick={handleLogin}
        className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
      >
        Login with Discord
      </button>
    </div>
  );
}
