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
from lockstep.models.bulkcurrencyconversionmodel import BulkCurrencyConversionModel
from lockstep.models.currencyratemodel import CurrencyRateModel

class CurrenciesClient:
    """
    Lockstep Platform methods related to Currencies
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_currency_rate(self, sourceCurrency: str, destinationCurrency: str, date: str, dataProvider: str) -> LockstepResponse[CurrencyRateModel]:
        """
        Retrieve a currency conversation rate from one currency to
        another as of the specified date. Optionally, you can specify
        which currency data provider to use.

        The currency rate model contains all of the information used to
        make the API call, plus the rate to use for the conversion.

        Parameters
        ----------
        sourceCurrency : str
            The ISO 4217 currency code of the origin currency. For a
            list of currency codes, call List Currencies.
        destinationCurrency : str
            The ISO 4217 currency code of the target currency. For a
            list of currency codes, call List Currencies.
        date : str
            The date for which we should cto use for this currency
            conversion.
        dataProvider : str
            Optionally, you can specify a data provider.
        """
        path = f"/api/v1/Currencies/{sourceCurrency}/{destinationCurrency}"
        result = self.client.send_request("GET", path, None, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())

    def bulk_currency_data(self, destinationCurrency: str, body: list[BulkCurrencyConversionModel]) -> LockstepResponse[list[CurrencyRateModel]]:
        """
        Receives an array of dates and currencies and a destination
        currency and returns an array of the corresponding currency
        rates to the given destination currency (Limit X).

        Parameters
        ----------
        destinationCurrency : str
            The currency to convert to.
        body : list[BulkCurrencyConversionModel]
            A list of dates and source currencies.
        """
        path = "/api/v1/Currencies/bulk"
        result = self.client.send_request("POST", path, body, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())
