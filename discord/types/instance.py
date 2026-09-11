"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from typing import Dict, List, Literal, Optional, TypedDict
from typing_extensions import NotRequired

from .snowflake import Snowflake


class InstanceEndpoints(TypedDict):
    api: str
    api_client: str
    api_public: str
    gateway: str
    media: str
    static_cdn: str
    marketing: str
    admin: str
    invite: str
    gift: str
    webapp: str


class CaptchaConfiguration(TypedDict):
    provider: Literal['none', 'hcaptcha', 'turnstile']
    hcaptcha_site_key: Optional[str]
    turnstile_site_key: Optional[str]


class InstanceFeatures(TypedDict):
    voice_enabled: bool
    stripe_enabled: bool
    self_hosted: bool
    presigned_attachment_uploads: bool
    emails_enabled: bool


class GIFProvider(TypedDict):
    provider: str
    display_name: str
    attribution_required: bool


class SSOStatus(TypedDict):
    enabled: bool
    enforced: bool
    display_name: Optional[str]
    redirect_uri: str


class RegistrationPolicy(TypedDict):
    mode: Literal['open', 'approval', 'closed']
    admin_registration_urls_enabled: bool


class CommunityPolicy(TypedDict):
    single_community: bool
    single_community_guild_id: Optional[Snowflake]
    direct_messages_disabled: bool


class ServiceAvailability(TypedDict):
    gif_enabled: bool
    youtube_enabled: bool
    bluesky_enabled: bool


LimitKey = Literal[
    'avatar_max_size',
    'emoji_max_size',
    'feature_animated_avatar',
    'feature_animated_banner',
    'feature_custom_discriminator',
    'feature_custom_notification_sounds',
    'feature_early_access',
    'feature_global_expressions',
    'feature_higher_video_quality',
    'feature_per_guild_profiles',
    'feature_voice_entrance_sounds',
    'max_attachment_file_size',
    'max_attachments_per_message',
    'max_bio_length',
    'max_bookmarks',
    'max_channels_per_category',
    'max_custom_backgrounds',
    'max_embeds_per_message',
    'max_favorite_meme_tags',
    'max_favorite_memes',
    'max_group_dm_recipients',
    'max_group_dms_per_user',
    'max_guild_channels',
    'max_guild_emojis',
    'max_guild_emojis_animated1',
    'max_guild_emojis_animated_more1',
    'max_guild_emojis_static1',
    'max_guild_emojis_static_more1',
    'max_guild_invites',
    'max_guild_members',
    'max_guild_roles',
    'max_guild_stickers',
    'max_guild_stickers_more2',
    'max_guilds',
    'max_message_length',
    'max_private_channels_per_user',
    'max_reactions_per_message',
    'max_relationships',
    'max_users_per_message_reaction',
    'max_voice_message_duration',
    'max_webhooks_per_channel',
    'max_webhooks_per_guild',
    'sticker_max_size',
]


class LimitFilters(TypedDict):
    traits: NotRequired[List[str]]
    guildFeatures: NotRequired[List[str]]


class LimitRule(TypedDict):
    id: str
    filters: NotRequired[LimitFilters]
    overrides: Dict[LimitKey, int]


class LimitConfiguration(TypedDict):
    version: Literal[2]
    traitDefinitions: List[str]
    rules: List[LimitRule]
    defaultsHash: str


class PushConfiguration(TypedDict):
    public_vapid_key: Optional[str]


class PublicBranding(TypedDict):
    product_name: str
    icon_url: Optional[str]
    symbol_url: Optional[str]
    logo_url: Optional[str]
    wordmark_url: Optional[str]
    favicon_url: Optional[str]
    theme_color: Optional[str]


class PublicSetupState(TypedDict):
    configured: bool
    admin_url: Optional[str]


class PublicLegalConfiguration(TypedDict):
    terms_url: Optional[str]
    privacy_url: Optional[str]


class PublicRegistrationFields(TypedDict):
    collect_date_of_birth: bool


class PublicApplicationConfiguration(TypedDict):
    branding: PublicBranding
    setup: PublicSetupState
    legal: PublicLegalConfiguration
    registration: PublicRegistrationFields


class InstanceDiscovery(TypedDict):
    api_code_version: int
    endpoints: InstanceEndpoints
    captcha: CaptchaConfiguration
    features: InstanceFeatures
    gif: GIFProvider
    sso: SSOStatus
    registration: RegistrationPolicy
    community: CommunityPolicy
    services: ServiceAvailability
    limits: LimitConfiguration
    push: PushConfiguration
    app_public: PublicApplicationConfiguration
