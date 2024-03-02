# PyTABS - ETABS .NET API python wrapper
# PierLabel - cPierLabel interface 
__all__ = ['PierLabel']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import typing
from typing import TypedDict


class PierSectionProperties(TypedDict):
    """TypedDict class for Pier section properties return"""
    pier_name: str
    number_stories: int
    story_name: list[str]
    axis_angle: list[float]
    num_area_objs: list[int]
    num_line_objs: list[int]
    width_bot: list[float]
    thickness_bot: list[float]
    width_top: list[float]
    thickness_top: list[float]
    mat_prop: list[str]
    cg_bot_x: list[float]
    cg_bot_y: list[float]
    cg_bot_z: list[float]
    cg_top_x: list[float]
    cg_top_y: list[float]
    cg_top_z: list[float]


class PierLabel:
    """PierLabel interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PierLabel interface
        self.pier_label = etabs.cPierLabel(self.sap_model.PierLabel)

    def change_name(self, pier_name: str, new_pier_name: str) -> None:
        """Changes the name of a defined Pier Label.

        :param pier_name: name of defined pier to change
        :type pier_name: str
        :param new_pier_name: new name of pier
        :type new_pier_name: str
        """
        handle(self.pier_label.ChangeName(pier_name, new_pier_name))

    def delete(self, pier_name: str) -> None:
        """Deletes the specified Pier Label.

        :param pier_name: name of defined pier to delete
        :type pier_name: str
        """
        handle(self.pier_label.Delete(pier_name))

    def get_names_list(self) -> list[str]:
        """Retrieves the names of all defined Pier Labels.

        :return: All Pier Labels
        :rtype: list[str]
        """
        _number_names = int()
        pier_names = [str()]
        [ret, _number_names, pier_names] = self.pier_label.GetNameList(_number_names, pier_names)
        handle(ret)
        return list(pier_names)

    def get_pier(self, pier_name: str) -> bool:
        """Checks whether the specified Pier Label exists.

        :param pier_name: pier name to check
        :type pier_name: str
        :return: True if the Pier Label exists, False otherwise
        :rtype: bool
        """
        ret = self.pier_label.GetPier(pier_name)
        if ret == 0:
            return True
        return False

    def get_section_properties(self, pier_name: str) -> PierSectionProperties:
        """Retrieves the section properties for a specified pier.

        :param pier_name: Pier name for which to retrieve section properties
        :type pier_name: str
        :return: section properties of requested Pier
        :rtype: PierSectionProperties
        """
        number_stories = int()
        story_name = [str()]
        axis_angle = [float()]
        num_area_objs = [int()]
        num_line_objs = [int()]
        width_bot = [float()]
        thickness_bot = [float()]
        width_top = [float()]
        thickness_top = [float()]
        mat_prop = [str()]
        cg_bot_x = [float()]
        cg_bot_y = [float()]
        cg_bot_z = [float()]
        cg_top_x = [float()]
        cg_top_y = [float()]
        cg_top_z = [float()]
        [ret, number_stories, story_name, axis_angle,
         num_area_objs, num_line_objs, width_bot,
         thickness_bot, width_top, thickness_top,
         mat_prop, cg_bot_x, cg_bot_y, cg_bot_z,
         cg_top_x, cg_top_y, cg_top_z] = self.pier_label.GetSectionProperties(pier_name, number_stories, story_name,
                                                                              axis_angle, num_area_objs, num_line_objs,
                                                                              width_bot, thickness_bot, width_top,
                                                                              thickness_top, mat_prop, cg_bot_x,
                                                                              cg_bot_y,
                                                                              cg_bot_z, cg_top_x, cg_top_y, cg_top_z)
        handle(ret)
        return {'pier_name': pier_name,
                'number_stories': number_stories,
                'story_name': list(story_name),
                'axis_angle': list(axis_angle),
                'num_area_objs': list(num_area_objs),
                'num_line_objs': list(num_line_objs),
                'width_bot': list(width_bot),
                'thickness_bot': list(thickness_bot),
                'width_top': list(width_top),
                'thickness_top': list(thickness_top),
                'mat_prop': list(mat_prop),
                'cg_bot_x': list(cg_bot_x),
                'cg_bot_y': list(cg_bot_y),
                'cg_bot_z': list(cg_bot_z),
                'cg_top_x': list(cg_top_x),
                'cg_top_y': list(cg_top_y),
                'cg_top_z': list(cg_top_z)}

    def set_pier(self, pier_name: str) -> None:
        """Adds a new Pier Label. 

        :param pier_name: name of new pier label
        :type pier_name: str
        """
        handle(self.pier_label.SetPier(pier_name))
