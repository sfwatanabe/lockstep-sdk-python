#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class DpoSummaryGroupTotalModel:
    """
    Represents the group totals for the values found in the daily
    payable outstanding summary
    """

    groupKey: str | None = None
    vendors: int | None = None
    bills: int | None = None
    amountOutstanding: float | None = None
    dpo: float | None = None
