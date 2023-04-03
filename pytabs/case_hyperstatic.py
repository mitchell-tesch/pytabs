# pyTABS - ETABS .NET API python wrapper
# CaseHyperStatic - cCaseHyperStatic
__all__ = ['CaseHyperStatic']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class CaseHyperStatic:
    """CaseHyperStatic interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for hyperstatic cases
        self.hyerstatic = etabs.cCaseHyperStatic(sap_model.LoadCases.HyperStatic)
        
        # relate custom enumerations