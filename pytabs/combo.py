# pyTABS - ETABS .NET API python wrapper
# Combo - cCombo
__all__ = ['Combo']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing
from typing import TypedDict

class CaseList(TypedDict):
    """TypedDict class for case list return"""
    number_items : int
    cname_types : list[etabs.eCNameType]
    cnames : list[str]
    mode_numbers : list[int]
    scaling_factors : list[float]


class Combo:
    """Combo interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for static nonlinear staged load cases
        self.combo = etabs.cCombo(sap_model.RespCombo)
        # relate etabs enumerations
        self.eCNameType = etabs.eCNameType
        
        # relate custom enumerations


    def get_case_list(self, name : str) -> CaseList:
        """Retrieves all load cases and response combinations included in the load combination specified by the Name item.

        :param name: The name of an existing load combination.
        :type name: str
        :return: Load cases and response combinations included
        :rtype: CaseList
        """
        number_items = int()
        cname_types = [etabs.eCNameType.LoadCase]
        cnames = [str()]
        mode_numbers = [int()]
        scaling_factors = [float()]
        [ret, number_items, cname_types,
         cnames, mode_numbers, scaling_factors] = self.combo.GetCaseList_1(name, number_items, cname_types,
                                                                           cnames, mode_numbers, scaling_factors)
        handle(ret)
        return {'number_items': number_items,
                'cname_types': list(cname_types),
                'cnames': list(cnames),
                'mode_numbers': list(mode_numbers),
                'scaling_factors': list(scaling_factors)}