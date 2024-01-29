# pyTABS - ETABS .NET API python wrapper
# SpandrelLabel - cSpandrelLabel
__all__ = ['SpandrelLabel']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import typing
from typing import TypedDict, Union

class SpandrelNameList(TypedDict):
    """TypedDict class for Spandrel name list return"""
    number_names : int
    spandrel_names : list[str]
    is_multi_story : list[bool]

class SectionProperties(TypedDict):
    """TypedDict class for Spandrel section properties return"""
    spandrel_name : str
    number_stories : int
    story_name : list[str]
    num_area_obj : list[int]
    num_line_obj : list[int]
    length : list[float]
    depth_left : list[float]
    thickness_left : list[float]
    depth_right : list[float]
    thickness_right : list[float]
    mat_prop : list[str]
    cg_left_x : list[float]
    cg_left_y : list[float]
    cg_left_z : list[float]
    cg_right_x : list[float]
    cg_right_y : list[float]
    cg_right_z : list[float]


class SpandrelLabel:
    """SpandrelLabel interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create SpandrelLabel interface
        self.spandrel_label = etabs.cSpandrelLabel(sap_model.SpandrelLabel)


    def change_name(self, spandrel_label : str, new_spandrel_label : str) -> None:
        """Changes the name of a defined Spandrel Label 
        
        :param spandrel_label: the existing name of a defined Spandrel 
        :type spandrel_label: str 
        :param new_spandrel_label: the new name for the Spandrel Label 
        :type new_spandrel_label: str 
        """
        handle(self.spandrel_label.ChangeName(spandrel_label, new_spandrel_label))


    def delete(self, spandrel_label : str) -> None:
        """Deletes the specified Spandrel Label 
        
        :param spandrel_label: the name of an existing Spandrel Label 
        :type spandrel_label: str 
        """
        handle(self.spandrel_label.Delete(spandrel_label))


    def get_name_list(self) -> SpandrelNameList:
        """Retrieves the names of all defined Spandrel Labels 
        
        :return: all story names and if spans multiple stories 
        :rtype: SpandrelNameList
        """
        number_names = int()
        spandrel_name = [str()]
        is_multi_story = [bool()]
        [ret, number_names,
         spandrel_name, is_multi_story] = self.spandrel_label.GetNameList(number_names,
                                                                          spandrel_name,
                                                                          is_multi_story)
        handle(ret)
        return {'number_names' : number_names,
                'spandrel_name ' : spandrel_name,
                'is_multi_story' : is_multi_story}


    def get_section_properties (self, spandrel_name : str) -> SectionProperties:
        """Retrieves the section properties for a specified spandrel 
        
        :param spandrel_name: name of an existing spandrel 
        :type spandrel_name: str 
        :return: section properties for the specified spandrel 
        :type SectionProperties 
        """
        number_stories = int()
        story_name = [str()]
        num_area_obj = [int()]
        num_line_obj = [int()]
        length = [float()]
        depth_left = [float()]
        thickness_left = [float()]
        depth_right = [float()]
        thickness_right = [float()]
        mat_prop = [str()]
        cg_left_x = [float()]
        cg_left_y = [float()]
        cg_left_z = [float()]
        cg_right_x = [float()]
        cg_right_y = [float()]
        cg_right_z = [float()]
        
        [ret, number_stories, story_name,
         num_area_obj, num_line_obj,
         length, depth_left, thickness_left,
         depth_right, thickness_right, mat_prop,
         cg_left_x, cg_left_y, cg_left_z,
         cg_right_x, cg_right_y, cg_right_z] = self.spandrel_label.GetSectionProperties(spandrel_name, number_stories, story_name,
                                                                                        num_area_obj, num_line_obj,
                                                                                        length, depth_left, thickness_left,
                                                                                        depth_right, thickness_right, mat_prop,
                                                                                        cg_left_x, cg_left_y, cg_left_z,
                                                                                        cg_right_x, cg_right_y, cg_right_z)
        handle(ret)
        return {'spandrel_name': spandrel_name,
                'number_stories': number_stories,
                'story_name': list(story_name),
                'num_area_obj': list(num_area_obj),
                'num_line_obj': list(num_line_obj),
                'length': list(length),
                'depth_left': list(depth_left),
                'thickness_left': list(thickness_left),
                'depth_right': list(depth_right),
                'thickness_right': list(thickness_right),
                'mat_prop': list(mat_prop),
                'cg_left_x': list(cg_left_x),
                'cg_left_y': list(cg_left_y),
                'cg_left_z': list(cg_left_z),
                'cg_right_x': list(cg_right_x),
                'cg_right_y': list(cg_right_y),
                'cg_right_z': list(cg_right_z)}


    def get_spandrel(self, spandrel_name : str) -> Union[None, dict]:
        """Retrieves the specified Spandrel Label

        :param spandrel_name: name of an existing spandrel
        :type spandrel_name: str
        :return: If spandrel exists, dict with Spandrel name and whether it is multi-story, else None
        :rtype: Union[None, dict]
        """
        is_multi_story = bool()
        [ret, is_multi_story] = self.spandrel_label.GetSpandrel(spandrel_name, is_multi_story)
        if ret == 0:
            return {'spandrel_name': spandrel_name,
                    'is_multi_story': is_multi_story}


    def set_spandrel (self, spandrel_name : str, is_multi_story : bool) -> None:
        """Adds a new Spandrel Label or modifies and existing Spandrel Label

        :param spandrel_name: name of the spandrel, if existing spandrel label is modified
        :type spandrel_name: str
        :param is_multi_story: whether the Spandrel Label spans multiple story levels 
        :type is_multi_story: bool
        """
        handle(self.spandrel_label.SetSpandrel(spandrel_name, is_multi_story))
