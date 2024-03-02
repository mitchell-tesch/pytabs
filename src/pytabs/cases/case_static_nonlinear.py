# PyTABS - ETABS .NET API python wrapper
# CaseStaticNonlinear - cCaseStaticNonlinear interface
__all__ = ['CaseStaticNonlinear']

# import ETABS namespace and pyTABS error handler

# import custom enumerations
from src.pytabs.enumerations import (eGeometryNonlinearityType,
                                     eLoadApplicationControlType,
                                     eDisplacementControlType,
                                     eDisplacementMonitorType,
                                     eMonitoredDisplacementDoF,
                                     eNonlinearStaticCaseLoadType)


class CaseStaticNonlinear:
    """CaseStaticNonlinearStaged interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for static nonlinear load cases
        self.static_nonlinear = etabs.cCaseStaticNonlinear(sap_model.LoadCases.StaticNonlinear)

        # relate custom enumerations
        self.eGeometryNonlinearityTypes = eGeometryNonlinearityType
        self.eLoadApplicationControlType = eLoadApplicationControlType
        self.eDisplacementControlType = eDisplacementControlType
        self.eMonitoredDisplacementType = eDisplacementMonitorType
        self.eMonitoredDisplacementDoF = eMonitoredDisplacementDoF
        self.eNonlinearStaticCaseLoadType = eNonlinearStaticCaseLoadType

    # TODO Get Methods

    def set_case(self, name: str) -> None:
        """Initializes a static nonlinear load case.

        :param name:  name of an existing or new load case. If this is an existing case, that case is modified; otherwise, a new case is added
        :type name: str
        """
        handle(self.static_nonlinear.SetCase(name))

    def set_geometric_nonlinearity(self, name: str, geometry_nonlinearity_type: eGeometryNonlinearityType) -> None:
        """Sets the geometric nonlinearity option for the specified load case.

        :param name: name of an existing static nonlinear load case
        :type name: str
        :param geometry_nonlinearity_type: one of load case 
        :type geometry_nonlinearity_type: eGeometryNonlinearityTypes
        """
        handle(self.static_nonlinear.SetGeometricNonlinearity(name, int(geometry_nonlinearity_type)))

    # TODO SetHingeUnloading - need to understand types

    def set_initial_case(self, name: str, initial_case_name: str) -> None:
        """Sets the nonlinear static load case to be considered to contain the initial conditions.

        :param name: name of existing nonlinear static load case
        :type name: str
        :param initial_case_name: name of nonlinear static load case to be considered as the initial conditions
        :type initial_case_name: str
        """
        handle(self.static_nonlinear.SetInitialCase(name, initial_case_name))

    def set_load_application(self, name: str,
                             load_application_control: eLoadApplicationControlType,
                             displacement_control: eDisplacementControlType,
                             displacement: float,
                             displacement_monitor: eDisplacementMonitorType,
                             monitored_dof: eMonitoredDisplacementDoF,
                             point_name: str,
                             generalized_displacement: str) -> None:
        """Set load case load application control parameters.

        :param name: name of existing nonlinear static load case
        :type name: str
        :param load_application_control: load application control method
        :type load_application_control: eLoadApplicationControlType
        :param displacement_control: displacement control method
        :type displacement_control: eDisplacementControlType
        :param displacement: monitored displacement magnitude
        :type displacement: float
        :param displacement_monitor: displacement monitor method
        :type displacement_monitor: eDisplacementMonitorType
        :param monitored_dof: monitored degree of freedom
        :type monitored_dof: eMonitoredDisplacementDoF
        :param point_name: name of existing point to be monitored
        :type point_name: str
        :param generalized_displacement: generalized displacement input (refer ETABS manual)
        :type generalized_displacement: str
        """
        handle(self.static_nonlinear.SetLoadApplication(name, load_application_control, displacement_control,
                                                        displacement, displacement_monitor, monitored_dof,
                                                        point_name, generalized_displacement))

    def set_loads(self, name: str, number_loads: int, load_types: list[eNonlinearStaticCaseLoadType],
                  load_names: list[str], scale_factors: list[float]) -> None:
        """Sets the load data for the specified analysis case.

        :param name: name of an existing static nonlinear load case
        :type name: str
        :param number_loads: number of loads assigned to the specified analysis case
        :type number_loads: int
        :param load_types: load type; one of `eNonlinearStaticCaseLoadType`
        :type load_types: list[eNonlinearStaticCaseLoadType]
        :param load_names: for a load this is the name of a defined load pattern, for an acceleration this is UX, UY, UZ, RX, RY or RZ and for a mode this is the mode number.
        :type load_names: list[str]
        :param scale_factors: scaling factor for load or mode, or magnitude of an acceleration
        :type scale_factors: list[float]
        """
        self.__verify_loading_details(number_loads, load_types, load_names, scale_factors)
        load_types = [load_type.value for load_type in load_types]
        [ret, _load_types, _load_names, _scale_factors] = self.static_nonlinear.SetLoads(name, number_loads,
                                                                                         load_types, load_names,
                                                                                         scale_factors)
        handle(ret)

    def set_mass_source(self, name: str, mass_source: str) -> None:
        """Sets the mass source for the specified analysis case.
        
        :param name: name of an existing static nonlinear load case
        :type name: str
        :param mass_source: name of an existing mass source
        :type mass_source: str
        """
        handle(self.static_nonlinear.SetMassSource(name, mass_source))

    def set_modal_case(self, name: str, modal_case: str) -> None:
        """Sets the mass source for the specified analysis case.

        :param name: name of an existing static nonlinear load case
        :type name: str
        :param modal_case: name of an existing modal load case
        :type modal_case: str
        """
        handle(self.static_nonlinear.SetModalCase(name, modal_case))

    def set_results_saved(self, name: str, save_multiple_steps: bool, min_saved_steps: int = 10,
                          max_saved_steps: int = 100, save_positive_displacements_only: bool = True) -> None:
        """Set results saved settings for specified load case.

        :param name: name of an existing static nonlinear load case
        :type name: str
        :param save_multiple_steps: if `True`, save multiple steps, if `False` save final step only 
        :type save_multiple_steps: bool
        :param min_saved_steps: minimum number of steps saved per stage, defaults to 10
        :type min_saved_steps: int, optional
        :param max_saved_steps: maximum number of steps saved per stage, defaults to 100
        :type max_saved_steps: int, optional
        :param save_positive_displacements_only: if `True` save positive displacement increments only, defaults to True
        :type save_positive_displacements_only: bool, optional
        """
        handle(self.static_nonlinear.SetResultsSaved(name, save_multiple_steps, min_saved_steps,
                                                     max_saved_steps, save_positive_displacements_only))

    # TODO SetSolControlParameters
    # TODO SetTargetForceParameters

    def __verify_loading_details(self, number_loads: int, load_types: list[eNonlinearStaticCaseLoadType],
                                 load_names: list[str], scale_factors: list[float]):
        """Private method for verifying loading details used by method `.set_loads`
        """
        if any(len(input_list) != number_loads for input_list in [load_types, load_names, scale_factors]):
            raise ValueError('length of all input lists must must be equal to input number_loads')
        for _l, load_type in enumerate(load_types):
            load_name = load_names[_l]
            if load_type is eNonlinearStaticCaseLoadType.ACCELERATION and (
                    load_name not in ['UX', 'UY', 'UZ', 'RX', 'RY', 'RZ']):
                raise ValueError(
                    'where load type is acceleration, the load name must be UX, UY, UZ, RX, RY or RZ, indicating the direction')
            elif load_type is eNonlinearStaticCaseLoadType.MODE:
                try:
                    int(load_name)
                except ValueError:
                    raise ValueError('where load type is mode, the load name must be a node number')
