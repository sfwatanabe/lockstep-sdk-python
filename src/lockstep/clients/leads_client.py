#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from src.lockstep.lockstep_api import LockstepApi
from src.lockstep.lockstep_response import LockstepResponse
from src.lockstep.models.leadmodel import LeadModel

class LeadsClient:
    """
    Lockstep Platform methods related to Leads
    """

    def __init__(self, client: LockstepApi):
        self.client = client

    def create_leads(self, body: list[LeadModel]) -> LockstepResponse[list[LeadModel]]:
        """
        Creates one or more Leads within the Lockstep platform and
        returns the records as created.

        A Lead is a person who is interested in the Lockstep platform
        but needs certain new features in order to use it. If you are
        interested in the Lockstep platform, you can create a lead with
        your information and our team will prioritize the feature you
        need.

        Parameters
        ----------
        body : list[LeadModel]
            The Leads to create
        """
        path = "/api/v1/Leads"
        result = self.client.send_request("POST", path, body, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())
