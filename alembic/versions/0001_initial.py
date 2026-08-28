"""initial schema

Revision ID: 0001
Revises:
Create Date: 2026-08-28

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import app.db.uuid  # noqa: F401  registers the custom UUID column type

# revision identifiers, used by Alembic.
revision: str = "0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.create_table('plans',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('description', sa.String(length=500), nullable=True),
        sa.Column('price_monthly_minor', sa.BigInteger(), nullable=True),
        sa.Column('price_yearly_minor', sa.BigInteger(), nullable=True),
        sa.Column('currency', sa.String(length=3), nullable=False),
        sa.Column('features', sa.JSON(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
        )
        op.create_table('users',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )
        op.create_table('webhook_events',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('stripe_event_id', sa.String(length=255), nullable=False),
        sa.Column('event_type', sa.String(length=100), nullable=False),
        sa.Column('payload', sa.JSON(), nullable=False),
        sa.Column('processed_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('error', sa.String(length=500), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('stripe_event_id')
        )
        op.create_table('discord_accounts',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('user_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('discord_id', sa.BigInteger(), nullable=False),
        sa.Column('username', sa.String(length=100), nullable=False),
        sa.Column('discriminator', sa.String(length=10), nullable=True),
        sa.Column('avatar', sa.String(length=255), nullable=True),
        sa.Column('access_token_enc', sa.String(length=500), nullable=False),
        sa.Column('refresh_token_enc', sa.String(length=500), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('discord_id'),
        sa.UniqueConstraint('user_id')
        )
        op.create_table('sessions',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('user_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('token_hash', sa.String(length=64), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('revoked_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('ip_address', sa.String(length=45), nullable=True),
        sa.Column('user_agent', sa.String(length=500), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('token_hash')
        )
        op.create_table('workspaces',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('owner_user_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('slug', sa.String(length=100), nullable=False),
        sa.Column('discord_guild_id', sa.BigInteger(), nullable=True),
        sa.Column('is_claimed', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['owner_user_id'], ['users.id'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('discord_guild_id'),
        sa.UniqueConstraint('slug')
        )
        op.create_table('api_keys',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('key_hash', sa.String(length=64), nullable=False),
        sa.Column('prefix', sa.String(length=20), nullable=False),
        sa.Column('scopes', sa.JSON(), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('revoked_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('last_used_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_api_keys_key_hash', 'api_keys', ['key_hash'], unique=True)
        op.create_index('ix_api_keys_prefix', 'api_keys', ['prefix'], unique=False)
        op.create_index('ix_api_keys_workspace_id', 'api_keys', ['workspace_id'], unique=False)
        op.create_table('customers',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('user_id', app.db.uuid.UUID(length=36), nullable=True),
        sa.Column('discord_id', sa.BigInteger(), nullable=True),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('stripe_customer_id', sa.String(length=255), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_customers_workspace_discord', 'customers', ['workspace_id', 'discord_id'], unique=False)
        op.create_index('ix_customers_workspace_email', 'customers', ['workspace_id', 'email'], unique=False)
        op.create_table('discord_role_mappings',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('guild_id', sa.BigInteger(), nullable=False),
        sa.Column('role_id', sa.String(length=100), nullable=False),
        sa.Column('resource_type', sa.String(length=50), nullable=False),
        sa.Column('resource_id', app.db.uuid.UUID(length=36), nullable=True),
        sa.Column('action', sa.String(length=20), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('metadata', sa.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_discord_role_mappings_guild_role', 'discord_role_mappings', ['guild_id', 'role_id'], unique=False)
        op.create_index('ix_discord_role_mappings_workspace_id', 'discord_role_mappings', ['workspace_id'], unique=False)
        op.create_table('products',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('slug', sa.String(length=100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('price_minor', sa.BigInteger(), nullable=False),
        sa.Column('currency', sa.String(length=3), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('image_url', sa.String(length=500), nullable=True),
        sa.Column('discord_role_id', sa.String(length=100), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.CheckConstraint('price_minor >= 0', name='ck_product_price_non_negative'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_products_workspace_slug', 'products', ['workspace_id', 'slug'], unique=True)
        op.create_table('stripe_accounts',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('stripe_account_id', sa.String(length=255), nullable=False),
        sa.Column('charges_enabled', sa.Boolean(), nullable=False),
        sa.Column('payouts_enabled', sa.Boolean(), nullable=False),
        sa.Column('details_submitted', sa.Boolean(), nullable=False),
        sa.Column('country', sa.String(length=2), nullable=True),
        sa.Column('default_currency', sa.String(length=3), nullable=True),
        sa.Column('created_at_stripe', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('stripe_account_id'),
        sa.UniqueConstraint('workspace_id')
        )
        op.create_table('vault_subscriptions',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('plan_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('stripe_subscription_id', sa.String(length=255), nullable=False),
        sa.Column('status', sa.String(length=30), nullable=False),
        sa.Column('current_period_start', sa.DateTime(timezone=True), nullable=True),
        sa.Column('current_period_end', sa.DateTime(timezone=True), nullable=True),
        sa.Column('cancel_at_period_end', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['plan_id'], ['plans.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('stripe_subscription_id')
        )
        op.create_index('ix_vault_subscriptions_stripe_subscription_id', 'vault_subscriptions', ['stripe_subscription_id'], unique=False)
        op.create_index('ix_vault_subscriptions_workspace_id', 'vault_subscriptions', ['workspace_id'], unique=False)
        op.create_table('workspace_members',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('user_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('role', sa.String(length=20), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('workspace_id', 'user_id', name='uq_workspace_member')
        )
        op.create_table('audit_logs',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('actor_user_id', app.db.uuid.UUID(length=36), nullable=True),
        sa.Column('actor_api_key_id', app.db.uuid.UUID(length=36), nullable=True),
        sa.Column('action', sa.String(length=100), nullable=False),
        sa.Column('resource_type', sa.String(length=100), nullable=False),
        sa.Column('resource_id', app.db.uuid.UUID(length=36), nullable=True),
        sa.Column('metadata', sa.JSON(), nullable=False),
        sa.Column('ip_address', sa.String(length=45), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['actor_api_key_id'], ['api_keys.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['actor_user_id'], ['users.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_audit_logs_actor_api_key_id', 'audit_logs', ['actor_api_key_id'], unique=False)
        op.create_index('ix_audit_logs_actor_user_id', 'audit_logs', ['actor_user_id'], unique=False)
        op.create_index('ix_audit_logs_resource_type_id', 'audit_logs', ['resource_type', 'resource_id'], unique=False)
        op.create_index('ix_audit_logs_workspace_id', 'audit_logs', ['workspace_id'], unique=False)
        op.create_table('licenses',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('customer_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('product_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('license_hash', sa.String(length=64), nullable=False),
        sa.Column('license_prefix', sa.String(length=20), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('max_activations', sa.Integer(), nullable=False),
        sa.Column('activation_count', sa.Integer(), nullable=False),
        sa.Column('revoked_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('revoked_reason', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.CheckConstraint('max_activations >= 0', name='ck_license_max_activations_non_negative'),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('license_hash')
        )
        op.create_index('ix_licenses_customer_id', 'licenses', ['customer_id'], unique=False)
        op.create_index('ix_licenses_license_hash', 'licenses', ['license_hash'], unique=False)
        op.create_index('ix_licenses_product_id', 'licenses', ['product_id'], unique=False)
        op.create_index('ix_licenses_workspace_id', 'licenses', ['workspace_id'], unique=False)
        op.create_table('orders',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('customer_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('order_number', sa.String(length=50), nullable=False),
        sa.Column('idempotency_key', sa.String(length=255), nullable=False),
        sa.Column('status', sa.String(length=30), nullable=False),
        sa.Column('payment_status', sa.String(length=30), nullable=False),
        sa.Column('total_minor', sa.BigInteger(), nullable=False),
        sa.Column('currency', sa.String(length=3), nullable=False),
        sa.Column('stripe_payment_intent_id', sa.String(length=255), nullable=True),
        sa.Column('refunded_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.CheckConstraint('total_minor >= 0', name='ck_order_total_non_negative'),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('idempotency_key'),
        sa.UniqueConstraint('order_number')
        )
        op.create_index('ix_orders_customer_id', 'orders', ['customer_id'], unique=False)
        op.create_index('ix_orders_stripe_payment_intent_id', 'orders', ['stripe_payment_intent_id'], unique=False)
        op.create_index('ix_orders_workspace_id', 'orders', ['workspace_id'], unique=False)
        op.create_table('product_assets',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('product_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('asset_type', sa.String(length=50), nullable=False),
        sa.Column('file_name', sa.String(length=255), nullable=False),
        sa.Column('storage_key', sa.String(length=500), nullable=False),
        sa.Column('mime_type', sa.String(length=100), nullable=True),
        sa.Column('size_bytes', sa.BigInteger(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_product_assets_product_id', 'product_assets', ['product_id'], unique=False)
        op.create_table('product_versions',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('product_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('version', sa.String(length=50), nullable=False),
        sa.Column('changelog', sa.Text(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_product_versions_product_id', 'product_versions', ['product_id'], unique=False)
        op.create_table('license_activations',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('license_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('device_id', sa.String(length=255), nullable=False),
        sa.Column('ip_address', sa.String(length=45), nullable=True),
        sa.Column('user_agent', sa.String(length=500), nullable=True),
        sa.Column('activated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('deactivated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['license_id'], ['licenses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_license_activations_device_id', 'license_activations', ['license_id', 'device_id'], unique=True)
        op.create_index('ix_license_activations_license_id', 'license_activations', ['license_id'], unique=False)
        op.create_table('order_items',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('order_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('product_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('product_name', sa.String(length=255), nullable=False),
        sa.Column('price_minor', sa.BigInteger(), nullable=False),
        sa.Column('currency', sa.String(length=3), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.CheckConstraint('price_minor >= 0', name='ck_order_item_price_non_negative'),
        sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_order_items_order_id', 'order_items', ['order_id'], unique=False)
        op.create_index('ix_order_items_product_id', 'order_items', ['product_id'], unique=False)
        op.create_table('payments',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('order_id', app.db.uuid.UUID(length=36), nullable=True),
        sa.Column('vault_subscription_id', app.db.uuid.UUID(length=36), nullable=True),
        sa.Column('stripe_payment_intent_id', sa.String(length=255), nullable=False),
        sa.Column('amount_minor', sa.BigInteger(), nullable=False),
        sa.Column('currency', sa.String(length=3), nullable=False),
        sa.Column('status', sa.String(length=30), nullable=False),
        sa.Column('refunded_amount_minor', sa.BigInteger(), nullable=False),
        sa.Column('fee_minor', sa.BigInteger(), nullable=False),
        sa.Column('metadata', sa.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['vault_subscription_id'], ['vault_subscriptions.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('stripe_payment_intent_id')
        )
        op.create_index('ix_payments_order_id', 'payments', ['order_id'], unique=False)
        op.create_index('ix_payments_stripe_payment_intent_id', 'payments', ['stripe_payment_intent_id'], unique=False)
        op.create_index('ix_payments_vault_subscription_id', 'payments', ['vault_subscription_id'], unique=False)
        op.create_table('product_files',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('version_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('file_name', sa.String(length=255), nullable=False),
        sa.Column('storage_key', sa.String(length=500), nullable=False),
        sa.Column('mime_type', sa.String(length=100), nullable=True),
        sa.Column('size_bytes', sa.BigInteger(), nullable=False),
        sa.Column('checksum_sha256', sa.String(length=64), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.CheckConstraint('size_bytes >= 0', name='ck_product_file_size_non_negative'),
        sa.ForeignKeyConstraint(['version_id'], ['product_versions.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_product_files_version_id', 'product_files', ['version_id'], unique=False)
        op.create_table('downloads',
        sa.Column('id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('workspace_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('customer_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('version_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('file_id', app.db.uuid.UUID(length=36), nullable=False),
        sa.Column('token', sa.String(length=255), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('used_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('ip_address', sa.String(length=45), nullable=True),
        sa.Column('user_agent', sa.String(length=500), nullable=True),
        sa.Column('is_used', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['file_id'], ['product_files.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['version_id'], ['product_versions.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_downloads_customer_id', 'downloads', ['customer_id'], unique=False)
        op.create_index('ix_downloads_file_id', 'downloads', ['file_id'], unique=False)
        op.create_index('ix_downloads_token', 'downloads', ['token'], unique=True)
        op.create_index('ix_downloads_version_id', 'downloads', ['version_id'], unique=False)
        # ### end Alembic commands ###


def downgrade() -> None:
    pass
