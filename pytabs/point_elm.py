# PyTABS - ETABS .NET API python wrapper
# PointElm - cPointElm interface
__all__ = ['PointElm']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *


# import custom enumerations


# import typing


class PointElm:
    """PointElm interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PointElm interface
        self.point_elm = etabs.cPointElm(sap_model.PointElm)

        # relate custom enumerations
