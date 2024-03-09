# PyTABS - ETABS .NET API python wrapper
# LinkObj - cLinkObj interface
__all__ = ['LinkObj']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations


class LinkObj:
    """LinkObj interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create LinkObj interface
        self.link_obj = etabs.cLinkObj(sap_model.LinkObj)

        # relate custom enumerations
