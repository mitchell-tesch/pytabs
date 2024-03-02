# PyTABS - ETABS .NET API python wrapper
# CaseModalHistoryNonlinear - cCaseModalHistoryNonlinear interface
__all__ = ['CaseModalHistoryNonlinear']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *


# import custom enumerations


# import typing


class CaseModalHistoryNonlinear:
    """CaseModalHistoryNonlinear interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for modal history Nonlinear cases
        self.modal_history_nonlinear = etabs.cCaseModalHistoryNonlinear(sap_model.LoadCases.ModHistNonlinear)

        # relate custom enumerations
