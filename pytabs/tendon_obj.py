# pyTABS - ETABS .NET API python wrapper
# TendonObj - cTendonObj
__all__ = ['TendonObj']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class TendonObj:
    """TendonObj interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create TendonObj interface
        self.tendon_obj = etabs.cTendonObj(sap_model.TendonObj)
        
        # relate custom enumerations