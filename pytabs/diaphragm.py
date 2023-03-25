# pyTABS - ETABS .NET API python wrapper
# Diaphragm - cDiaphragm
__all__ = ['Diaphragm']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class Diaphragm:
    """Diaphragm interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create Diaphragm interface
        self.diaphragm = etabs.cDiaphragm(sap_model.Diaphragm)
        
        # relate custom enumerations