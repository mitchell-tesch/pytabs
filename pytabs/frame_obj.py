# pyTABS - ETABS .NET API python wrapper
# FrameObj - cFrameObj interface 
__all__ = ['FrameObj']

# import etabs namespace and error handler
from pytabs.etabs import *
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
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create FrameObj interface
        self.frame_obj = cFrameObj(self.sap_model.FrameObj)
        
        
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


    def set_group_assign(self, name : str, group_name : str, remove : bool = False, item_type: eItemType = eItemType.Objects) -> None:
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