# pyTABS - ETABS .NET API python wrapper
# Group - cGroup interface 
__all__ = ['Group']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import typing


class Group:
    """Group interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create Group interface
        self.group = etabs.cGroup(self.sap_model.GroupDef)        
        

    def set_group_1(self,
                    group_name : str,
                    group_color : int = -1,
                    specified_selection : bool = True,
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
                    specified_connection_design : bool =  True) -> None:
        """Sets the group data.

        :param group_name: name of group
        :type group_name: str
        :param group_color: display color of group, defaults to -1 (auto)
        :type group_color: int, optional
        :param specified_selection: `True` if the group is specified to be used for selection; otherwise `False`, defaults to `True`
        :type specified_selection: bool, optional
        :param specified_section_cut_def: `True` if the group is specified to be used for defining section cuts; otherwise `False`, defaults to `True`
        :type specified_section_cut_def: bool, optional
        :param specified_steel_design: `True` if the group is specified to be used for defining steel frame design groups; otherwise `False`, defaults to `True`
        :type specified_steel_design: bool, optional
        :param specified_concrete_design: `True` if the group is specified to be used for defining concrete frame design groups; otherwise `False`, defaults to `True`
        :type specified_concrete_design: bool, optional
        :param specified_aluminum_design: `True` if the group is specified to be used for defining aluminum frame design groups; otherwise `False`, defaults to `True`
        :type specified_aluminum_design: bool, optional
        :param specified_static_nla_active: `True` if the group is specified to be used for defining stages for nonlinear static analysis; otherwise `False`, defaults to `True`
        :type specified_static_nla_active: bool, optional
        :param specified_auto_seismic_output: `True` if the group is specified to be used for reporting auto seismic loads; otherwise `False`, defaults to `False`
        :type specified_auto_seismic_output: bool, optional
        :param specified_auto_wind_output: `True` if the group is specified to be used for reporting auto wind loads; otherwise `False`, defaults to `False`
        :type specified_auto_wind_output: bool, optional
        :param specified_mass_weight: `True` if the group is specified to be used for reporting group masses and weight; otherwise `False`, defaults to `True`
        :type specified_mass_weight: bool, optional
        :param specified_steeljoist_design: `True` if the group is specified to be used for defining steel joist design groups; otherwise `False`, defaults to `True`
        :type specified_steeljoist_design: bool, optional
        :param specified_wall_design: `True` if the group is specified to be used for defining wall design groups; otherwise `False`, defaults to `True`
        :type specified_wall_design: bool, optional
        :param specified_baseplate_design: `True` if the group is specified to be used for defining base plate design groups; otherwise `False`, defaults to `True`
        :type specified_baseplate_design: bool, optional
        :param specified_connection_design: `True` if the group is specified to be used for defining connection design groups; otherwise `False`, defaults to `True`
        :type specified_connection_design: bool, optional
        """
        handle(self.group.SetGroup_1(group_name,
                                     group_color,
                                     specified_selection,
                                     specified_section_cut_def,
                                     specified_steel_design,
                                     specified_concrete_design,
                                     specified_aluminum_design,
                                     specified_static_nla_active,
                                     specified_auto_seismic_output,
                                     specified_auto_wind_output,
                                     specified_mass_weight, 
                                     specified_steeljoist_design,
                                     specified_wall_design,
                                     specified_baseplate_design,
                                     specified_connection_design))
