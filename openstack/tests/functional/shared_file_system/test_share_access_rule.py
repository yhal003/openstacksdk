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

from openstack.tests.functional.shared_file_system import base


class ShareAccessRuleTest(base.BaseSharedFileSystemTest):

    def setUp(self):
        super(ShareAccessRuleTest, self).setUp()

        self.SHARE_NAME = self.getUniqueString()
        mys = self.create_share(
            name=self.SHARE_NAME, size=2, share_type="dhss_false",
            share_protocol='NFS', description=None)
        self.operator_cloud.shared_file_system.wait_for_status(
            mys,
            status='available',
            failures=['error'],
            interval=5,
            wait=self._wait_for_timeout)
        self.assertIsNotNone(mys)
        self.assertIsNotNone(mys.id)
        self.SHARE_ID = mys.id

    def test_access_rules(self):
        # TODO(kafilat): An Access Rule needs to be created
        # for the new share;
        pass
