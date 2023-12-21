# pyTABS - ETABS .NET API python wrapper
# SpandrelLabel - cSpandrelLabel
__all__ = ['SpandrelLabel']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing

from typing import TypedDict

class GetNameList(TypedDict): 
    """Retrieves the names of all defined Spandrel Labels"""
    number_names : int 
    spandrel_label : list[str]
    is_multi_story : list[bool]

class SectionProperties(TypedDict):
    """Retrieves the section properties of the specified spandrel"""
    spandrel_name : str
    number_stories : int
    story_name :list[str]
    number_area_object : list[int]
    number_line_object : list[int]
    spandrel_length : list[float]
    spandrel_depth_left : list[float]
    spandrel_thickness_left : list[float]
    spandrel_depth_right : list[float]
    spandrel_thickness_right : list[float]
    pier_material_property : list[str]
    center_gravity_left_x : list[float]
    center_gravity_left_y : list[float]
    center_gravity_left_z : list[float]
    center_gravity_right_x : list[float]
    center_gravity_right_y : list[float]
    center_gravity_right_z : list[float]


class SpandrelLabel:
    """SpandrelLabel interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create SpandrelLabel interface
        self.spandrel_label = etabs.cSpandrelLabel(sap_model.SpandrelLabel)
        
        # relate custom enumerations

    def change_name(self, spandrel_label : str, new_spandrel_label : str) -> None: 
        """Changes the name of a defined Spandrel Label 
        
        :param spandrel_label: the existing name of a defined Spandrel 
        :type spandrel_label: str 
        :param new_spandrel_label: the new name for the Spandrel Label 
        :type new_spandrel_label: str 
        """
        handle(self.spandrel_label.ChangeName(spandrel_label, new_spandrel_label))
    
    def delete_method(self, spandrel_label : str) -> None: 
        """Deletes the specified Spandrel Label 
        
        :param spandrel_label: the name of an existing Spandrel Label 
        :type spandrel_label: str 
        """

        handle(self.spandrel_label.Delete(spandrel_label))

    def get_name_list(self) -> GetNameList : 
        """Retrieves the names of all defined Spandrel Labels 
        
        :return: all story names and if spans multiple stories 
        :rtype: GetNameList
        """
        [ret, number_names, spandrel_label, is_multi_story] = self.spandrel_label.GetNameList(number_names, spandrel_label, is_multi_story)

        handle (ret)
        return{'number_names' : number_names, 
                'spandrel_label' : spandrel_label, 
                'is_multi_story' : is_multi_story}

    def get_section_properties (self, spandrel_name : str) -> SectionProperties: 
        """Retrieves the section properties for a specified spandrel 
        
        :param spandrel_name: name of an existing spandrel 
        :type spandrel_name: str 
        :return: section properties for the specified spandrel 
        :type SectionProperties 
        """
        spandrel_name = str()
        number_stories = int() 
        story_name = [str()]
        number_area_object = [int()]
        number_line_object = [int()]
        spandrel_length = [float()]
        spandrel_depth_left = [float()]
        spandrel_thickness_left = [float()]
        spandrel_depth_right = [float()]
        spandrel_thickness_right = [float()]
        pier_material_property = [str()]
        center_gravity_left_x = [float()]
        center_gravity_left_y = [float()]
        center_gravity_left_z = [float()]
        center_gravity_right_x = [float()]
        center_gravity_right_y = [float()]
        center_gravity_right_z = [float()]

        [ret, spandrel_name, number_stories, story_name, number_area_object, 
        number_line_object, spandrel_length, spandrel_depth_left, spandrel_thickness_left, 
        spandrel_depth_right, spandrel_thickness_right, pier_material_property, 
        center_gravity_left_x, center_gravity_left_y, center_gravity_left_z, 
        center_gravity_right_x, 
        center_gravity_right_y, center_gravity_right_z] = self.spandrel_label.GetSectionProperties(spandrel_name, number_stories, story_name, number_area_object, 
                                                                                                    number_line_object, spandrel_length, spandrel_depth_left, spandrel_thickness_left, 
                                                                                                    spandrel_depth_right, spandrel_thickness_right, pier_material_property, 
                                                                                                    center_gravity_left_x, center_gravity_left_y, center_gravity_left_z, 
                                                                                                    center_gravity_right_x, center_gravity_right_y, center_gravity_right_z)
        handle(ret)
        return{'spandrel_name': spandrel_name, 
                'number_stories' : number_stories, 
                'story_name' : list(story_name), 
                'number_area_object': list(number_area_object), 
                'number_line_object' : list(number_line_object), 
                'spandrel_length':list(spandrel_length), 
                'spandrel_depth_left' :list(spandrel_depth_left), 
                'spandrel_thickness_left' : list(spandrel_thickness_left), 
                'spandrel_depth_right' : list(spandrel_depth_right), 
                'spandrel_thickness_right' : list(spandrel_thickness_right), 
                'pier_material_property' : list(pier_material_property), 
                'center_gravity_left_x' : list(center_gravity_left_x), 
                'center_gravity_left_y' : list(center_gravity_left_y), 
                'center_gravity_left_z' : list(center_gravity_left_z), 
                'center_gravity_right_x' : list(center_gravity_right_x), 
                'center_gravity_right_y' : list(center_gravity_right_y), 
                'center_gravity_right_z' : list(center_gravity_right_z)}
        

    def get_spandrel(self, spandrel_name : str) -> bool: 
        """Retrieves the specified Spandrel Label 
        
        :param spandrel_name: the name of an existing Spandrel Label 
        :type spandrel_name: str 
        :return multiple_story: whether the Spandrel Label spans multiple story levels 
        :rtype multiple_story: bool
        """
        
        multiple_story = bool()

        [ret, multiple_story] = self.spandrel_label.GetSpandrel(spandrel_name, multiple_story)

        handle(ret)
        return multiple_story

    
    def set_spandrel (self, spandrel_name : str, multiple_story : bool) -> None: 
        """Adds a new Spandrel Label or modifies and existing Spandrel Label 
        
        :param spandrel_name: name of the spandrel. If it is the name of an existing spandrel label, the spandrel is modified otherwise a new spandrel label is added
        :type spandrel_name: str 
        :param multiple_story: whether the Spandrel Label spans multiple story levels 
        :type multiple_story: bool 
        """
        handle(self.spandrel_label.SetSpandrel(spandrel_name, multiple_story))
