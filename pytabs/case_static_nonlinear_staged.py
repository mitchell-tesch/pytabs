# pyTABS - ETABS .NET API python wrapper
# CaseStaticNonlinearStaged - cCaseStaticNonlinearStaged
__all__ = ['CaseStaticNonlinearStaged']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *


# import custom enumerations
from pytabs.enumerations import (eGeometryNonlinearityType,
                                 eLoadApplicationControlType,
                                 eDisplacementControlType,
                                 eDisplacementMonitorType,
                                 eMonitoredDisplacementDoF,
                                 eStageOperationType,
                                 eStageObjectType,
                                 eStageMyType)


class CaseStaticNonlinearStaged:
    """CaseStaticNonlinearStaged interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for static nonlinear staged load cases
        self.static_nonlinear_staged = cCaseStaticNonlinearStaged(sap_model.LoadCases.StaticNonlinearStaged)
        
        # relate custom enumerations
        self.eGeometryNonlinearityTypes = eGeometryNonlinearityType
        self.eLoadApplicationControlType = eLoadApplicationControlType
        self.eDisplacementControlType = eDisplacementControlType
        self.eMonitoredDisplacementType = eDisplacementMonitorType
        self.eMonitoredDisplacementDoF = eMonitoredDisplacementDoF
        self.eStageOperationType = eStageOperationType
        self.eStageObjectType = eStageObjectType
        self.eStageMyType = eStageMyType


    # TODO - Get Methods


    def set_case(self, name : str) -> None:
        """Initializes a static nonlinear staged load case.

        :param name: name of an existing or new load case
        :type name: str
        """
        handle(self.static_nonlinear_staged.SetCase(name))


    def set_geometric_nonlinearity(self, name : str, geometry_nonlinearity_type : eGeometryNonlinearityType) -> None:
        """Sets the geometric nonlinearity option for the specified load case.

        :param name: name of an existing static nonlinear staged load case
        :type name: str
        :param geometry_nonlinearity_type: one of load case 
        :type geometry_nonlinearity_type: eGeometryNonlinearityTypes
        """
        handle(self.static_nonlinear_staged.SetGeometricNonlinearity(name, int(geometry_nonlinearity_type)))


    # TODO SetHingeUnloading - need to understand types


    def set_initial_case(self, name : str, initial_case_name : str) -> None:
        """Sets the nonlinear static load case to be considered to contain the initial conditions.

        :param name: name of existing nonlinear static staged load case
        :type name: str
        :param initial_case_name: name of nonlinear static load case to be considered as the initial conditions
        :type initial_case_name: str
        """
        handle(self.static_nonlinear_staged.SetInitialCase(name, initial_case_name))


    def set_mass_source(self, name : str, mass_source : str) -> None:
        """Sets the mass source for the specified analysis case.

        :param name: name of an existing static nonlinear staged load case
        :type name: str
        :param mass_source: name of an existing mass source
        :type mass_source: str
        """
        handle(self.static_nonlinear_staged.SetMassSource(name, mass_source))


    def set_material_nonlinearity(self, name : str, time_dependent_materials : bool = True) -> None:
        """Sets the status of time dependent material properties for the specified load case.

        :param name: name of an existing static nonlinear staged load case
        :type name: str
        :param time_dependent_materials: `True` to enable time dependent materials, defaults to True
        :type time_dependent_materials: bool, optional
        """
        handle(self.static_nonlinear_staged.SetMaterialNonlinearity(name, time_dependent_materials))


    # TODO SetResultsSaved

    # TODO SetSolControlParameters


    def set_stage_data(self, name : str, stage : int, number_operations : int,
                       operation_types : list[eStageOperationType],
                       object_types : list[eStageObjectType],
                       object_names : list[str],
                       ages : list[float],
                       my_types : list[eStageMyType],
                       my_names : list[str],
                       scaling_factors : list[float]) -> None:
        """Sets stage data for the specified stage in the specified load case.

        :param name: name of an existing static nonlinear staged load case
        :type name: str
        :param stage: stage in the specified load case for which data is to be set
        :type stage: int
        :param number_operations: number of operations to set for the specified stage 
        :type number_operations: int
        :param operation_types: operation type of each operation
        :type operation_types: list[eStageOperationType]
        :param object_types: object type associated with each operation
        :type object_types: list[eStageObjectType]
        :param object_names: name of the object associated with each operation
        :type object_names: list[str]
        :param ages: ages of the added structure at the time it is added, in days (only applies to .ADD operation types)
        :type ages: list[float]
        :param my_types: load type or object type for each operation, depending on operation type (refer CSI ETABS API Manual)
        :type my_types: list[eStageMyType]
        :param my_names: load assignment or object name for each operation, depending on operation type (refer CSI ETABS API Manual)
        :type my_names: list[str]
        :param scaling_factors:  scale factor for the load assigned to the operation (only applies to .LOAD_NEW and .LOAD_ALL operation types)
        :type scaling_factors: list[float]
        """
        self.__verify_stage_operations(number_operations, operation_types, object_types,
                                         object_names, ages, my_types, my_names, scaling_factors)
        operation_types = [operation_type.value for operation_type in operation_types]
        object_types = [object_type.value for object_type in object_types]
        my_types = [my_type.value for my_type in my_types]
        [ret, ret_operation_types,
         ret_object_types, ret_object_names,
         ages, my_types, my_names, scaling_factors] = self.static_nonlinear_staged.SetStageData_2(name,
                                                                                                  stage,
                                                                                                  number_operations,
                                                                                                  operation_types,
                                                                                                  object_types,
                                                                                                  object_names,
                                                                                                  ages,
                                                                                                  my_types,
                                                                                                  my_names,
                                                                                                  scaling_factors)
        handle(ret)


    def set_stage_definitions(self, name : str, number_stages : int,
                              durations : list[float],
                              output_statuses : list[bool],
                              output_names : list[str],
                              comments : list[str]) -> None:
        """Sets the stage definition data for the specified load case.

        :param name: name of an existing static nonlinear staged load case
        :type name: str
        :param number_stages: number of stages to be defined for the specified load case
        :type number_stages: int
        :param durations: duration in days for each stage
        :type durations: list[float]
        :param output_statuses: `True` or `False`, indicating if analysis output is to be saved for each stage 
        :type output_statuses: list[bool]
        :param output_names: user-specified output name for each stage
        :type output_names: list[str]
        :param comments: user comment for each stage, may be a blank string
        :type comments: list[str]
        """
        [ret, ret_durations, ret_output_statuses,
         ret_output_names, comments] = self.static_nonlinear_staged.SetStageDefinitions_2(name, number_stages,
                                                                                          durations, output_statuses,
                                                                                          output_names, comments)
        handle(ret)


    def __verify_stage_operations(self, number_operations : int, operation_types : list[eStageOperationType],
                                  object_types : list[eStageObjectType], object_names : list[str],
                                  ages : list[float], my_types : list[eStageMyType], my_names : list[str],
                                  scaling_factors : list[float]) -> None:
        """Private method for verifying staging details used by method `.set_stage_data`
        """
        input_lists = [operation_types, object_types, object_names, ages, my_types, my_names, scaling_factors]
        if any(len(input_list) != number_operations for input_list in input_lists):
            raise ValueError('length of all input lists must must be equal to input number_operations')
        # TODO add detailed validation of operation requirements


    def __verify_stage_definitions(self, number_stages : int, durations : list[float], output_statuses : list[bool],
                                   output_names : list[str], comments : list[str]) -> None:
        """Private method for verifying stage definitions used by method `.set_stage_definitions`
        """
        input_lists = [number_stages, durations, output_statuses, output_names, comments]
        if any(len(input_list) != number_stages for input_list in input_lists):
            raise ValueError('length of all input lists must must be equal to input number_stages')
