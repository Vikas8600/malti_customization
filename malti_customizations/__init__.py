__version__ = "0.0.1"

from erpnext.controllers.selling_controller import SellingController
from malti_customizations.overrides.selling_settings import validate_selling_price
SellingController.validate_selling_price = validate_selling_price