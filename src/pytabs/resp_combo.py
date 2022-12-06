# pyTABS - ETABS .NET API python wrapper
# RespCombo - cCombo interface 
__all__ = ['RespCombo']

# import typing
from typing import Union
# import pyTABS error handler
from pytabs.error_handle import *
# import ETABS API .dll
from ETABSv1 import *


class RespCombo:
    """Combo interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        """substantiates the cCombo interface

        Args:
            sap_model (cSapModel): SapModel from EtabsModel
        """
        # link of SapModel interface
        self.sap_model = sap_model
        # create RespCombo interface
        self.resp_combo = cCombo(sap_model.RespCombo)


    def get_name_list(self) -> list[str]:
        """Retrieves the names of all defined response combinations. 

        Returns:
            list[str]: List of combination names.
        """
        number_names = 0
        combo_names = ['']
        [ret, number_names, combo_names] = self.resp_combo.GetNameList(number_names, combo_names)
        handle(ret)
        return list(combo_names)