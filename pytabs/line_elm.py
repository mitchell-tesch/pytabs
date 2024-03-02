# PyTABS - ETABS .NET API python wrapper
# LineElm - cLineElm interface
__all__ = ['LineElm']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *


# import custom enumerations


# import typing


class LineElm:
    """LineElm interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create LineElm interface
        self.line_elm = etabs.cLineElm(sap_model.LineElm)

        # relate custom enumerations
