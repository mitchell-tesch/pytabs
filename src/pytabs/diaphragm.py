# PyTABS - ETABS .NET API python wrapper
# Diaphragm - cDiaphragm interface
__all__ = ['Diaphragm']

# import ETABS namespace and pyTABS error handler
from .etabs_config import *
from .error_handle import *

# import custom enumerations


class Diaphragm:
    """Diaphragm interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create Diaphragm interface
        self.diaphragm = etabs.cDiaphragm(sap_model.Diaphragm)

        # relate custom enumerations
