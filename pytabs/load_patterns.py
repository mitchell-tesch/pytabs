# pyTABS - ETABS .NET API python wrapper
# LoadPatterns- cLoadPatterns interface 
__all__ = ['LoadPatterns']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *


class LoadPatterns:
    """LoadPatterns interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create LoadPatterns interface
        self.load_patterns = etabs.cLoadPatterns(sap_model.LoadPatterns)


    def add(self, load_pattern_name : str, load_pattern_type : etabs.eLoadPatternType, self_weight_multiplier : float = 0, add_analysis_case : bool = True):
        """Adds a new load pattern.

        :param load_pattern_name: name for the new load pattern
        :type load_pattern_name: str
        :param load_pattern_type: one of the items in the eLoadPatternType enumeration
        :type load_pattern_type: eLoadPatternType
        :param self_weight_multiplier: self weight multiplier for the new load pattern, defaults to 0
        :type self_weight_multiplier: float, optional
        :param add_analysis_case: if `True`, a linear static load case corresponding to the new load pattern is added, defaults to `True`
        :type add_analysis_case: bool, optional
        """
        handle(self.load_patterns.Add(load_pattern_name, load_pattern_type, self_weight_multiplier, add_analysis_case))


    #TODO Add ChangeName method


    def count(self) -> int:
        """Retrieves the number of defined load patterns.

        :return: number of defined load patterns
        :rtype: int
        """
        return self.load_patterns.Count()


    #TODO Add Delete method
    #TODO GetAutoSeismicCode method
    #TODO GetAutoWindCode method


    def get_type(self, load_pattern_name : str) -> etabs.eLoadPatternType:
        """Retrieves the load type for a specified load pattern.

        :param load_pattern_name: name of an existing load pattern
        :type load_pattern_name: str
        :return: one of the items in the eLoadPatternType enumeration
        :rtype: eLoadPatternType
        """
        load_pattern_type = etabs.eLoadPatternType.ActiveEarthPressure
        [ret, load_pattern_type] = self.load_patterns.GetLoadType(load_pattern_name, load_pattern_type)
        handle(ret)
        return load_pattern_type


    def get_name_list(self) -> list[str]:
        """Retrieves the names of all defined load cases.

        :return: list of load pattern names
        :rtype: list[str]
        """
        number_names = int()
        load_pattern_names = [str()]
        [ret, number_names, load_pattern_names] = self.load_patterns.GetNameList(number_names, load_pattern_names)
        handle(ret)
        return list(load_pattern_names)


    def get_self_weight_multiplier(self, load_pattern_name : str) -> float:
        """Retrieves the self weight multiplier for a specified load pattern.

        :param load_pattern_name: name of an existing load pattern
        :type load_pattern_name: str
        :return: self weight multiplier for the specified load pattern
        :rtype: float
        """
        self_weight_multiplier = float()
        [ret, self_weight_multiplier] = self.load_patterns.GetSelfWTMultiplier(load_pattern_name, self_weight_multiplier)
        handle(ret)
        return self_weight_multiplier


    def set_load_type(self, load_pattern_name : str, load_pattern_type : etabs.eLoadPatternType) -> None:
        """Assigns a load type to a load pattern.

        :param load_pattern_name: name of an existing load pattern
        :type load_pattern_name: str
        :param load_pattern_type: one of the items in the `eLoadPatternType` enumeration
        :type load_pattern_type: eLoadPatternType
        """
        handle(self.load_patterns.SetLoadType(load_pattern_name, load_pattern_type))


    def set_self_weight_multiplier(self, load_pattern_name : str, self_weight_multiplier : float) -> None:
        """Assigns a self weight multiplier to a load case.

        :param load_pattern_name: name of an existing load pattern
        :type load_pattern_name: str
        :param self_weight_multiplier: self weight multiplier for the specified load pattern 
        :type self_weight_multiplier: float
        """
        handle(self.load_patterns.SetSelfWTMultiplier(load_pattern_name, self_weight_multiplier))