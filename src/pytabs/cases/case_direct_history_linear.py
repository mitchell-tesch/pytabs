# PyTABS - ETABS .NET API python wrapper
# CaseDirectHistoryLinear - cCaseDirectHistoryLinear
__all__ = ['CaseDirectHistoryLinear']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import etabs
from pytabs.error_handle import handle

# import custom enumerations


class CaseDirectHistoryLinear:
    """CaseDirectHistoryLinear interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for direct history linear cases
        self.direct_history_linear = etabs.cCaseDirectHistoryLinear(sap_model.LoadCases.DirHistLinear)

        # relate custom enumerations
