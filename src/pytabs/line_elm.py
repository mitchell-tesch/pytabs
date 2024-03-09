# PyTABS - ETABS .NET API python wrapper
# LineElm - cLineElm interface
__all__ = ['LineElm']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations


class LineElm:
    """LineElm interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create LineElm interface
        self.line_elm = etabs.cLineElm(sap_model.LineElm)

        # relate custom enumerations
