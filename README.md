# Vault

Digital product platform for Discord communities — license keys, downloads, subscriptions, and payments, managed from a web dashboard and a Discord bot.

## Structure

```
app/       FastAPI backend (API v1)
bot/       Discord bot (discord.py)
web/       Next.js dashboard
alembic/   Database migrations
tests/     Backend tests
docker/    Container images
```

## Quick start

1. Copy `.env.example` to `.env` and fill in your values.
2. `docker compose up` to run the API, bot, worker, Postgres, and Redis.
3. For the dashboard: `cd web`, `cp .env.local.example .env.local`, then `npm install && npm run dev`.

## Components

- **API** (`app/`) — FastAPI service exposing workspaces, products, customers, orders, licenses, downloads, subscriptions, payments, API keys, audit logs, and Discord endpoints.
- **Bot** (`bot/`) — discord.py bot with `/shop`, `/licenses`, `/admin_sync`, and `/admin_set_role` slash commands that call the Vault API.
- **Web** (`web/`) — Next.js dashboard with Discord OAuth login and pages for overview, products, orders, licenses, and downloads.
