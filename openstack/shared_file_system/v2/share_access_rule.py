# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack import resource


class ShareAccessRule(resource.Resource):
    resource_key = "share_access_rule"
    resources_key = "share_access_rules"
    base_path = "/share-access-rules"

    # capabilities
    allow_create = False
    allow_fetch = True
    allow_commit = False
    allow_delete = False
    allow_list = True
    allow_head = False

    _query_mapping = resource.QueryParameters("share_id")

    _max_microversion = '2.45'

    #: Properties
    #: The access credential of the entity granted share access.
    access_key = resource.Body("access_key", type=str)
    #: The access level to the share.
    access_level = resource.Body("access_level", type=str)
    #: The object of the access rule.
    access_list = resource.Body("access_list", type=str)
    #: The value that defines the access.
    access_to = resource.Body("access_to", type=str)
    #: The access rule type.
    access_type = resource.Body("access_type", type=str)
    #: The date and time stamp when the resource was created within the
    #: service’s database.
    created_at = resource.Body("created_at")
    #: One or more access rule metadata key and value pairs as a dictionary
    #: of strings.
    metadata = resource.Body("metadata", type=dict)
    #: The UUID of the share to which you are granted or denied access.
    share_id = resource.Body("share_id", type=str)
    #: The state of the access rule.
    state = resource.Body("state", type=str)
    #: The date and time stamp when the resource was last updated within
    #: the service’s database.
    updated_at = resource.Body("updated_at", type=str)
