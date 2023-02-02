# pyTABS - ETABS .NET API python wrapper
# Story - cStory interface 
__all__ = ['Story']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import typing
from typing import TypedDict, Union

class StoryInfo(TypedDict):
    """TypedDict class for Story information return"""
    base_elevation : float
    number_stories : int
    story_names : list[str]
    story_elevations : list[float]
    story_heights : list[float]
    is_master_story : list[bool]
    similar_to_story : list[str]
    splice_above : list[bool]
    splice_height : list[float]
    colour : list[int]


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
    
    
    def get_GUID(self, story_name : int) -> str:
        """Retrieves the GUID of a defined story.

        :param story_name: name of a defined story
        :type story_name: int
        :return: GUID of the story
        :rtype: str
        """
        guid = str()
        [ret, guid] = self.story.GetGUID(story_name, guid)
        handle(ret)
        return guid
    
    
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

    
    def get_stories(self) -> StoryInfo: 
        """Retrieves the story information for the current tower.

        :return: story information for all stories
        :rtype: StoryInfo
        """
        base_elevation = float()
        number_stories = int()
        story_names = [str()]
        story_elevations = [float()]
        story_heights = [float()]
        is_master_story = [bool()]
        similar_to_story = [str()]
        splice_above = [bool()]
        splice_height = [float()]
        colour = [int()]
        
        [ret, base_elevation, number_stories, story_names, 
         story_elevations, story_heights, is_master_story,
         similar_to_story, splice_above, splice_height, colour] = self.story.GetStories_2(base_elevation, number_stories, story_names, 
                                                                                          story_elevations, story_heights, is_master_story,
                                                                                          similar_to_story, splice_above, splice_height, colour)
        handle (ret)
        return {'base_elevation' : base_elevation,
                'number_stories' : number_stories,
                'story_names' : story_names,
                'story_elevations' : story_elevations,
                'story_heights' : story_heights,
                'is_master_story' : is_master_story,
                'similar_to_story' : similar_to_story,
                'splice_above' : splice_above,
                'splice_height' : splice_height,
                'colour': colour}
    
    
    def set_elevation(self, story_name : int, elevation : float) -> None: 
        """Sets the elevation of a defined story.
        
        :param story_name: name of a defined story 
        :type story_name: int
        :param elevation: elevation of the story 
        :type elevation: float 
        """
        handle(self.story.SetElevation(story_name, elevation))
    
    
    def set_GUID (self, story_name : str, guid : str = '') -> None: 
        """Sets the GUID of a defined story.

        :param story_name: name of a defined story
        :type story_name: str
        :param guid: GUID of the story, defaults to ''
        :type guid: str, optional
        """
        handle(self.story.SetGUID(story_name, guid))
    
    
    def set_height(self, story_name : int, height : float) -> None: 
        """Sets the height of a defined story.
        
        param story_name: name of a defined story 
        :type story_name: int
        :param height: height of the story
        :type height: float 
        """
        handle(self.story.SetHeight(story_name, height))
    
    
    def set_master_story(self, story_name : str, is_master_story : bool) -> None: 
        """Sets whether a defined story is a master story.
        
        param story_name: name of a defined story 
        :type story_name: str
        :param is_master_story: `True` if the story is a master story, `False` otherwise 
        :type is_master_story: bool 
        """
        handle(self.story.SetMasterStory(story_name, is_master_story))
    
    
    def set_similar(self, story_name : str, similar_to_story : str) -> None:
        """Sets the master story that a defined story should be similar to.
        
        :param story_name: name of a defined story which is not a master story
        :type story_name: str 
        :param similar_to_story: name of a defined master story that the requested story should be similar to 
        :type similar_to_story: str
        """
        handle (self.story.SetSimilarTo(story_name, similar_to_story))
    
    
    def set_splice(self, story_name : str, splice_above : bool, splice_height : float) -> None:
        """Sets the splice height of a defined story.
        
        :param story_name: name of defined story
        :type story_name: str
        :param splice_above: `True` if the story has a splice height, and `False` otherwise  
        :type splice_above: bool 
        :param splice_height: story splice height 
        :type splice_height: float 
        """
        handle(self.story.SetSplice(story_name, splice_above, splice_height))
        
        
    def set_stories(self, base_elevation : float, number_stories : int, story_names : list[str], story_heights : list[float],
                    is_master_story : list[bool], similar_to_story : list[str], splice_above : list[bool], splice_height : list[float], 
                    colour : list[int]) -> None: 
        """Sets the stories for the current tower.

        :param base_elevation: elevation of the base
        :type base_elevation: float
        :param number_stories: number of stories
        :type number_stories: int
        :param story_names: names of the stories
        :type story_names: list[str]
        :param story_heights: story heights
        :type story_heights: list[float]
        :param is_master_story: `True` if the story is master story, and `False` otherwise 
        :type is_master_story: list[bool]
        :param similar_to_story: if the story is not a master story, which master story the story is similar to 
        :type similar_to_story: list[str]
        :param splice_above: `True` if the story has a splice height, and `False` otherwise 
        :type splice_above: list[bool]
        :param splice_height: story splice height
        :type splice_height: list[float]
        :param colour: display color for the story specified
        :type colour: list[int]
        """
        [ret, ret_story_names, ret_story_heights, 
         ret_is_master_story, ret_similar_to_story, 
         ret_splice_above, ret_splice_height, ret_colour] = self.story.SetStories_2(base_elevation, number_stories, story_names,
                                                                                    story_heights, is_master_story, similar_to_story,
                                                                                    splice_above, splice_height, colour)
        handle(ret)