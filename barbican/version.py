# Copyright 2010-2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Cloudkeep's Barbican version.

The code repository should only control major and minor version information in
this file. Per-build information will be supplied at build time via the
'build_id' and 'commit_id' parameters.
"""

__version__ = '2013.2.{build_id}'
__version_info__ = tuple(__version__.split('.'))
__version_commit__ = '{commit_id}'
