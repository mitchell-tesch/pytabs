# pyTABS - ETABS .NET API python wrapper
# SpandrelLabel - cSpandrelLabel
__all__ = ['SpandrelLabel']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class SpandrelLabel:
    """SpandrelLabel interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create SpandrelLabel interface
        self.spandrel_label = etabs.cSpandrelLabel(sap_model.SpandrelLabel)
        
        # relate custom enumerations