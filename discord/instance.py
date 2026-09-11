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

from contextvars import ContextVar
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types import instance


class InstanceEndpoints:
    def __init__(self, data: instance.InstanceEndpoints):
        self.api_client = data['api_client']
        self.api_public = data['api_public']
        self.gateway = data['gateway']
        self.media = data['media']
        self.static_cdn = data['static_cdn']
        self.marketing = data['marketing']
        self.admin = data['admin']
        self.invite = data['invite']
        self.gift = data['gift']
        self.webapp = data['webapp']


class InstanceFeatures:
    def __init__(self, data: instance.InstanceFeatures):
        self.voice_enabled = data['voice_enabled']
        self.stripe_enabled = data['stripe_enabled']
        self.self_hosted = data['self_hosted']
        self.presigned_attachment_uploads = data['presigned_attachment_uploads']
        self.emails_enabled = data['emails_enabled']


class InstanceDiscovery:
    def __init__(self, origin_url: str, data: instance.InstanceDiscovery):
        self.origin_url = origin_url
        self.api_code_version = data['api_code_version']
        self.endpoints = InstanceEndpoints(data['endpoints'])
        self.features = InstanceFeatures(data['features'])


instance_context: ContextVar[InstanceDiscovery] = ContextVar('instance_context')
get_instance = instance_context.get
set_instance = instance_context.set
