# pyTABS - ETABS .NET API python wrapper
# PropAreaSpring - cPropAreaSpring
__all__ = ['PropAreaSpring']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PropAreaSpring:
    """PropAreaSpring interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropAreaSpring interface
        self.prop_area_spring = etabs.cPropAreaSpring(sap_model.PropAreaSpring)
        
        # relate custom enumerations