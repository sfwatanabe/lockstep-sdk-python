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
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#



from src.models.ErpInfoModel import ErpInfoModel
from src.models.CompanyModel import CompanyModel

# Represents the data sent during the onboarding flow
class ProvisioningModel:
    fullName: str
    timeZone: str
    defaultCurrency: str
    erp: ErpInfoModel
    company: CompanyModel

