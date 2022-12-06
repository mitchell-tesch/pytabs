# pyTABS - ETABS .NET API python wrapper
# AnalysisResults - cAnalysisResults interface 
__all__ = ['AnalysisResults']

# import typing
from typing import TypedDict
# import pyTABS error handler
from pytabs.error_handle import *
# import ETABS API .dll
from ETABSv1 import *


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
        """substantiates the cAnalysisResults interface

        Args:
            sap_model (cSapModel): SapModel from EtabsModel
        """
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
        
        Args:
            case_name (str): The name of an existing load case

        Returns:
            bool: selected for output?
        """
        [ret, selected] = self.analysis_results_setup.GetCaseSelectedForOutput(case_name)
        return selected


    def get_combo_selected_for_output(self, combo_name : str) -> bool:
        """Checks if a load combination is selected for output.
        
        Args:
            combo_name (str): The name of an existing load combination

        Returns:
            bool: selected for output?
        """
        [ret, selected] = self.analysis_results_setup.GetComboSelectedForOutput(combo_name)
        return selected


    def set_case_selected_for_output(self, case_name : str, select_state : bool = True) -> None:
        """Sets a load case selected for output flag.

        Args:
            case_name (str): name of existing load case
            select_state (bool, optional): selected for output?. Defaults to True.
        """
        handle(self.analysis_results_setup.SetCaseSelectedForOutput(case_name, select_state))
    
    
    def set_combo_selected_for_output(self, combo_name : str, select_state : bool = True) -> None:
        """Sets a load combo selected for output flag.

        Args:
            combo_name (str): name of existing load combination
            select_state (bool, optional): selected for output?. Defaults to True.
        """
        handle(self.analysis_results_setup.SetComboSelectedForOutput(combo_name, select_state))


    def pier_force(self) -> PierForce:
        """Retrieves pier forces for any defined pier objects in the model.

        Args:
            number_results (int): The total number of results returned by the program 

        Returns:
            PierForce: TypedDictionary of pier analysis results
        """
        number_results = 0
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