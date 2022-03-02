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


from dataclasses import dataclass

@dataclass
class FinancialAccountBalanceHistoryModel:
    """
    Represents a balance for a financial account for a given period of
    time.
    """

    financialAccountBalanceHistoryId: str = None
    groupKey: str = None
    financialAccountId: str = None
    appEnrollmentId: str = None
    financialYear: int = None
    periodNumber: int = None
    periodStartDate: str = None
    periodEndDate: str = None
    status: str = None
    balance: float = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
