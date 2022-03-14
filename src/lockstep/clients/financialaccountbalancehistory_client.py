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

from lockstep.lockstep_response import LockstepResponse
from lockstep.action_result_model import ActionResultModel
from lockstep.fetch_result import FetchResult
from lockstep.models.financialaccountbalancehistorymodel import FinancialAccountBalanceHistoryModel

class FinancialAccountBalanceHistoryClient:
    """
    Lockstep Platform methods related to FinancialAccountBalanceHistory
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_financial_account_balance_history(self, id: str) -> LockstepResponse[FinancialAccountBalanceHistoryModel]:
        """
        Retrieves the Financial Account Balance History specified by
        this unique identifier.

        A Financial Account Balance History records either the current
        or end of period balance for a corresponding financial account.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Financial
            Account Balance History
        """
        path = f"/api/v1/FinancialAccountBalanceHistory/{id}"
        result = self.client.send_request("GET", path, None, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())

    def update_financial_account_balance_history(self, id: str, body: object) -> LockstepResponse[FinancialAccountBalanceHistoryModel]:
        """
        Updates a Financial Account Balance History that matches the
        specified id with the requested information.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        A Financial Account Balance History records either the current
        or end of period balance for a corresponding financial account.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Financial
            Account Balance History to update
        body : object
            A list of changes to apply to this Financial Account Balance
            History
        """
        path = f"/api/v1/FinancialAccountBalanceHistory/{id}"
        result = self.client.send_request("PATCH", path, body, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())

    def delete_financial_account_balance_history(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Delete the Financial Account Balance History referred to by this
        unique identifier.

        A Financial Account Balance History records either the current
        or end of period balance for a corresponding financial account.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Financial
            Account Balance History to disable
        """
        path = f"/api/v1/FinancialAccountBalanceHistory/{id}"
        result = self.client.send_request("DELETE", path, None, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())

    def create_financial_account_balance_history(self, body: list[FinancialAccountBalanceHistoryModel]) -> LockstepResponse[list[FinancialAccountBalanceHistoryModel]]:
        """
        Creates a Financial Account Balance History from a given model.

        A Financial Account Balance History records either the current
        or end of period balance for a corresponding financial account.

        Parameters
        ----------
        body : list[FinancialAccountBalanceHistoryModel]
            The Financial Account Balance Histories to create
        """
        path = "/api/v1/FinancialAccountBalanceHistory"
        result = self.client.send_request("POST", path, body, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())

    def query_financial_account_balance_history(self, filter: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[FinancialAccountBalanceHistoryModel]]:
        """
        Queries Financial Account Balance History for this account using
        the specified filtering, sorting, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        A Financial Account Balance History records either the current
        or end of period balance for a corresponding financial account.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 200). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/FinancialAccountBalanceHistory/query"
        result = self.client.send_request("GET", path, None, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())
