# pyTABS - ETABS .NET API python wrapper
# PropLink - cPropLink
__all__ = ['PropLink']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PropLink:
    """PropLink interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropLink interface
        self.prop_link = etabs.cPropLink(sap_model.PropLink)
        
        # relate relevant ETABS enumerations
        self.eLinkPropType = etabs.eLinkPropType
        """EtabsModel `LinkPropType` enumeration"""
        
        # relate custom enumerations