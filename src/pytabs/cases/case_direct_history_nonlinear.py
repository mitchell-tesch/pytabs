# pyTABS - ETABS .NET API python wrapper
# CaseDirectHistoryNonlinear - cCaseDirectHistoryNonlinear
__all__ = ['CaseDirectHistoryNonlinear']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


class CaseDirectHistoryNonlinear:
    """CaseDirectHistoryNonlinear interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for direct history nonlinear cases
        self.direct_history_nonlinear = etabs.cCaseDirectHistoryNonlinear(sap_model.LoadCases.DirHistNonlinear)

        # relate custom enumerations
