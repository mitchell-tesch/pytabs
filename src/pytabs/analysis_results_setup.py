# PyTABS - ETABS .NET API python wrapper
# AnalysisResultsSetup - cAnalysisResultsSetup interface
__all__ = ['AnalysisResultsSetup']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations
from .enumerations import (eResultsSetupStepOutOption, eResultsSetupComboOutOption)


class AnalysisResultsSetup:
    """AnalysisResultsSetup interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create AnalysisResultsSetup interface
        self.analysis_results_setup = etabs.cAnalysisResultsSetup(sap_model.Results.Setup)

        # relate custom enumerations
        self.eResultsSetupStepOutOption = eResultsSetupStepOutOption
        self.eResultsSetupComboOutOption = eResultsSetupComboOutOption

    # Analysis Results Setup Methods
    def deselect_all_cases_combos_for_output(self) -> None:
        """Deselects all load cases and response combinations for output."""
        handle(self.analysis_results_setup.DeselectAllCasesAndCombosForOutput())

    def get_case_selected_for_output(self, case_name: str) -> bool:
        """Checks if a load case is selected for output.

        :param case_name: name of an existing load case
        :type case_name: str
        :return: `True` if the Case selected for output, `False` otherwise
        :rtype: bool
        """
        [ret, selected] = self.analysis_results_setup.GetCaseSelectedForOutput(case_name)
        handle(ret)
        return selected

    def get_combo_selected_for_output(self, combo_name: str) -> bool:
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
        return gx, gy, gz

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
        return start_buckling_mode, end_buckling_mode, all_buckling_modes

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
        [ret, start_mode, end_mode, all_modes] = self.analysis_results_setup.GetOptionModeShape(start_mode, end_mode,
                                                                                                all_modes)
        handle(ret)
        return all_modes, start_mode, end_mode

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

    def set_case_selected_for_output(self, case_name: str, select_state: bool = True) -> None:
        """Sets a load case selected for output flag.

        :param case_name: name of existing load case
        :type case_name: str
        :param select_state: select case for output, defaults to `True`
        :type select_state: bool, optional
        """
        handle(self.analysis_results_setup.SetCaseSelectedForOutput(case_name, select_state))

    def set_combo_selected_for_output(self, combo_name: str, select_state: bool = True) -> None:
        """Sets a combination selected for output flag.

        :param combo_name: name of the existing combination
        :type combo_name: str
        :param select_state: select combination for output defaults to `True`
        :type select_state: bool, optional
        """
        handle(self.analysis_results_setup.SetComboSelectedForOutput(combo_name, select_state))

    def set_base_reaction_location(self, point: tuple[float, float, float]) -> None:
        """Sets the global coordinates of the location at which the base reactions are reported.

        :param point: global coordinate of 3d point where base reactions are to be reported (gx, gy, gz)
        :type point: tuple[float, float, float]
        """
        handle(self.analysis_results_setup.SetOptionBaseReactLoc(point[0], point[1], point[2]))

    def set_buckling_mode_setup(self, start_buckling_mode: int, end_buckling_mode: int,
                                all_buckling_modes: bool = False) -> None:
        """Sets the buckling mode range for output. 
        
        :param start_buckling_mode: first buckling mode number 
        :type start_buckling_mode: int
        :param end_buckling_mode: last buckling mode number 
        :type start_buckling_mode: int
        :param all_buckling_modes: all buckling modes, defaults to `False` 
        :type start_buckling_mode: bool, optional 
        """
        handle(self.analysis_results_setup.SetOptionBucklingMode(start_buckling_mode, end_buckling_mode,
                                                                 all_buckling_modes))

    def set_direct_history_setup(self, option: eResultsSetupStepOutOption) -> None:
        """Sets the direct history results option.
        
        :param option: one of step out options (envelopes, step-by-step or last-step)
        :type option:  eResultsSetupStepOutOption
        """
        handle(self.analysis_results_setup.SetOptionDirectHist(option.value))

    def set_modal_history_setup(self, option: eResultsSetupStepOutOption) -> None:
        """Sets the modal history results option.
        
        :param option: one of step out options (envelopes, step-by-step or last-step)
        :type option:  eResultsSetupStepOutOption
        """
        handle(self.analysis_results_setup.SetOptionModalHist(option.value))

    def set_mode_shape_setup(self, start_mode: int, end_mode: int, all_modes: bool = False) -> None:
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

    def set_combination_setup(self, option: eResultsSetupComboOutOption) -> None:
        """Sets the non-linear static results option.
        
        :param option: one of combo options (envelopes or multiple)
        :type option: eResultsSetupComboOutOption
        """
        handle(self.analysis_results_setup.SetOptionMultiValuedCombo(option.value))

    def set_nonlinear_setup(self, option: eResultsSetupStepOutOption) -> None:
        """Sets the non-linear static results option.
        
        :param option: one of step out options (envelopes, step-by-step or last-step)
        :type option: eResultsSetupStepOutOption
        """
        handle(self.analysis_results_setup.SetOptionNLStatic(option.value))
