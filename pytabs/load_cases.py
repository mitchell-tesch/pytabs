# pyTABS - ETABS .NET API python wrapper
# LoadCases - cLoadCases interface 
__all__ = ['LoadCases']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *

# import typing
from typing import Union


class LoadCases:
    """LoadCases interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create LoadCases interface
        self.load_cases = cLoadCases(sap_model.LoadCases)


    def count(self, case_type : Union[None, eLoadCaseType] = None) -> int:
        """Count of load cases of type if specified.

        :param case_type: load case type enumeration, defaults to None
        :type case_type: Union[None, eLoadCaseType], optional
        :return: count of load case of type, if specified, else all
        :rtype: int
        """
        if case_type:
            return self.load_cases.Count(case_type)
        else:
            return self.load_cases.Count()


    def get_name_list(self, case_type : Union[None, eLoadCaseType] = None) -> list[str]:
        """Retrieves the names of all defined load cases of the specified type.

        :param case_type: load case type enumeration, defaults to None
        :type case_type: Union[None, eLoadCaseType], optional
        :return: load case names of type, if specified, else all
        :rtype: list[str]
        """
        number_names = int()
        case_names = [str()]
        if case_type:
            [ret, number_names, case_names] = self.load_cases.GetNameList(number_names, case_names, case_type)
        else:
            [ret, number_names, case_names] = self.load_cases.GetNameList(number_names, case_names)
        handle(ret)
        return list(case_names)