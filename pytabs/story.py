# pyTABS - ETABS .NET API python wrapper
# Story - cStory interface 
__all__ = ['Story']

# import etabs namespace and error handler
from pytabs.etabs import *
from pytabs.error_handle import *

# import typing
from typing import Union


class Story:
    """Story interface"""
    def __init__(self, sap_model : cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PierLabel interface
        self.story = cStory(self.sap_model.Story)
        
        
    def get_elevation(self, story_name : str) -> float:
        """Retrieves the elevation of a defined story.

        :param story_name: name of a defined story
        :type story_name: str
        :return: elevation of the story
        :rtype: float
        """
        elevation = float()
        [ret, elevation] = self.story.GetElevation(story_name, elevation)
        handle(ret)
        return elevation
    
    
    def get_height(self, story_name : str) -> float:
        """Retrieves the height of a defined story.

        :param story_name: name of a defined story
        :type story_name: str
        :return: height of the story
        :rtype: float
        """
        height = float()
        [ret, height] = self.story.GetHeight(story_name, height)
        handle(ret)
        return height
    
    
    def get_master_story(self, story_name : str) -> bool:
        """Retrieves whether a defined story is a master story.

        :param story_name: name of a defined story
        :type story_name: str
        :return: True if the story is a master story, False otherwise
        :rtype: bool
        """
        is_master_story = bool()
        [ret, is_master_story] = self.story.GetMasterStory(story_name, is_master_story)
        handle(ret)
        return is_master_story
    
    
    def get_name_list(self) -> list[str]:
        """Retrieves the names of all defined stories.

        :return: all story names
        :rtype: list[str]
        """
        number_names = int()
        story_names = ['']
        [ret, number_names, story_names] = self.story.GetNameList(number_names, story_names)
        handle(ret)
        return list(story_names)
    
    
    def get_similar_to(self, story_name : str) -> Union[str, None]:
        """Retrieves whether a defined story is a master story.

        :param story_name: name of a defined story
        :type story_name: str
        :return: name of similar story, if story is master returns None
        :rtype: Union[str, None]
        """
        is_master = bool()
        similar_story = str()
        [ret, is_master, similar_story] = self.story.GetSimilarTo(story_name, is_master, similar_story)
        handle(ret)
        if not is_master:
            return similar_story
    
    
    def get_splice(self, story_name : str) -> Union[float, None]:
        """Retrieves the story splice height, if applicable.

        :param story_name: name of a defined story
        :type story_name: str
        :return: height of splice, if present otherwise None
        :rtype: Union[float, None]
        """
        splice_above = bool()
        splice_height = float()
        [ret, splice_above, splice_height] = self.story.GetSplice(story_name, splice_above, splice_height)
        handle(ret)
        if splice_above:
            return splice_height