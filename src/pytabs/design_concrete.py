# PyTABS - ETABS .NET API python wrapper
# DesignConcrete - cDesignConcrete interface
__all__ = ['DesignConcrete']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations

# import typing
from typing import TypedDict


class DesignConcrete:
    """DesignConcrete interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create DesignConcrete interface
        self.design_concrete= etabs.cDesignConcrete(sap_model.DesignConcrete)

        # relate custom enumerations

    # Design Concrete Methods

