# pyTABS - ETABS .NET API python wrapper
# GridSys - cGridSys
__all__ = ['GridSys']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class GridSys:
    """GridSys interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create GridSys interface
        self.grid_sys = etabs.cGridSys(sap_model.GridSys)
        
        # relate custom enumerations