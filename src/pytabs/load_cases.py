# pyTABS - ETABS .NET API python wrapper
# LoadCases - cLoadCases interface 
__all__ = ['LoadCases']

# import typing
from typing import Union
# import pyTABS error handler
from pytabs.error_handle import *
# import ETABS API .dll
from ETABSv1 import *


class LoadCases:
    """LoadCases interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        """substantiates the cLoadCases interface

        Args:
            sap_model (cSapModel): SapModel from EtabsModel
        """
        # link of SapModel interface
        self.sap_model = sap_model
        # create LoadCases interface
        self.load_cases = cLoadCases(sap_model.LoadCases)


    def count(self, case_type : Union[None, eLoadCaseType] = None) -> int:
        """Count of load cases of type if specified.
        Args:
            case_type (Union[None, eLoadCaseType], optional): Load case type enumeration. Defaults to None.

        Returns:
            int: Count of load case of type if specified.
        """
        if case_type:
            return self.load_cases.Count(case_type)
        else:
            return self.load_cases.Count()


    def get_name_list(self, case_type : Union[None, eLoadCaseType] = None) -> list[str]:
        """Retrieves the names of all defined load cases of the specified type. 

        Args:
            case_type (Union[None, eLoadCaseType], optional): Load case type enumeration. Defaults to None.

        Returns:
            list[str]: List of load case names of type if specified.
        """
        number_names = 0
        case_names = ['']
        if case_type:
            [ret, number_names, case_names] = self.load_cases.GetNameList(number_names, case_names, case_type)
        else:
            [ret, number_names, case_names] = self.load_cases.GetNameList(number_names, case_names)
        handle(ret)
        return list(case_names)