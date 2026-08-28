"use client";

export function getAccessToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("vault_access_token");
}

export function setAccessToken(token: string) {
  localStorage.setItem("vault_access_token", token);
}

export function clearAccessToken() {
  localStorage.removeItem("vault_access_token");
}

export async function loginWithDiscord(code: string) {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/auth/discord/callback`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code }),
    }
  );
  if (!res.ok) throw new Error("Login failed");
  const data = await res.json();
  setAccessToken(data.access_token);
  return data;
}
