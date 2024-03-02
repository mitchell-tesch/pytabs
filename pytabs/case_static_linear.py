# PyTABS - ETABS .NET API python wrapper
# CaseStaticLinear - cCaseStaticLinear interface
__all__ = ['CaseStaticLinear']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations
from pytabs.enumerations import eLinearStaticCaseLoadType

# import typing
from typing import TypedDict


class StaticLinearLoadData(TypedDict):
    """TypedDict class for static linear load case loading data"""
    case_name: str
    load_types: list[eLinearStaticCaseLoadType]
    load_names: list[str]
    scaling_factors: list[float]


class CaseStaticLinear:
    """CaseStaticLinearStaged interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for static linear load cases
        self.static_linear = etabs.cCaseStaticLinear(sap_model.LoadCases.StaticLinear)

        # relate custom enumerations
        self.eLinearStaticCaseLoadType = eLinearStaticCaseLoadType

    def get_initial_case(self, name: str) -> str:
        """Retrieves the initial condition assumed for the specified load case.

        :param name: name of an existing static linear load case
        :type name: str
        :return: blank, None, or the name of an existing analysis case
        :rtype: str
        """
        initial_case = str()
        [ref, initial_case] = self.static_linear.GetInitialCase(name, initial_case)
        handle(ref)
        return initial_case

    def get_loads(self, name: str) -> StaticLinearLoadData:
        """Retrieves the load data for the specified load case.

        :param name: name of an existing static linear load case
        :type name: str
        :return: load data
        :rtype: StaticLinearLoadData
        """
        _number_names = int()
        load_types = [str()]
        load_names = [str()]
        scaling_factors = [float()]
        [ret, _number_names, load_types,
         load_names, scaling_factors] = self.static_linear.GetLoads(name, _number_names, load_types,
                                                                    load_names, scaling_factors)
        handle(ret)
        load_types = [eLinearStaticCaseLoadType(load_type) for load_type in load_types]
        return {'case_name': name,
                'load_types': load_types,
                'load_names': load_names,
                'scaling_factors': scaling_factors}

    def set_case(self, name: str) -> None:
        """Initializes a static linear load case.

        :param name: name of an existing or new load case
        :type name: str
        """
        handle(self.static_linear.SetCase(name))

    def set_initial_case(self, name: str, initial_case_name: str) -> None:
        """Sets the initial condition for the specified load case.

        :param name: name of an existing static linear load case
        :type name: str
        :param initial_case_name:  name of an existing analysis case, can be blank or None
        :type initial_case_name: str
        """
        handle(self.static_linear.SetInitialCase(name, initial_case_name))

    def set_loads(self, name: str, number_loads: int, load_types: list[eLinearStaticCaseLoadType],
                  load_names: list[str], scale_factors: list[float]) -> None:
        """Sets the load data for the specified analysis case.

        :param name: name of an existing static nonlinear load case
        :type name: str
        :param number_loads: number of loads assigned to the specified analysis case
        :type number_loads: int
        :param load_types: load type; one of `eLinearStaticCaseLoadType`
        :type load_types: list[eLinearStaticCaseLoadType]
        :param load_names: for a load this is the name of a defined load pattern, for an acceleration this is UX, UY, UZ, RX, RY or RZ and for a mode this is the mode number.
        :type load_names: list[str]
        :param scale_factors: scaling factor for load or mode, or magnitude of an acceleration
        :type scale_factors: list[float]
        """
        self.__verify_loading_details(number_loads, load_types, load_names, scale_factors)
        load_types = [load_type.value for load_type in load_types]
        [ret, _load_types, _load_names, _scale_factors] = self.static_linear.SetLoads(name, number_loads,
                                                                                      load_types, load_names,
                                                                                      scale_factors)
        handle(ret)

    def __verify_loading_details(self, number_loads: int, load_types: list[eLinearStaticCaseLoadType],
                                 load_names: list[str], scale_factors: list[float]):
        """Private method for verifying loading details used by method `.set_loads`
        """
        if any(len(input_list) != number_loads for input_list in [load_types, load_names, scale_factors]):
            raise ValueError('length of all input lists must must be equal to input number_loads')
        for _l, load_type in enumerate(load_types):
            load_name = load_names[_l]
            if load_type is eLinearStaticCaseLoadType.ACCELERATION and (
                    load_name not in ['UX', 'UY', 'UZ', 'RX', 'RY', 'RZ']):
                raise ValueError('where load type is acceleration, the load name must be UX, UY, UZ, RX, RY or RZ, indicating the direction')
