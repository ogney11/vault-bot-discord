import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Vault Dashboard",
  description: "Manage your digital products and licenses",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
