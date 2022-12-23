# pyTABS - ETABS .NET API python wrapper
# AnalysisResults - cAnalysisResults interface 
__all__ = ['AnalysisResults']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *

# import typing
from typing import TypedDict

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



class AnalysisResults:
    """AnalysisResults interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create AnalysisResultsSetup interface
        self.analysis_results_setup = cAnalysisResultsSetup(sap_model.Results.Setup)
        # create AnalysisResults interface
        self.analysis_results = cAnalysisResults(sap_model.Results)


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
    
    
    def get_combination_setup(self) -> str:
        """Retrieves the combination option setup.

        :return: 'envelope' or 'multiple' (if possible)
        :rtype: str
        """
        option_dict = {1: 'envelopes', 2: 'multiple'}
        option = int()
        [ret, option] = self.analysis_results_setup.GetOptionMultiValuedCombo(option)
        handle(ret)
        return option_dict[option]
    
    
    def get_nonlinear_setup(self) -> str:
        """Retrieves the non-linear static results option.

        :return: 'envelopes', 'step-by-step' or 'last-step'
        :rtype: str
        """
        option_dict = {1: 'envelopes', 2: 'step-by-step', 3: 'last-step'}
        option = int()
        [ret, option] = self.analysis_results_setup.GetOptionNLStatic(option)
        handle(ret)
        return option_dict[option]
    
    
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


    def set_combination_setup(self, option : str) -> None:
        """Sets the non-linear static results option.
        
        :param option: 'envelope' or 'multiple' (if possible)
        :type option: str
        """
        option_dict = {'envelopes': 1, 'multiple': 2}
        option_int = option_dict[option]
        handle(self.analysis_results_setup.SetOptionMultiValuedCombo(option_int))


    def set_nonlinear_setup(self, option : str) -> None:
        """Sets the non-linear static results option.
        
        :param option: 'envelopes', 'step-by-step' or 'last-step'
        :type option: str
        """
        option_dict = {'envelopes': 1, 'step-by-step': 2, 'last-step': 3}
        option_int = option_dict[option]
        handle(self.analysis_results_setup.SetOptionNLStatic(option_int))


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
        # handle(ret)
        return {'number_results': number_results,
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'period': list(period),
                'frequency': list(frequency),
                'circular_frequency': list(circular_frequency),
                'eigen_value': list(eigen_value)}


    def pier_force(self) -> PierForce:
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