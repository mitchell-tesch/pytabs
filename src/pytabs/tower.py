# PyTABS - ETABS .NET API python wrapper
# Tower - cTower interface
__all__ = ['Tower']

# import ETABS namespace and pyTABS error handler
from .etabs_config import *
from .error_handle import *

# import custom enumerations

# import typing


class Tower:
    """Tower interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create Tower interface
        self.tower = etabs.cTower(sap_model.Tower)

        # relate custom enumerations
