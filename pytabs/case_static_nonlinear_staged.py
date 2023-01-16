# pyTABS - ETABS .NET API python wrapper
# CaseStaticNonlinearStaged - cCaseStaticNonlinearStaged
__all__ = ['CaseStaticNonlinearStaged']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *


class CaseStaticNonlinearStaged:
    """CaseStaticNonlinearStaged interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for static nonlinear staged load cases
        self.static_nonlinear_staged = cCaseStaticNonlinearStaged(sap_model.LoadCases.StaticNonlinearStaged)
    
    
    def set_case(self, name : str) -> None:
        """Sets and existing load case to type Static Nonlinear Staged.

        :param name: name of new load case
        :type name: str
        """
        handle(self.static_nonlinear_staged.SetCase(name))