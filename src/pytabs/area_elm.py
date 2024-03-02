# PyTABS - ETABS .NET API python wrapper
# AreaElm - cAreaElm interface 
__all__ = ['AreaElm']

# import ETABS namespace and pyTABS error handler
from .etabs_config import *
from .error_handle import *

# import custom enumerations


class AreaElm:
    """AreaElm interface"""
    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create AreaElm interface
        self.area_elm = etabs.cAreaElm(sap_model.AreaElm)

        # relate custom enumerations
