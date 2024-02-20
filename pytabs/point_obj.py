# pyTABS - ETABS .NET API python wrapper
# PointObj - cPointObj
__all__ = ['PointObj']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PointObj:
    """PointObj interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PointObj interface
        self.point_obj = etabs.cPointObj(sap_model.PointObj)
        
        # relate relevant ETABS enumerations
        self.eDiaphragmOption = etabs.eDiaphragmOption
        """EtabsModel `DiaphragmOption` enumeration"""
        

        # relate custom enumerations
        
        
        
    def get_name_from_label (self, label : str, story : str) -> str:
        """Retrieves the unique name of a point object, given the label and story level.

        :param label: The point object label 
        :type label: str
        :param story: The point object story level  
        :type label: str
        :return point_name: The unique name of the point object
        :rtype: str
        """

        point_name = str()
        [ret, point_name] = self.point_obj.GetNameFromLabel(label, story, point_name) 
        handle(ret)
        return point_name
    

    def get_name_list_on_story(self, story_name : str) -> list[str]:
        """Retrieves the names of the defined point objects on a given story.

        :param story_name: name of an existing story
        :type story_name: str
        :return: point object names on existing story
        :rtype: list[str]
        """
        
        number_names = int()
        point_names = [str()]
        [ret, number_names, point_names] = self.point_obj.GetNameListOnStory(story_name, number_names, point_names)
        handle(ret)
        return list(point_names)
    
    def get_coordinate_catesian(self, point_name, c_sys: str = "Global") -> list[float]:
        """Retrieves the x, y, and z coordinates of the specified point object in the present units
        
        :param point_name: unique name of an existing point object
        :type point_name: str
        :parap c_sys: coordinate system definition, 'Global' by default
        :type c_sys: str
        :return: catersian coordinate matrix [x, y, z] for the specified coordinate system in the present units
        :rtype: float
        """

        x = float()
        y = float()
        z = float()
   
        [ret, x, y, z] = self.point_obj.GetCoordCartesian(point_name, x, y, z, c_sys)
        handle(ret)
        return ([x, y, z])
    

    def get_uncoupled_point_spring(self, point_name: str) -> list[float]:
        """Retrieves the uncoupled spring stiffness 6x6 matrix of the defined point object.

        :param point_name: unique name of an existing point object
        :type point_name: str
        :return: point object spring stiffness matrix [U1, U2, U3, R1, R2, R3]
        :rtype: list[float]
        """

        point_springs = [float()]

        [ret, point_springs] = self.point_obj.GetSpring(point_name, point_springs)
        handle(ret)
        return list(point_springs)
    

    def get_spring_assignment(self, point_name: str) -> str:
        """Retrieves the point object spring assignment of the defined point object.

        :param point_name: unique name of an existing point object
        :type point_name: str
        :return: point object spring assignment
        :rtype: str
        """  
        point_spring_assign = str()

        [ret, point_spring_assign] = self.point_obj.GetSpringAssignment(point_name, point_spring_assign)
        handle(ret)
        return point_spring_assign
    
    def set_spring_assignment(self, point_name: str, point_spring_name: str, item_type: etabs.eItemType = etabs.eItemType.Objects) -> None:
        """Assigns an existing name point spring property to point objects.
        
        :param point_name: unique name of an existing point object
        :type point_name: str
        :param point_spring_name: name of an existing point spring property
        :typ point_spring_name: str
        :param item_type: one of eItemType enumeration (`Objects` : area object specified by name is added/removed from group, `Group` : all area objects in the group specified by name are added/removed from group, `SelectedObjects` : all selected area objects are added/removed from group, name is ignored), defaults to eItemType.Objects
        :type item_type: eItemType, optional
        """

        handle(self.point_obj.SetSpringAssignment(point_name, point_spring_name, item_type))

        return

