# pyTABS - ETABS .NET API python wrapper
# Frame - cFrameObj interface 
__all__ = ['Frame']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *

# import typing
from typing import Union

class Frame:
    """Frame interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PierLabel interface
        self.frame = cFrameObj(self.sap_model.FrameObj)
        
        
    def get_name_list_on_story(self, story_name : str) -> list(str()):
        """Retrieves the elevation of a defined story.

        :param story_name: name of a defined story
        :type story_name: str
        :return: All Frame Labels
        :rtype: list(str)
        """
        number_name = int()
        frame_names = [str()]
        [ret, number_name, frame_names] = self.frame.GetNameListOnStory(story_name, number_name, frame_names)
        
        handle(ret)
        return list(frame_names)

    def get_frame(self, frame_name: str) -> bool: #figure out how to add multiple inputs. Ask Mitch Later. 
        """Checks whether the specified Frame Label exists.

        :param frame_name: frame name to check
        :type pier_name: str
        :return: True if the frame Label exists, False otherwise
        :rtype: bool
        """
        ret = self.frame.GetAllFrames(MyName= frame_name)
        if ret == 0:
            return True
        return False

    def set_group(self, frame_name : str, group_name : str, remove : bool = False, item_type: eItemType = eItemType.Objects ) -> None:
        """_summary_

        :param frame_name: _description_
        :type frame_name: str
        :param group_name: _description_
        :type group_name: str
        :param remove: _description_, defaults to False
        :type remove: bool, optional
        :param item_type: _description_, defaults to eItemType.Objects
        :type item_type: eItemType, optional
        """
        ret = self.frame.SetGroupAssign(frame_name, group_name, remove, item_type)
        handle(ret)
