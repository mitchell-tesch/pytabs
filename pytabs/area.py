# pyTABS - ETABS .NET API python wrapper
# Area - cAreaObj interface 
__all__ = ['Area']

# import etabs namespace and error handler
from turtle import st
from pytabs.etabs import *
from pytabs.error_handle import *

# import typing
from typing import Union

class Area:
    """Area interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PierLabel interface
        self.area = cAreaObj(self.sap_model.AreaObj)

    def get_name_list_on_story(self, story_name: str) -> list(str()):
        """_summary_

        :param self: _description_
        :type self: _type_
        :return: _description_
        :rtype: _type_
        """
        number_name = int()
        area_name = [str()]

        [ret, number_name, area_name] = self.area.GetNameListOnStory(story_name, number_name, area_name)
        handle(ret)

        return list(area_name)

    def get_label_from_name(self, name : str) -> str():
        label = str()
        story = str()

        [ret, label, story] = self.area.GetLabelFromName(name, label, story)
        handle(ret)

        return label

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
        ret = self.area.SetGroupAssign(frame_name, group_name, remove, item_type)
        handle(ret)
