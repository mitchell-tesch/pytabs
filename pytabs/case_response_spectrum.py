# pyTABS - ETABS .NET API python wrapper
# CaseResponseSpectrum - cCaseResponseSpectrum
__all__ = ['CaseResponseSpectrum']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class CaseResponseSpectrum:
    """CaseResponseSpectrum interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for response spectrum cases
        self.response_spectrum = etabs.cCaseResponseSpectrum(sap_model.LoadCases.ResponseSpectrum)
        
        # relate custom enumerations