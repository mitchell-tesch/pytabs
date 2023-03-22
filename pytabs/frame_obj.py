# pyTABS - ETABS .NET API python wrapper
# FrameObj - cFrameObj interface 
__all__ = ['FrameObj']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import typing
from typing import TypedDict

class FrameObjectLabelData(TypedDict):
    """TypedDict class for Frame object label data return"""
    frame_name : str
    frame_label : str
    frame_story : str

class FrameObj:
    """FrameObj interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create FrameObj interface
        self.frame_obj = etabs.cFrameObj(self.sap_model.FrameObj)

    def add_by_coord(self, xi_coordinate : float, yi_coordinate : float, zi_coordinate : float, xj_coordinate : float, yj_coordinate : float, zj_coordinate : float, propname : str = "Default", username : str =  " ", csys : str = "Global" ) -> str:
        """Adds a new frame object whose end points are at the specific coordinates.
        :param xi_coordinate: the X coordinates of the I-End of the added frame object 
                                in the coordinate system defined by the csys item
        :type xi_coordinate: float
        :param yi_coordinate: the Y coordinates of the I-End of the added frame object 
                                in the coordinate system defined by the csys item
        :type yi_coordinate: float
        :param zi_coordinate: the Z coordinates of the I-End of the added frame object 
                                in the coordinate system defined by the csys item
        :type zi_coordinate: float
        :param xj_coordinate: the X coordinates of the J-End of the added frame object 
                                in the coordinate system defined by the csys item
        :type xj_coordinate: float
        :param yj_coordinate: the Y coordinates of the J-End of the added frame object 
                                in the coordinate system defined by the csys item
        :type yj_coordinate: float
        :param zj_coordinate: the Z coordinates of the J-End of the added frame object 
                                in the coordinate system defined by the csys item
        :type zj_coordinate: float
        :param propname: if `Default` the program assigns a default section property to the frame object, if `None` no section property
                        is assigned to the frame object, if it is the name of a defined frame section property,that property is assigned 
                        to the frame object
        :type propname: str, optional
        :param username: if a username is specified and that name is already used for another frame,cable or tendon object
                        the program ignores the username, if no username is specified the program assigns a default name to the frame object
        :type username: str,optional
        :param csys: the name of the coordinate system in which the frame object end point coordinates are defined
        :type csys: str, optional
        :return: the name that the program ultimately assigns for the frame object
        :rtype: str
        """
        frame_name = str()
        [ret, frame_name] = self.frame_obj.AddByCoord(xi_coordinate, yi_coordinate, zi_coordinate, xj_coordinate, yj_coordinate, zj_coordinate, frame_name, propname, username, csys)
        handle(ret)
        return frame_name

    def add_by_point(self, point_i : str, point_j : str, propname : str = "Default", username : str =  " ") -> str:
        """Adds a new frame object whose end points are specified by name. 
        :param point_i: the name of a defined point object at the I-End of the added frame object
        :type point_i: str
        param point_j: the name of a defined point object at the J-End of the added frame object
        :type point_j: str
        :param propname: if `Default` the program assigns a default section property to the frame object, if `None` no section property
                            is assigned to the frame object, if it is the name of a defined frame section property,that property is assigned 
                            to the frame object
        :type propname: str, optional
        :param username: if a username is specified and that name is already used for another frame,cable or tendon object
                            the program ignores the username, if no username is specified the program assigns a default name to the frame object
        :type username: str,optional
        :return: the name that the program ultimately assigns for the frame object
        :rtype: str
        """
        frame_name = str()
        [ret, frame_name] = self.frame_obj.AddByPoint(point_i, point_j, frame_name, propname, username )
        handle(ret)
        return frame_name

    def get_label_from_name(self, frame_name : str) -> FrameObjectLabelData:
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

    def get_name_list_on_story(self, story_name : str) -> list[str]:
        """Retrieves the names of the defined frame objects on a given story.

        :param story_name: name of an existing story
        :type story_name: str
        :return: frame object names on existing story
        :rtype: list[str]
        """
        number_names = int()
        frame_names = [str()]
        [ret, number_names, frame_names] = self.frame_obj.GetNameListOnStory(story_name, number_names, frame_names)
        handle(ret)
        return list(frame_names)

    def get_group_assign(self, frame_name : str) -> list[str]:
            """Retrieves the groups to which a frame object is assigned.
            :param frame_name: name of the frame object
            :type frame_name: str
            :return: group names of assigned frame object
            :rtype: list[str]
            """
            group_number_names = int()
            group_names = str()
            [ret, group_number_names, group_names] = self.frame_obj.GetGroupAssign(frame_name, group_number_names, group_names)
            handle(ret)
            return list(group_names)

    def get_GUID(self, frame_name : str) -> str:
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
        
    def get_design_procedure(self, frame_name : str) -> str:
            """Retrieves the design procedure for a frame object.
            :param frame_name: name of the frame object
            :type frame_name: str
            :return: number indicating the design procdure type of the specified frame object
            :rtype: int
            """
            procedure_type_desc = {0: 'Program determined', 1: 'Steel Frame Design',
                                           2: 'Concrete Frame Design', 3: 'Composite Beam Design',
                                           4: 'Steel Joist Design', 7:'No Design', 13: 'Composite Column Design'}
            procedure_type = int()
            [ret, procedure_type] = self.frame_obj.GetDesignProcedure(frame_name, procedure_type)
            handle(ret)
            return procedure_type_desc[procedure_type]

    def set_group_assign(self, name : str, group_name : str, remove : bool = False, item_type: etabs.eItemType = etabs.eItemType.Objects) -> None:
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
        