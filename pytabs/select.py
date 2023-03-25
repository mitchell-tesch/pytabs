# pyTABS - ETABS .NET API python wrapper
# Select - cSelect
__all__ = ['Select']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class Select:
    """Select interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create SelectObj interface
        self.select = etabs.cSelect(sap_model.SelectObj)
        
        # relate custom enumerations