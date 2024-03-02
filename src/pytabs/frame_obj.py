# PyTABS - ETABS .NET API python wrapper
# FrameObj - cFrameObj interface 
__all__ = ['FrameObj']

# import ETABS namespace and pyTABS error handler
from .etabs_config import *
from .error_handle import *

# import pyTABS custom enumerations
from .enumerations import eFrameDesignProcedure

# import typing
from typing import TypedDict


class FrameObjectLabelData(TypedDict):
    """TypedDict class for Frame object label data return"""
    frame_name: str
    frame_label: str
    frame_story: str


class FrameObj:
    """FrameObj interface"""
    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create FrameObj interface
        self.frame_obj = etabs.cFrameObj(self.sap_model.FrameObj)
        
        # relate relevant ETABS enumerations
        self.eHingeLocationType = etabs.eHingeLocationType
        """EtabsModel `HingeLocationType` enumeration"""

    def add_by_coord(self, xi_coordinate: float, yi_coordinate: float, zi_coordinate: float,
                     xj_coordinate: float, yj_coordinate: float, zj_coordinate: float,
                     prop_name: str = "Default", user_name: str = "", coordinate_sys: str = "Global") -> str:
        """Adds a new frame object whose end points are at the specific coordinates.
        
        :param xi_coordinate: the X coordinates of the I-End of the added frame object in the coordinate system defined by the coordinate_sys item
        :type xi_coordinate: float
        :param yi_coordinate: the Y coordinates of the I-End of the added frame object in the coordinate system defined by the coordinate_sys item
        :type yi_coordinate: float
        :param zi_coordinate: the Z coordinates of the I-End of the added frame object in the coordinate system defined by the coordinate_sys item
        :type zi_coordinate: float
        :param xj_coordinate: the X coordinates of the J-End of the added frame object in the coordinate system defined by the coordinate_sys item
        :type xj_coordinate: float
        :param yj_coordinate: the Y coordinates of the J-End of the added frame object in the coordinate system defined by the coordinate_sys item
        :type yj_coordinate: float
        :param zj_coordinate: the Z coordinates of the J-End of the added frame object in the coordinate system defined by the coordinate_sys item
        :type zj_coordinate: float
        :param prop_name: if `Default` ETABS assigns a default section property to the frame object, if `None` no section property is assigned to the frame object, otherwise use the name of a defined frame section property
        :type prop_name: str, optional
        :param user_name: if a user_name is specified and that name is already used for another frame, cable or tendon object the program ignores the username, if no username is specified the program assigns a default name to the frame object
        :type user_name: str, optional
        :param coordinate_sys: the name of the coordinate system in which the frame object end point coordinates are defined
        :type coordinate_sys: str, optional
        :return: the name ETABS ultimately assigns for the frame object
        :rtype: str
        """
        frame_name = str()
        [ret, frame_name] = self.frame_obj.AddByCoord(xi_coordinate, yi_coordinate, zi_coordinate,
                                                      xj_coordinate, yj_coordinate, zj_coordinate,
                                                      frame_name, prop_name, user_name, coordinate_sys)
        handle(ret)
        return str(frame_name)

    def add_by_point(self, point_i: str, point_j: str, prop_name: str = "Default", user_name: str = "") -> str:
        """Adds a new frame object whose end points are specified by name. 
        :param point_i: the name of a defined point object at the I-End of the added frame object
        :type point_i: str
        param point_j: the name of a defined point object at the J-End of the added frame object
        :type point_j: str
        :param prop_name: if `Default` ETABS assigns a default section property to the frame object, if `None` no section property is assigned to the frame object, otherwise use the name of a defined frame section property
        :type prop_name: str, optional
        :param user_name: if a user_name is specified and that name is already used for another frame, cable or tendon object the program ignores the username, if no username is specified the program assigns a default name to the frame object
        :type user_name: str,optional
        :return: the name ETABS ultimately assigns for the frame object
        :rtype: str
        """
        frame_name = str()
        [ret, frame_name] = self.frame_obj.AddByPoint(point_i, point_j, frame_name, prop_name, user_name)
        handle(ret)
        return str(frame_name)

    def get_design_orientation(self, frame_name: str) -> etabs.eFrameDesignOrientation:
        """Retrieves the design orientation for a frame object.

        :param frame_name: name of the frame object
        :type frame_name: str
        :return: A value from the eFrameDesignOrientation enumeration
        :rtype: etabs.eFrameDesignOrientation
        """
        design_orientation = etabs.eFrameDesignOrientation.Null
        [ret, design_orientation] = self.frame_obj.GetDesignOrientation(frame_name, design_orientation)
        handle(ret)
        return design_orientation

    def get_design_procedure(self, frame_name: str) -> eFrameDesignProcedure:
        """Retrieves the design procedure for a frame object.

        :param frame_name: name of the frame object
        :type frame_name: str
        :return: A value from the eFrameDesignProcedure enumeration
        :rtype: eFrameDesignProcedure
        """
        procedure_type = int()
        [ret, procedure_type] = self.frame_obj.GetDesignProcedure(frame_name, procedure_type)
        handle(ret)
        return eFrameDesignProcedure(procedure_type)

    def get_group_assign(self, name: str) -> list[str]:
        """Retrieves the groups to which a frame object is assigned.

        :param name: name of an existing frame object
        :type name: str
        :return: names of the groups to which the frame object is assigned
        :rtype: list[str]
        """
        _number_groups = int()
        groups = [str()]
        [ret, _number_groups, groups] = self.frame_obj.GetGroupAssign(name, _number_groups, groups)
        handle(ret)
        return list(groups)

    def get_guid(self, frame_name: str) -> str:
        """Retrieves the GUID(Global Unique ID) for the specified frame object.
        
        :param frame_name: name of the frame object
        :type frame_name: str
        :return: the GUID of the specified frame object
        :rtype: str
        """
        guid = str()
        [ret, guid] = self.frame_obj.GetGUID(frame_name, guid)
        handle(ret)
        return guid

    def get_label_from_name(self, frame_name: str) -> FrameObjectLabelData:
        """Retrieves the label and story for a unique frame object name.
        :param frame_name: name of the frame object
        :type frame_name: str
        :return: label and story of frame object name
        :rtype: `FrameObjectLabelData`
        """
        frame_label = str()
        frame_story = str()
        [ret, frame_label, frame_story] = self.frame_obj.GetLabelFromName(frame_name, frame_label, frame_story)
        handle(ret)
        return {'frame_name': frame_name,
                'frame_label': frame_label,
                'frame_story': frame_story}

    # TODO def get_modifiers(self, name : str)

    def get_name_list(self) -> list[str]:
        """Retrieves the names of all defined frame objects.

        :return: frame object names
        :rtype: list[str]
        """
        _number_names = int()
        frame_names = [str()]
        [ret, _number_names, frame_names] = self.frame_obj.GetNameList(_number_names, frame_names)
        handle(ret)
        return list(frame_names)

    def get_name_list_on_story(self, story_name: str) -> list[str]:
        """Retrieves the names of the defined frame objects on a given story.

        :param story_name: name of an existing story
        :type story_name: str
        :return: frame object names on existing story
        :rtype: list[str]
        """
        _number_names = int()
        frame_names = [str()]
        [ret, _number_names, frame_names] = self.frame_obj.GetNameListOnStory(story_name, _number_names, frame_names)
        handle(ret)
        return list(frame_names)
    
    def get_spring_assignment(self, frame_name: str) -> str:
        """Retrieves the frame object line spring assignment of the defined frame object.

        :param frame_name: unique name of an existing frame object
        :type frame_name: str
        :return: frame object line spring assignment
        :rtype: str
        """  
        spring_prop = str()
        [ret, spring_prop] = self.frame_obj.GetSpringAssignment(frame_name, spring_prop)
        handle(ret)
        return spring_prop

    def set_group_assign(self, name: str, group_name: str, remove: bool = False,
                         item_type: etabs.eItemType = etabs.eItemType.Objects) -> None:
        """Adds or removes frame objects from a specified group.

        :param name: name of an existing frame object or group depending on the value of item_type
        :type name: str
        :param group_name: name of an existing group to which the assignment is made
        :type group_name: str
        :param remove: `True` for add, False for remove, defaults to `False`
        :type remove: bool, optional
        :param item_type: one of eItemType enumeration (`Objects` : frame object specified by name is added/removed from group, `Group` : all frame objects in the group specified by name are added/removed from group, `SelectedObjects` : all selected frame objects are added/removed from group, name is ignored), defaults to `eItemType.Objects`
        :type item_type: eItemType, optional
        """
        handle(self.frame_obj.SetGroupAssign(name, group_name, remove, item_type))

    def set_spring_assignment(self, frame_name: str, line_spring_prop: str,
                              item_type: etabs.eItemType = etabs.eItemType.Objects) -> None:
        """Assigns an existing line spring property to frame objects of the value item_type.
        
        :param frame_name: unique name of an existing frame object
        :type frame_name: str
        :param line_spring_prop: name of an existing line spring property
        :type line_spring_prop: str
        :param item_type: one of eItemType enumeration (`Objects` : area object specified by name is added/removed from group, `Group` : all area objects in the group specified by name are added/removed from group, `SelectedObjects` : all selected area objects are added/removed from group, name is ignored), defaults to eItemType.Objects
        :type item_type: eItemType, optional
        """
        handle(self.frame_obj.SetSpringAssignment(frame_name, line_spring_prop, item_type))
