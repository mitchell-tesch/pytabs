# pyTABS - ETABS .NET API python wrapper
# PropLineSpring - cPropLineSpring
__all__ = ['PropLineSpring']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PropLineSpring:
    """PropLineSpring interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropLineSpring interface
        self.prop_line_spring = etabs.cPropLineSpring(sap_model.PropLineSpring)
        
        # relate custom enumerations