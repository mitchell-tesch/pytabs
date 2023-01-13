# pyTABS - ETABS .NET API python wrapper
# Group - cGroup interface 
__all__ = ['Group']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *

# import typing
from typing import Union

class Group:
    """Group interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PierLabel interface
        self.group = cGroup(self.sap_model.GroupDef)        
        

    def set_group_1(self, name :str, color: int = -1, specified_selection : bool =  True,
                    specified_section_cut_def : bool =  True,
                    specified_steel_design : bool =  True,
                    specified_concrete_design : bool =  True,
                    specified_aluminum_design : bool =  True,
                    specified_static_nla_active: bool =  True,
                    specified_auto_seismic_output : bool =  False,
                    specified_auto_wind_output : bool =  False,
                    specified_mass_weight : bool =  True,
                    specified_steeljoist_design : bool =  True,
                    specified_wall_design : bool =  True,
                    specified_baseplate_design : bool =  True,
                    specified_connection_desgin : bool =  True) -> None:
        """
        :param name: This is the name of a group. If this is the name of an existing group, that group is modified, otherwise a new group is added.
        :type name: str
        :param color: The display color for the group specified as a Integer. If this value is input as –1, the program automatically selects a display color for the group.
        :type color: int, optional
        :param specified_selection: defaults to True
        :type specified_selection: bool, optional
        :param specified_section_cut_def: defaults to True
        :type specified_section_cut_def: bool, optional
        :param specified_steel_design: defaults to True
        :type specified_steel_design: bool, optional
        :param specified_concrete_design: defaults to True
        :type specified_concrete_design: bool, optional
        :param specified_aluminum_design: defaults to True
        :type specified_aluminum_design: bool, optional
        :param specified_static_nla_active: defaults to True
        :type specified_static_nla_active: bool, optional
        :param specified_auto_seismic_output: defaults to False
        :type specified_auto_seismic_output: bool, optional
        :param specified_auto_wind_output: defaults to False
        :type specified_auto_wind_output: bool, optional
        :param specified_mass_weight: defaults to True
        :type specified_mass_weight: bool, optional
        :param specified_steeljoist_design: defaults to True
        :type specified_steeljoist_design: bool, optional
        :param specified_wall_design: defaults to True
        :type specified_wall_design: bool, optional
        :param specified_baseplate_design: defaults to True
        :type specified_baseplate_design: bool, optional
        :param specified_connection_desgin: defaults to True
        :type specified_connection_desgin: bool, optional
        """
        ret = self.group.SetGroup_1(name, color, specified_selection,specified_section_cut_def, specified_steel_design,
                                    specified_concrete_design, specified_aluminum_design, specified_static_nla_active,
                                    specified_auto_seismic_output,specified_auto_wind_output, specified_mass_weight, 
                                    specified_steeljoist_design, specified_wall_design, specified_baseplate_design,
                                    specified_connection_desgin)
        handle(ret)
