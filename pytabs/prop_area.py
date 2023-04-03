# pyTABS - ETABS .NET API python wrapper
# PropArea - cPropArea
__all__ = ['PropArea']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PropArea:
    """PropArea interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropArea interface
        self.prop_area = etabs.cPropArea(sap_model.PropArea)
        
        # relate relevant ETABS enumerations
        self.eDeckType = etabs.eDeckType
        """EtabsModel `DeckType` enumeration"""
        self.eShellType = etabs.eShellType
        """EtabsModel `ShellType` enumeration"""
        self.eSlabType = etabs.eSlabType
        """EtabsModel `SlabType` enumeration"""
        self.eWallPropType = etabs.eWallPropType
        """EtabsModel `WallPropType` enumeration"""
        
        # relate custom enumerations