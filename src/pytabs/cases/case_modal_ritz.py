# PyTABS - ETABS .NET API python wrapper
# CaseModalRitz - cCaseModalRitz interface
__all__ = ['CaseModalRitz']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import etabs
from pytabs.error_handle import handle

# import custom enumerations


class CaseModalRitz:
    """CaseModalRitz interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for modal Ritz cases
        self.modal_ritz = etabs.cCaseModalRitz(sap_model.LoadCases.ModalRitz)

        # relate custom enumerations
