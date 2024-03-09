# PyTABS - ETABS .NET API python wrapper
# Analyse - cAnalyze interface 
__all__ = ['Analyse']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations

# import typing


class Analyse:
    """Analyse interface"""
    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create Analyse interface
        self.analyse = etabs.cAnalyze(sap_model.Analyze)
        
        # relate custom enumerations
