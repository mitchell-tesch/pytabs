# pyTABS - ETABS .NET API python wrapper
# PointObj - cPointObj
__all__ = ['PointObj']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PointObj:
    """PointObj interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PointObj interface
        self.point_obj = etabs.cPointObj(sap_model.PointObj)
        
        # relate relevant ETABS enumerations
        self.eDiaphragmOption = etabs.eDiaphragmOption
        """EtabsModel `DiaphragmOption` enumeration"""
        
        # relate custom enumerations