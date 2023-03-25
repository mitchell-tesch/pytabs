# pyTABS - ETABS .NET API python wrapper
# CaseModalEigen - cCaseModalEigen
__all__ = ['CaseModalEigen']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class CaseModalEigen:
    """CaseModalEigen interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for modal Eigen cases
        self.modal_eigen = etabs.cCaseModalEigen(sap_model.LoadCases.ModalEigen)
        
        # relate custom enumerations