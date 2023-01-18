# pyTABS - ETABS .NET API python wrapper
# CaseStaticNonlinear - cCaseStaticNonlinear
__all__ = ['CaseStaticNonlinear']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *

# import custom enumerations
from pytabs.enumerations import eGeometryNonlinearityTypes


class CaseStaticNonlinear:
    """CaseStaticNonlinearStaged interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for static nonlinear load cases
        self.static_nonlinear = cCaseStaticNonlinear(sap_model.LoadCases.StaticNonlinear)
    
    
    def set_case(self, name : str) -> None:
        """Initializes a static nonlinear load case.

        :param name:  name of an existing or new load case. If this is an existing case, that case is modified; otherwise, a new case is added
        :type name: str
        """
        handle(self.static_nonlinear.SetCase(name))


    def set_geometric_nonlinearity(self, name : str, geometry_nonlinearity_type : eGeometryNonlinearityTypes) -> None:
        handle(self.static_nonlinear.SetGeometricNonlinearity(name, int(geometry_nonlinearity_type)))