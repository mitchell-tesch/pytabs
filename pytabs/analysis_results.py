# pyTABS - ETABS .NET API python wrapper
# AnalysisResults - cAnalysisResults interface 
__all__ = ['AnalysisResults']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *


# import custom enumerations
from pytabs.enumerations import (eResultsSetupStepOutOption, eResultsSetupComboOutOption)


# import typing
from typing import TypedDict

class BaseReact(TypedDict) : 
    """TypedDict class for base_react return"""
    number_results : int
    story : list[str]
    load_case : list[str]
    step_type : list[str]
    step_number : list[float]
    x_direction_force : list[float]
    y_direction_force : list[float]
    z_direction_force : list[float]
    moment_x : list[float]
    param_moment_y : list[float]
    moment_z : list[float]
    x_coordinate : list[float]
    y_coordinate : list[float]
    z_coordinate : list[float]

class BaseReactWithCentroid(TypedDict) : 
    """TypedDict class for base_react_with_centroid return"""
    number_results : int
    story : list[str]
    load_case : list[str]
    step_type : list[str]
    step_number : list[float]
    x_direction_force : list[float]
    y_direction_force : list[float]
    z_direction_force : list[float]
    moment_x : list[float]
    param_moment_y : list[float]
    moment_z : list[float]
    x_coordinate : list[float]
    y_coordinate : list[float]
    z_coordinate : list[float]
    x_centroid_for_x_direction : list[float]
    y_centroid_for_x_direction : list[float]
    z_centroid_for_x_direction : list[float]
    x_centroid_for_y_direction : list[float]
    y_centroid_for_y_direction : list[float]
    z_centroid_for_y_direction : list[float]
    x_centroid_for_z_direction : list[float]
    y_centroid_for_z_direction : list[float]
    z_centroid_for_z_direction : list[float]

class BucklingFactor(TypedDict) : 
    """TypedDict class for buckling_factor return"""
    number_results : int
    load_case : list[str]
    step_type : list[str]
    step_number : list[float]
    factor : list[float]

class JointDisplacement(TypedDict) : 
    """TypedDict class for joint_displacement return"""
    number_results : int 
    object_name : list[str]
    element_name : list[str]
    load_case : list[str]
    step_type : list[str]
    step_number : list[float]
    delta_u1 : list[float]
    delta_u2 : list[float]
    delta_u3 : list[float]
    rotation_r1 : list[float]
    rotation_r2 : list[float]
    rotation_r3 : list[float]


class ModalLoadParticipationRatios (TypedDict) : 
    """Typed class for modal_load_participation_ratios"""
    number_results : int 
    load_case : list[str]
    item_type : list[str]
    item : list[str]
    stat : list[float]
    dyn : list[float]

class ModalParticipatingMassRatios (TypedDict) : 
    """TypedDict class for modal_participating_mass_ratios"""
    number_results : int
    load_case : list[str]
    step_type : list[str]
    step_number : list[float]
    period : list[float]
    delta_x : list[float]
    delta_y : list[float]
    delta_z : list[float]
    sum_delta_x : list[float]
    sum_delta_y : list[float]
    sum_delta_z : list[float]
    rotation_x : list[float]        
    rotation_y : list[float]
    rotation_z : list[float]
    sum_rotation_x : list[float]
    sum_rotation_y : list[float]
    sum_rotation_z : list[float]

class ModalParticipationFactors(TypedDict) : 
    """TypedDict class for modal_participation_factors"""
    number_results : int
    load_case : list[str]
    step_type : list[str]
    step_number : list[float]
    period : list[float]
    delta_x : list[float]
    delta_y : list[float]
    delta_z : list[float]
    rotation_x : list[float]        
    rotation_y : list[float]
    rotation_z : list[float]
    modal_mass : list[float]
    modal_stiff : list[float]

class ModalPeriod(TypedDict):
    """TypedDict class for modal_period return"""
    number_results : int
    load_case : list[str]
    step_type : list[str]
    step_number : list[int]
    period : list[float]
    frequency : list[float]
    circular_frequency : list[float]
    eigen_value : list[float]
    
    
class PierForce(TypedDict):
    """TypedDict class for pir_force return"""
    number_results : int
    story_name : list[str]
    pier_name : list[str]
    load_case : list[str]
    location : list[str]
    p : list[float]
    v2 : list[float]
    v3 : list[float]
    t : list[float]
    m2 : list[float]
    m3 : list[float]

