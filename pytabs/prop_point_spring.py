# pyTABS - ETABS .NET API python wrapper
# PropPointSpring - cPropPointSpring
__all__ = ['PropPointSpring']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PropPointSpring:
    """PropPointSpring interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropPointSpring interface
        self.prop_point_spring = etabs.cPropPointSpring(sap_model.PropPointSpring)
        
        # relate custom enumerations