# pyTABS - ETABS .NET API python wrapper
# LoadCases - cLoadCases interface 
__all__ = ['LoadCases']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *
from pytabs.case_static_nonlinear_staged import *

# import typing
from typing import Union
from typing import TypedDict


class LoadCaseType(TypedDict):
    """TypedDict class for load case type return"""
    case_name : str
    case_type : eLoadCaseType
    sub_type : Union[None, str]
    design_type : eLoadPatternType
    design_type_option : str
    is_automatic : bool


class LoadCases:
    """LoadCases interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create LoadCases interface
        self.load_cases = cLoadCases(sap_model.LoadCases)
        # create interface for static nonlinear staged load cases
        self.static_nonlinear_staged = CaseStaticNonlinearStaged(sap_model)


    def change_name(self, case_name : str, new_case_name :str) -> None:
        """Changes the name of a defined Load Case.

        :param case_name: name of defined load case to change
        :type case_name: str
        :param new_case_name: new name of load case
        :type new_case_name: str
        """
        handle(self.load_cases.ChangeName(case_name, new_case_name))


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


    def delete(self, case_name : str) -> None:
        """Deletes the specified load case.

        :param case_name: name of existing load case
        :type case_name: str
        """
        handle(self.load_cases.Delete(case_name))


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


    def get_type(self, case_name : str) -> LoadCaseType:
        """Retrieves the case type, design type, and auto flag for the specified load case.

        :param case_name: name of existing load case
        :type case_name: str
        :return: load case type, sub type and 
        :rtype: LoadCaseType
        """
        case_type = eLoadCaseType.Buckling
        sub_type = int()
        design_type = eLoadPatternType.Notional
        design_type_option = int()
        is_automatic = int()
        design_type_options_desc = {0: 'Program determined', 1: 'User specified'}
        is_automatic_desc = {0: False, 1: True}
        
        [ref, case_type, sub_type, design_type, 
         design_type_option, is_automatic] = self.load_cases.GetTypeOAPI_1(case_name, case_type, sub_type,
                                                                           design_type, design_type_option, is_automatic)
        handle(ref)
        sub_type = self.__determine_sub_type(case_type, sub_type)
        return {'case_name': case_name,
                'case_type': case_type,
                'sub_type': sub_type,
                'design_type': design_type,
                'design_type_option': design_type_options_desc[design_type_option],
                'is_automatic': is_automatic_desc[is_automatic]}


    def set_design_type(self, case_name : str, design_type_option : int, design_type : eLoadPatternType = eLoadPatternType.Dead) -> None:
        """Set design type of existing load case.

        :param case_name: name of existing load case
        :type case_name: str
        :param design_type_option: design type option (0 = Program determined, 1 = User specified)
        :type design_type_option: int
        :param design_type: design type, defaults to eLoadPatternType.Dead
        :type design_type: eLoadPatternType, optional
        """
        handle(self.load_cases.SetDesignType(case_name, design_type_option, design_type))
        

    def __determine_sub_type(self, case_type : eLoadCaseType, sub_type : int) -> Union[None, str]:
        """Private method to determine string of load case sub type.

        :param case_type: load case type
        :type case_type: eLoadCaseType
        :param sub_type: load case sub type integer
        :type sub_type: int
        :return: load case sub type description, if applicable
        :rtype: Union[None, str]
        """
        if int(case_type) in [int(eLoadCaseType.NonlinearStatic), int(eLoadCaseType.Modal), int(eLoadCaseType.LinearHistory)]:
            if int(case_type) == int(eLoadCaseType.NonlinearStatic):
                sub_types_dict = {1: 'Nonlinear', 2: 'Nonlinear staged construction'}
            elif int(case_type) == int(eLoadCaseType.Modal):
                sub_types_dict = {1: 'Eigen', 2: 'Ritz'}
            else:
                sub_types_dict = {1: 'Transient', 2: 'Periodic'}
            return sub_types_dict[sub_type]