class SectionCutAnalysis(TypedDict) : 
    """TypedDict class for section_cut_analysis return"""
    number_results : int
    section_cut : list[str]
    load_case : list[str]
    step_type : list[str]
    step_number : list[float]
    force1 : list[float]
    force2 : list[float]
    force3 : list[float]
    moment1 : list[float]
    moment2 : list[float]
    moment3 : list[float]

class SectionCutDesign(TypedDict) : 
    """TypedDict class for section_cut_design return"""
    number_results : int
    section_cut : list[str]
    load_case : list[str]
    step_type : list[str]
    step_number : list[float]
    axial : list[float]
    shear2 : list[float]
    shear3 : list[float]
    torsion : list[float]
    moment2 : list[float]
    moment3 : list[float]

class SpandrelForce(TypedDict) : 
    """TypedDict class for spandrel_force return"""
    number_results : int
    story_name : list[str]
    spandrel_name : list[str]
    load_case : list[str]
    loaction : list[str]
    axial : list[float]
    shear2 : list[float]
    shear3 : list[float]
    torsion : list[float]
    moment2 : list[float]
    moment3 : list[float]

class StoryDrift(TypedDict): 
    """TypedDict class for story_drift return"""
    number_results : int
    story : list[str]
    load_case : list[str]
    step_type : list[str]
    step_number : list[float]
    direction : list[str]
    drift : list[float]
    label : list[str]
    x_direction : list[float]
    y_direction : list[float]
    z_direction : list[float]



