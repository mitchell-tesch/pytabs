# pyTABS - ETABS .NET API python wrapper
# RespCombo - cCombo interface 
__all__ = ['RespCombo']

# import pyTABS error handler
from pytabs.error_handle import handle
# import ETABS API .dll
from ETABSv1 import *


class RespCombo:
    """Combo interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create RespCombo interface
        self.resp_combo = cCombo(sap_model.RespCombo)


    def get_name_list(self) -> list[str]:
        """Retrieves the names of all defined response combinations.

        :return: list of combination names
        :rtype: list[str]
        """
        number_names = int()
        combo_names = [str()]
        [ret, number_names, combo_names] = self.resp_combo.GetNameList(number_names, combo_names)
        handle(ret)
        return list(combo_names)