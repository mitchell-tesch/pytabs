# PyTABS - ETABS .NET API python wrapper
# CaseDirectHistoryLinear - cCaseDirectHistoryLinear
__all__ = ['CaseDirectHistoryLinear']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *


# import custom enumerations


# import typing


class CaseDirectHistoryLinear:
    """CaseDirectHistoryLinear interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for direct history linear cases
        self.direct_history_linear = etabs.cCaseDirectHistoryLinear(sap_model.LoadCases.DirHistLinear)

        # relate custom enumerations
