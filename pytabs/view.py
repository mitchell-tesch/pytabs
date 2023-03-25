# pyTABS - ETABS .NET API python wrapper
# View - cView
__all__ = ['View']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class View:
    """View interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create View interface
        self.view = etabs.cView(sap_model.View)
        
        # relate custom enumerations