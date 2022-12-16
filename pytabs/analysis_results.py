# pyTABS - ETABS .NET API python wrapper
# AnalysisResults - cAnalysisResults interface 
__all__ = ['AnalysisResults']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *

# import typing
from typing import TypedDict


class PierForce(TypedDict):
    """TypedDict class for Pier force return"""
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