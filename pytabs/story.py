# pyTABS - ETABS .NET API python wrapper
# Story - cStory interface 
__all__ = ['Story']

# import pyTABS error handler
from pytabs.error_handle import *
# import ETABS API .dll
from ETABSv1 import *


class Story:
    """Story interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        """Substantiates the cStory interface.

        Args:
            sap_model (cSapModel): SapModel from EtabsModel.
        """
        # link of SapModel interface
        self.sap_model = sap_model
        # create PierLabel interface
        self.story = cStory(self.sap_model.Story)
        
        
    def get_elevation(self, story_name : str) -> float:
        """Retrieves the elevation of a defined story. 

        Args:
            story_name (str): The name of a defined story.

        Returns:
            float: The elevation of the story. 
        """
        elevation = float()
        [ret, elevation] = self.story.GetElevation(story_name, elevation)
        handle(ret)
        return elevation
    
    
    def get_height(self, story_name : str) -> float:
        """Retrieves the height of a defined story.

        Args:
            story_name (str): The name of a defined story.

        Returns:
            float: The height of the story.
        """
        height = float()
        [ret, height] = self.story.GetHeight(story_name, height)
        handle(ret)
        return height
    
    
    def get_master_story(self, story_name : str) -> bool:
        """Retrieves whether a defined story is a master story.

        Args:
            story_name (str): The name of a defined story.
            
        Returns:
            bool: True if the story is a master story, False otherwise. 
        """
        is_master_story = bool()
        [ret, is_master_story] = self.story.GetMasterStory(story_name, is_master_story)
        handle(ret)
        return is_master_story
    
    
    def get_name_list(self) -> list[str]:
        """Retrieves the names of all defined stories.

        Returns:
            list[str]:  All story names
        """
        number_names = int()
        story_names = ['']
        [ret, number_names, story_names] = self.story.GetNameList(number_names, story_names)
        handle(ret)
        return list(story_names)