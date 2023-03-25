# pyTABS - ETABS .NET API python wrapper
# LinkObj - cLinkObj
__all__ = ['LinkObj']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class LinkObj:
    """LinkObj interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create LinkObj interface
        self.link_obj = etabs.cLinkObj(sap_model.LinkObj)
        
        # relate custom enumerations