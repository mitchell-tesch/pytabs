# PyTABS - ETABS .NET API python wrapper
# AreaObj - cAreaObj interface 
__all__ = ['AreaObj']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import typing
from typing import TypedDict


class AreaObjectLabelData(TypedDict):
    """TypedDict class for Area object label data return"""
    area_name: str
    area_label: str
    area_story: str


class AreaObj:
    """AreaObj interface"""
    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create AreaObj interface
        self.area_obj = etabs.cAreaObj(self.sap_model.AreaObj)
        
        # relate relevant ETABS enumerations
        self.eWallPierRebarLayerType = etabs.eWallPierRebarLayerType
        """EtabsModel `WallPierRebarLayerType` enumeration"""
        self.eWallSpandrelRebarLayerType = etabs.eWallSpandrelRebarLayerType
        """EtabsModel `WallSpandrelRebarLayerType` enumeration"""

    def get_label_from_name(self, area_name: str) -> AreaObjectLabelData:
        """Retrieves the label and story for a unique area object name.

        :param area_name: name of the area object
        :type area_name: str
        :return: label and story of area object name
        :rtype: `AreaObjectLabelData`
        """
        area_label = str()
        area_story = str()
        [ret, area_label, area_story] = self.area_obj.GetLabelFromName(area_name, area_label, area_story)
        handle(ret)
        return {'area_name': area_name,
                'area_label': area_label,
                'area_story': area_story}

    def get_name_list_on_story(self, story_name: str) -> list[str]:
        """Retrieves the names of the defined area objects on a given story.

        :param story_name: name of an existing story
        :type story_name: str
        :return: area object names on existing story
        :rtype: list[str]
        """
        _number_names = int()
        area_names = [str()]
        [ret, _number_names, area_names] = self.area_obj.GetNameListOnStory(story_name, _number_names, area_names)
        handle(ret)
        return list(area_names)

    def get_property(self, area_name: str) -> str:
        """Retrieves the name of the area property assigned to an area object.
        
        :param area_name: name of an existing area object
        :type area_name: str
        :return: name of the area property assigned to the area object
        :rtype: str
        """
        prop_name = str()
        [ret, prop_name] = self.area_obj.GetProperty(area_name, prop_name)
        handle(ret)
        return prop_name

    def set_group_assign(self, name: str, group_name: str, remove: bool = False,
                         item_type: etabs.eItemType = etabs.eItemType.Objects) -> None:
        """Adds or removes area objects from a specified group.

        :param name: name of an existing area object or group depending on the value of item_type 
        :type name: str
        :param group_name: name of an existing group to which the assignment is made 
        :type group_name: str
        :param remove: `True` for add, False for remove, defaults to `False`
        :type remove: bool, optional
        :param item_type: one of eItemType enumeration (`Objects` : area object specified by name is added/removed from group, `Group` : all area objects in the group specified by name are added/removed from group, `SelectedObjects` : all selected area objects are added/removed from group, name is ignored), defaults to eItemType.Objects
        :type item_type: eItemType, optional
        """
        handle(self.area_obj.SetGroupAssign(name, group_name, remove, item_type))

    def get_spring_assignment(self, area_name: str) -> str:
        """Retrieves the area object area spring assignment of the defined frame object.

        :param area_name: unique name of an existing area object
        :type area_name: str
        :return: area object area spring assignment
        :rtype: str
        """  
        spring_prop = str()
        [ret, spring_prop] = self.area_obj.GetSpringAssignment(area_name, spring_prop)
        handle(ret)
        return spring_prop

    def set_spring_assignment(self, area_name: str, area_spring_prop: str,
                              item_type: etabs.eItemType = etabs.eItemType.Objects) -> None:
        """Assigns an existing area spring property to area objects of the value item_type.
        
        :param area_name: unique name of an existing area object
        :type area_name: str
        :param area_spring_prop: name of an existing area spring property
        :type area_spring_prop: str
        :param item_type: one of eItemType enumeration (`Objects` : area object specified by name is added/removed from group, `Group` : all area objects in the group specified by name are added/removed from group, `SelectedObjects` : all selected area objects are added/removed from group, name is ignored), defaults to eItemType.Objects
        :type item_type: eItemType, optional
        """
        handle(self.area_obj.SetSpringAssignment(area_name, area_spring_prop, item_type))