class AnalysisResults:
    """AnalysisResults interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create AnalysisResultsSetup interface
        self.analysis_results_setup = etabs.cAnalysisResultsSetup(sap_model.Results.Setup)
        # create AnalysisResults interface
        self.analysis_results = etabs.cAnalysisResults(sap_model.Results)
        
        # relate custom enumerations
        self.eResultsSetupStepOutOption = eResultsSetupStepOutOption
        self.eResultsSetupComboOutOption =  eResultsSetupComboOutOption


    # Analysis Results Setup Methods
    def deselect_all_cases_combos_for_output(self) -> None:
        """Deselects all load cases and response combinations for output."""
        handle(self.analysis_results_setup.DeselectAllCasesAndCombosForOutput())


    def get_case_selected_for_output(self, case_name : str) -> bool:
        """Checks if a load case is selected for output.

        :param case_name: name of an existing load case
        :type case_name: str
        :return: `True` if the Case selected for output, `False` otherwise
        :rtype: bool
        """
        [ret, selected] = self.analysis_results_setup.GetCaseSelectedForOutput(case_name)
        handle(ret)
        return selected


    def get_combo_selected_for_output(self, combo_name : str) -> bool:
        """Checks if a load combination is selected for output.

        :param combo_name: name of an existing combination
        :type combo_name: str
        :return: `True` if the Combination selected for output, `False` otherwise
        :rtype: bool
        """
        [ret, selected] = self.analysis_results_setup.GetComboSelectedForOutput(combo_name)
        handle(ret)
        return selected
    
    
    def get_base_reaction_location(self) -> tuple[float, float, float]:
        """Retrieves the global coordinates of the location at which the base reactions are reported.

        :return: global coordinate of 3d point where base reactions are reported (gx, gy, gz)
        :rtype: tuple[float, float, float]
        """
        gx = float()
        gy = float()
        gz = float()
        [ret, gx, gy, gz] = self.analysis_results_setup.GetOptionBaseReactLoc(gx, gy, gz)
        handle(ret)
        return (gx, gy, gz)
    

    def get_buckling_mode_setup(self) -> tuple[int, int, bool]: 
        """Retrieves the mode buckling range for output. 
        
        :return: return[0] - first buckling mode, return[1] - last buckling mode, return[2] - all buckling modes
        :rtype: tuple[int, int, bool]"""

        start_buckling_mode = int()
        end_buckling_mode = int()
        all_buckling_modes = bool()
        [ret, start_buckling_mode,
        end_buckling_mode, all_buckling_modes] = self.analysis_results_setup.GetOptionBucklingMode(start_buckling_mode, 
                                                                                                    end_buckling_mode,
                                                                                                    all_buckling_modes)
        handle(ret)
        return (start_buckling_mode, end_buckling_mode, all_buckling_modes)


    def get_direct_history_setup(self) -> eResultsSetupStepOutOption:
        """Retrieves the output option for direct history results.

        :return: one of step out options (envelopes, step-by-step or last-step)
        :rtype: eResultsSetupStepOutOption
        """
        option = int()
        [ret, option] = self.analysis_results_setup.GetOptionDirectHist(option)
        handle(ret)
        return eResultsSetupStepOutOption(option)


    def get_modal_history_setup(self) -> eResultsSetupStepOutOption: 
        """Retrieves the output option for modal history results. 

        :return: one of step out options (envelopes, step-by-step or last-step)
        :rtype: eResultsSetupStepOutOption
        """
        option = int()
        [ret, option] = self.analysis_results_setup.GetOptionModalHist(option)
        handle(ret)
        return eResultsSetupStepOutOption(option)


    def get_mode_shape_setup(self) -> tuple[bool, int, int]:
        """Retrieves the mode shape range for output.

        :return: return[0] - all modes, return[1] - first mode, return[2] - last mode
        :rtype: tuple[bool, int, int]
        """
        start_mode = int()
        end_mode = int()
        all_modes = bool()
        [ret, start_mode, end_mode, all_modes] = self.analysis_results_setup.GetOptionModeShape(start_mode, end_mode, all_modes)
        handle(ret)
        return (all_modes, start_mode, end_mode)
    
    
    # TODO GetOptionMultiStepStatic - setup options within ETABS unknown
    

    def get_combination_setup(self) -> eResultsSetupComboOutOption:
        """Retrieves the combination option setup.

        :return: one of combo options (envelopes or multiple)
        :rtype: eResultsSetupComboOutOption
        """
        option = int()
        [ret, option] = self.analysis_results_setup.GetOptionMultiValuedCombo(option)
        handle(ret)
        return eResultsSetupComboOutOption(option)
    
    
    def get_nonlinear_setup(self) -> eResultsSetupStepOutOption:
        """Retrieves the non-linear static results option.

        :return: one of step out options (envelopes, step-by-step or last-step)
        :rtype: eResultsSetupStepOutOption
        """
        option = int()
        [ret, option] = self.analysis_results_setup.GetOptionNLStatic(option)
        handle(ret)
        return eResultsSetupStepOutOption(option)
    
    
    def set_case_selected_for_output(self, case_name : str, select_state : bool = True) -> None:
        """Sets a load case selected for output flag.

        :param case_name: name of existing load case
        :type case_name: str
        :param select_state: select case for output, defaults to `True`
        :type select_state: bool, optional
        """
        handle(self.analysis_results_setup.SetCaseSelectedForOutput(case_name, select_state))
    
    
    def set_combo_selected_for_output(self, combo_name : str, select_state : bool = True) -> None:
        """Sets a combination selected for output flag.

        :param combo_name: name of the existing combination
        :type combo_name: str
        :param select_state: select combination for output defaults to `True`
        :type select_state: bool, optional
        """
        handle(self.analysis_results_setup.SetComboSelectedForOutput(combo_name, select_state))


    def set_base_reaction_location(self, point : tuple[float, float, float]) -> None:
        """Sets the global coordinates of the location at which the base reactions are reported.

        :param point: global coordinate of 3d point where base reactions are to be reported (gx, gy, gz)
        :type point: tuple[float, float, float]
        """
        handle(self.analysis_results_setup.SetOptionBaseReactLoc(point[0], point[1], point[2]))
    
    
    def set_buckling_mode_setup(self, start_buckling_mode : int, end_buckling_mode : int, all_buckling_modes : bool = False) -> None: 
        """Sets the buckling mode range for output. 
        
        :param start_buckling_mode: first buckling mode number 
        :type start_buckling_mode: int
        :param end_buckling_mode: last buckling mode number 
        :type start_buckling_mode: int
        :param all_buckling_modes: all buckling modes, defaults to `False` 
        :type start_buckling_mode: bool, optional 
        """
        handle(self.analysis_results_setup.SetOptionBucklingMode(start_buckling_mode, end_buckling_mode, all_buckling_modes))
        
        
    def set_direct_history_setup(self, option : eResultsSetupStepOutOption) -> None: 
        """Sets the direct history results option.
        
        :param option: one of step out options (envelopes, step-by-step or last-step)
        :type option:  eResultsSetupStepOutOption
        """
        handle(self.analysis_results_setup.SetOptionDirectHist(option.value))


    def set_modal_history_setup(self, option : eResultsSetupStepOutOption) -> None: 
        """Sets the modal history results option.
        
        :param option: one of step out options (envelopes, step-by-step or last-step)
        :type option:  eResultsSetupStepOutOption
        """
        handle(self.analysis_results_setup.SetOptionModalHist(option.value))
        
        
    def set_mode_shape_setup(self, start_mode : int, end_mode : int, all_modes : bool = False) -> None:
        """Sets the mode shape range for output.

        :param start_mode: first mode number
        :type start_mode: int
        :param end_mode: last mode number
        :type end_mode: int
        :param all_modes: all modes, defaults to False
        :type all_modes: bool, optional
        """
        handle(self.analysis_results_setup.SetOptionModeShape(start_mode, end_mode, all_modes))


    # TODO SetOptionMultiStepStatic - setup options within ETABS unknown
    

    def set_combination_setup(self, option : eResultsSetupComboOutOption) -> None:
        """Sets the non-linear static results option.
        
        :param option: one of combo options (envelopes or multiple)
        :type option: eResultsSetupComboOutOption
        """
        handle(self.analysis_results_setup.SetOptionMultiValuedCombo(option.value))


    def set_nonlinear_setup(self, option : eResultsSetupStepOutOption) -> None:
        """Sets the non-linear static results option.
        
        :param option: one of step out options (envelopes, step-by-step or last-step)
        :type option: eResultsSetupStepOutOption
        """
        handle(self.analysis_results_setup.SetOptionNLStatic(option.value))


    def base_react(self) -> BaseReact : 
            """Reports the structure total base reactions
            
            :return: total base reactions analysis results 
            :rtype: BaseReact
            """
            number_results = int() 
            load_case = [str()]
            step_type = [str()]
            step_num = [float()]
            x_direction_force = [float()]
            y_direction_force = [float()]
            z_direction_force = [float()]
            moment_x = [float()]
            param_moment_y = [float()]
            moment_z = [float()]
            x_coordinate = [float()]
            y_coordinate = [float()]
            z_coordinate = [float()]

            [ret, number_results, load_case, step_type, step_num, x_direction_force, 
            y_direction_force, z_direction_force, moment_x, param_moment_y, 
            moment_z, x_coordinate, y_coordinate, z_coordinate] = self.analysis_results.BaseReact(number_results, load_case, step_type, step_num, x_direction_force, y_direction_force, 
                                                                                                z_direction_force, moment_x, param_moment_y, moment_z, x_coordinate, y_coordinate, z_coordinate)
            #handle(ret)
            return{'number_results' : number_results,
                    'load_case' : list(load_case),
                    'step_type' : list(step_type),
                    'step_num' : list(step_num),
                    'x_direction_force' : list(x_direction_force),
                    'y_direction_force' : list(y_direction_force),
                    'z_direction_force' : list(z_direction_force),
                    'moment_x' : list(moment_x),
                    'param_moment_y' : list(param_moment_y),
                    'moment_z' : list(moment_z),
                    'x_coordinate' : list(x_coordinate),
                    'y_coordinate' : list(y_coordinate),
                    'z_coordinate' : list(z_coordinate)}


    def base_react_with_centroid(self) -> BaseReactWithCentroid : 
            """Reports the structure total base reactions and includes information on the centroid of the translational reaction forces.
            
            :return: Base reaction with centriod analysis results 
            :rtype: BaseReactWithCentroid
            """
            number_results = int() 
            load_case = [str()]
            step_type = [str()]
            step_number = [float()]
            x_direction_force = [float()]
            y_direction_force = [float()]
            z_direction_force = [float()]
            moment_x = [float()]
            param_moment_y = [float()]
            moment_z = [float()]
            x_coordinate = [float()]
            y_coordinate = [float()]
            z_coordinate = [float()]
            x_centroid_for_x_direction = [float()]
            y_centroid_for_x_direction = [float()]
            z_centroid_for_x_direction = [float()]
            x_centroid_for_y_direction = [float()]
            y_centroid_for_y_direction = [float()]
            z_centroid_for_y_direction = [float()]
            x_centroid_for_z_direction = [float()]
            y_centroid_for_z_direction = [float()]
            z_centroid_for_z_direction = [float()]

            [ret, number_results, load_case, step_type, step_number, x_direction_force, y_direction_force, z_direction_force, moment_x, param_moment_y, moment_z, x_coordinate, y_coordinate, 
            z_coordinate, x_centroid_for_x_direction, y_centroid_for_x_direction, z_centroid_for_x_direction, x_centroid_for_y_direction, y_centroid_for_y_direction, 
            z_centroid_for_y_direction, x_centroid_for_z_direction, y_centroid_for_z_direction, z_centroid_for_z_direction] = self.analysis_results.BaseReactWithCentroid(number_results, load_case, step_type, step_number, x_direction_force, y_direction_force, z_direction_force, moment_x, param_moment_y, moment_z, x_coordinate, y_coordinate, 
                                                                                                                                                                        z_coordinate, x_centroid_for_x_direction, y_centroid_for_x_direction, z_centroid_for_x_direction, x_centroid_for_y_direction, y_centroid_for_y_direction, 
                                                                                                                                                                        z_centroid_for_y_direction, x_centroid_for_z_direction, y_centroid_for_z_direction, z_centroid_for_z_direction)
            #handle(ret)
            return{'number_results' : number_results,
                    'load_case' : list(load_case),
                    'step_type' : list(step_type),
                    'step_num' : list(step_number),
                    'x_direction_force' : list(x_direction_force),
                    'y_direction_force' : list(y_direction_force),
                    'z_direction_force' : list(z_direction_force),
                    'moment_x' : list(moment_x),
                    'param_moment_y' : list(param_moment_y),
                    'moment_z' : list(moment_z),
                    'x_coordinate' : list(x_coordinate),
                    'y_coordinate' : list(y_coordinate),
                    'z_coordinate' : list(z_coordinate), 
                    'x_centroid_for_x_direction' : list(x_centroid_for_x_direction),
                    'y_centroid_for_x_direction' : list(y_centroid_for_x_direction),
                    'z_centroid_for_x_direction' : list(z_centroid_for_x_direction),
                    'x_centroid_for_y_direction' : list(x_centroid_for_y_direction),
                    'y_centroid_for_y_direction' : list(y_centroid_for_y_direction),
                    'z_centroid_for_y_direction' : list(z_centroid_for_y_direction),
                    'x_centroid_for_z_direction' : list(x_centroid_for_z_direction),
                    'y_centroid_for_z_direction' : list(y_centroid_for_z_direction),
                    'z_centroid_for_z_direction' : list(z_centroid_for_z_direction)}


    def buckling_factor(self) -> BucklingFactor : 
            """Reports buckling factors obtained from buckling load cases, 
            
            :return: Buckling factors analysis results 
            :rtype: BucklingFactor
            """
            number_results = int() 
            load_case = [str()]
            step_type = [str()]
            step_number = [float()]
            factor = [float()]

            [ret, number_results, load_case, step_type, step_number, factor] = self.analysis_results.BucklingFactor(number_results, load_case, step_type, step_number, factor)

            #handle(ret)
            return{'number_results' : number_results,
                    'load_case' : list(load_case),
                    'step_type' : list(step_type),
                    'step_num' : list(step_number),
                    'factor' : list(factor)}

    def joint_displacement(self, joint : str, item_type_element : etabs.eItemTypeElm) -> JointDisplacement : 
        """ Reports the joint displacements for the specified point elements.
        
        Note: The displacements reported by this function are relative displacements 
        
        :return: Joint Displacement analysis results 
        :rtype: JointDisplacement
        """
        number_results = int()
        object_name = [str()]
        element_name = [str()]
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        delta_u1 = [float()]
        delta_u2 = [float()]
        delta_u3 = [float()]
        rotation_r1 = [float()]
        rotation_r2 = [float()]
        rotation_r3 = [float()]

        [ret, number_results, object_name, element_name, 
        load_case, step_type, step_number, delta_u1, 
        delta_u2, delta_u3, rotation_r1, 
        rotation_r2, rotation_r3] = self.analysis_results.JointDispl(joint, item_type_element, number_results, object_name, element_name, 
                                                                    load_case, step_type, step_number, delta_u1, delta_u2, delta_u3, rotation_r1, 
                                                                    rotation_r2, rotation_r3)
        
        # handle(ret)
        return {'Number Results' : number_results, 
                'Object Name' : object_name,
                'Element Name' : element_name, 
                'Load Case' : load_case,
                'Step Type' : step_type,
                'Step Number': step_number, 
                'delta u1 (mm)' : list(delta_u1), 
                'delta u2 (mm)' : delta_u2,
                'delta u3 (mm)' : delta_u3,
                'rotation r1 (rad)' : rotation_r1, 
                'rotation r2 (rad)': rotation_r2,
                'rotation r3(rad)' : rotation_r3}
    

    def joint_drifts (self) -> StoryDrifts : 
        """Reports the joint drifts 
        
        return: Joint Displacement analysis results 
        rtype: StoryDrifts 
        """
        number_results = int() 
        story = 
        name = 
        load_case =
        step_tyep = 
        step_number = 
        displacement_x = 
        displacement_y = 
        drfit_x = 
        drift_y = 


    def modal_load_participation_ratios(self) -> ModalLoadParticipationRatios : 
            """Reports the modal load participation ratios for each selected modal analysis case
            
            :return: Modal load participation ratios analysis results 
            :rtype: ModalLoadParticipationRatios
            """
            number_results = int ()
            load_case = [str()]
            item_type = [str()]
            item = [str()]
            stat = [float()]
            dyn = [float()]

            [ret, number_results, load_case, item_type, item, stat, dyn] = self.analysis_results.ModalLoadParticipationRatios(number_results, load_case, item_type, item, stat, dyn)

            #handle(ret)
            return {'number_results' : number_results, 
                    'load_case' : list(load_case),
                    'item_type' : list(item_type),
                    'item' : list(item),
                    'stat' : list(stat),
                    'dyn' : list(dyn)}


    def modal_participating_mass_ratios(self) -> ModalParticipatingMassRatios : 
            """Reports the modal participating mass ratios for each mode of each selected modal analysis case 
            
            :return: Modal participating mass ratios analysis results 
            :rtype: ModalParticipatingMassRatios
            """
            number_results = int() 
            load_case = [str()]
            step_type = [str()]
            step_number = [float()]
            period = [float()]
            delta_x = [float()]
            delta_y = [float()]
            delta_z = [float()]
            sum_delta_x = [float()]
            sum_delta_y = [float()]
            sum_delta_z = [float()]
            rotation_x = [float()]
            rotation_y = [float()]
            rotation_z = [float()]
            sum_rotation_x = [float()]
            sum_rotation_y = [float()]
            sum_rotation_z = [float()]

            [ret, number_results, load_case, step_type, step_number, period, 
            delta_x, delta_y, delta_z, sum_delta_x, sum_delta_y, sum_delta_z, 
            rotation_x, rotation_y, rotation_z, sum_rotation_x, sum_rotation_y, sum_rotation_z] = self.analysis_results.ModalParticipatingMassRatios(number_results, load_case, step_type, step_number, 
                                                                                                                                        period, delta_x, delta_y, delta_z, sum_delta_x, sum_delta_y, sum_delta_z, 
                                                                                                                                        rotation_x, rotation_y, rotation_z, sum_rotation_x, sum_rotation_y, sum_rotation_z)
            #handle(ret)
            return {'Number Results' : number_results,
                    'Load Case' : list(load_case),
                    'Step Type' : list(step_type),
                    'Step Number' : list(step_number),
                    'Period (sec)' : list(period),
                    'Delta x' : list(delta_x),
                    'Delta y' : list(delta_y),
                    'Delta z' : list(delta_z),
                    'Sum Delta x' : list(sum_delta_x),
                    'Sum Delta y' : list(sum_delta_y),
                    'Sum Delta z' : list(sum_delta_z),
                    'Rotation x' : list(rotation_x), 
                    'Rotation y' : list(rotation_y), 
                    'Rotation z' : list(rotation_z), 
                    'Sum Rotation x' : list(sum_rotation_x),
                    'Sum Rotation y' : list(sum_rotation_y),
                    'Sum Rotation z' : list(sum_rotation_z)}


    def modal_participation_factors(self) -> ModalParticipationFactors : 
            """Reports the modal participation factors for each mode of each selected modal analysis case 
            
            :return: Modal participation factors analysis results 
            :rtype: ModalParticipationFactors
            """
            number_results = int() 
            load_case = [str()]
            step_type = [str()]
            step_number = [float()]
            period = [float()]
            delta_x = [float()]
            delta_y = [float()]
            delta_z = [float()]
            rotation_x = [float()]
            rotation_y = [float()]
            rotation_z = [float()]
            modal_mass = [float()]
            modal_stiff = [float()]

            [ret, number_results, load_case, step_type, step_number, period, 
            delta_x, delta_y, delta_z, rotation_x, rotation_y, rotation_z, modal_mass, modal_stiff] = self.analysis_results.ModalParticipationFactors(number_results, load_case, step_type, step_number, period, 
                                                                                                                delta_x, delta_y, delta_z, rotation_x, rotation_y, rotation_z, modal_mass, modal_stiff)

            #handle(ret)
            return {'number_results' : number_results,
                    'load_case' : list(load_case),
                    'step_type' : list(step_type),
                    'step_num' : list(step_number),
                    'period' : list(period),
                    'ux' : list(delta_x),
                    'uy' : list(delta_y),
                    'uz' : list(delta_z),
                    'rx' : list(rotation_x), 
                    'ry' : list(rotation_y), 
                    'rz' : list(rotation_z), 
                    'modal_mass' : list(modal_mass),
                    'modal_stiff' : list(modal_stiff)}


    def modal_period(self) -> ModalPeriod:
            """Reports the modal period, cyclic frequency, circular frequency and eigenvalue for each selected modal load case.

            :return: Modal period analysis results
            :rtype: ModalPeriod
            """
            number_results = int()
            load_case = [str()]
            step_type = [str()]
            step_number = [int()]
            period = [float()]
            frequency = [float()]
            circular_frequency = [float()]
            eigen_value = [float()]
            
            [ret, number_results, load_case, step_type, step_number,
            period, frequency, circular_frequency, eigen_value] = self.analysis_results.ModalPeriod(number_results, load_case, step_type, step_number,
                                                                                                    period, frequency, circular_frequency, eigen_value)
            handle(ret)
            return {'Number Results': number_results,
                    'Load Case': list(load_case),
                    'Step Type': list(step_type),
                    'Step Number': list(step_number),
                    'Period (sec)': list(period),
                    'Frequency (cyc/sec)': list(frequency),
                    'Circular Frequency (rad/sec)': list(circular_frequency),
                    'Eigenvalue rad\u00b2/sec\u00b2': list(eigen_value)}


    def pier_force(self) -> PierForce :
            """Retrieves pier forces for any defined pier objects in the model.

            :return: Pier force analysis results
            :rtype: PierForce
            """
            number_results = int()
            story_name = [str()]
            pier_name = [str()]
            load_case = [str()]
            location = [str()]
            p = [float()]
            v2 = [float()]
            v3 = [float()]
            t = [float()]
            m2 = [float()]
            m3 = [float()]
            
            [ret, number_results, story_name, pier_name,
            load_case, location, p, v2, v3, t, m2, m3] = self.analysis_results.PierForce(number_results, story_name, pier_name,
                                                                                        load_case, location, p, v2, v3, t, m2, m3)
            # handle(ret)
            return {'number_results': number_results,
                    'story_name': list(story_name),
                    'pier_name': list(pier_name),
                    'load_case': list(load_case),
                    'location': list(location),
                    'p': list(p),
                    'v2': list(v2),
                    'v3': list(v2),
                    't': list(t),
                    'm2': list(m2),
                    'm3': list(m3)}


    def section_cut_analysis(self) -> SectionCutAnalysis : 
            """Reports the section cut force for sections cuts that are specified to have an analysis (Force1, Force2, Force3, Moment1, Moment2, Moment3) result type
            
            :return: section cut analysis results 
            :rtype: SectionCutAnalysis 
            """
            number_results = int()
            section_cut = [str()]
            load_case = [str()]
            step_type = [str()]
            step_number = [float()]
            force1 = [float()]
            force2 = [float()]
            force3 = [float()] 
            moment1 = [float()]
            moment2 = [float()]
            moment3 = [float()]

            [ret, number_results, section_cut, load_case, step_type, 
            step_number, force1, force2, force3, moment1, moment2, moment3] = self.analysis_results.SectionCutAnalysis(number_results, section_cut, load_case, step_type, step_number, 
                                                                                                                    force1, force2, force3, moment1, moment2, moment3)
            #handle(ret)
            return {'number_results' : number_results, 
                    'section_cut' : list(section_cut),
                    'load_case' : list(load_case),
                    'step_type' : list(step_type),
                    'step_num' : list(step_number),
                    'force1' : list(force1),
                    'force2' : list(force2),
                    'force3' : list(force3), 
                    'moment1' : list(moment1),
                    'moment2' : list(moment2), 
                    'moment3' : list(moment3)}

    def section_cut_design(self) -> SectionCutDesign : 
            """Report the section cut force for sections cuts that are specified to have a design 
            (axial force, shear force 2, shear force 3, torsion, moment 2, moment 3) result type 
            
            :return: Section cut design results 
            :rtype: SectionCutDesign
            """
            number_results = int()
            section_cut = [str()]
            load_case = [str()]
            step_type = [str()]
            step_number = [float()]
            axial = [float()]
            shear2 = [float()]
            shear3 = [float()]
            torsion = [float()]
            moment2 = [float()]
            moment3 = [float()]

            [ret, number_results, section_cut, 
            load_case, step_type, step_number, axial, 
            shear2, shear3, torsion, moment2, moment3] = self.analysis_results.SectionCutAnalysis(number_results, section_cut, load_case, 
                                                                                                    step_type, step_number, axial, shear2, 
                                                                                                    shear3, torsion, moment2, moment3)
            #handle(ret)
            return {'number_results' : number_results, 
                    'section_cut' : list(section_cut),
                    'load_case' : list(load_case),
                    'step_type' : list(step_type),
                    'step_num' : list(step_number),
                    'axial' : list(axial), 
                    'shear2' : list(shear2),
                    'shear3' : list(shear3),
                    'torsion' : list(torsion),
                    'moment2' : list(moment2), 
                    'moment3' : list(moment3)}


    def spandrel_force(self) -> SpandrelForce : 
            """Retrieves spandrel forces for any defined spandrel objects in the model
            
            :return: Spandrel force analysis results 
            :rtype: SpandrelForce
            """
            number_results = int()
            story_name = [str()]
            spandrel_name = [str()]
            load_case = [str()]
            location = [str()]
            axial = [float()]
            shear2 = [float()]
            shear3 = [float()]
            torsion = [float()]
            moment2 = [float()]
            moment3 = [float()]

            [ret, number_results, story_name, spandrel_name, load_case, 
            location, axial, shear2, shear3, torsion, moment2, moment3] = self.analysis_results.SpandrelForce(number_results, story_name, spandrel_name, load_case, 
                                                                                                            location, axial, shear2, shear3, torsion, moment2, moment3)
            #handle(ret)
            return {'number_results' : number_results,
                    'story_name' : list(story_name),
                    'spandrel_name' : list(spandrel_name),
                    'load_case' : list(load_case),
                    'location' : list(location),
                    'axial' : list(axial), 
                    'shear2' : list(shear2),
                    'shear3' : list(shear3),
                    'torsion' : list(torsion),
                    'moment2' : list(moment2), 
                    'moment3' : list(moment3)}

    def story_drifts(self) -> StoryDrift : 
            """Reports the story drifts 
            
            :return: Story drifts analysis results 
            :rtype: StoryDrift
            """
            number_results = int()
            story = [str()]
            load_case = [str()]
            step_type = [str()]
            step_number = [float()]
            direction = [str()]
            drift = [float()]
            label = [str()]
            x_direction = [float()]
            y_direction = [float()]
            z_direction = [float()]

            [ret, number_results, story, load_case, 
            step_type, step_number, direction, drift, 
            label, x_direction, y_direction, z_direction] = self.analysis_results.StoryDrifts(number_results, story, 
                                                                                                load_case, step_type, step_number, 
                                                                                                direction, drift, label, x_direction, 
                                                                                                y_direction, z_direction)
            #handle(ret)
            return{'number_results' : number_results,
                    'story' : list(story), 
                    'load_case' : list(load_case),
                    'step_type' : list(step_type),
                    'step_num' : list(step_number),
                    'direction' : list(direction),
                    'drift' : list(drift),
                    'label' : list(label),
                    'x_direction' : list(x_direction),
                    'y_direction' : list(y_direction),
                    'z_direction' : list(z_direction)}