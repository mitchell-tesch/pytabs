# PyTABS - ETABS .NET API python wrapper
# GridSys - cGridSys interface
__all__ = ['GridSys']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations


class GridSys:
    """GridSys interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create GridSys interface
        self.grid_sys = etabs.cGridSys(sap_model.GridSys)

        # relate custom enumerations
