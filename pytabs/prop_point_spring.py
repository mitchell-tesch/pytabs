# pyTABS - ETABS .NET API python wrapper
# PropPointSpring - cPropPointSpring
__all__ = ['PropPointSpring']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PropPointSpring:
    """PropPointSpring interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropPointSpring interface
        self.prop_point_spring = etabs.cPropPointSpring(sap_model.PropPointSpring)
        
        # relate custom enumerations


    def get_names_list (self) -> list[str]:
        """Retrieves the names of all existing defined point spring properties.

        :return point_spring_names: list of point spring names
        :rtype: list(str)
        """

        number_names = int()
        point_spring_names = [str()]
        [ret, number_names, point_spring_names] = self.prop_point_spring.GetNameList(number_names, point_spring_names) 
        handle(ret)
        return list(point_spring_names)
    
    def get_point_spring_prop (self, point_spring_name: str, spring_option: int) -> list[float]:
        """Retrieves the point spring property of an existing named point spring.

        :param point_spring_name: name of an existing point spring property
        :type point_spring_name: str
        :param spring_option: spring stiffness option, 1. User Specified/Link Properties, 2. Based on Soil Profile and Footing Dimensions
        :type spring_option: int
        :return point_springs: point object spring stiffness matrix [U1, U2, U3, R1, R2, R3]
        :rtype: list[float]
        """
        point_springs = [float()]
        c_sys = str()
        soil_profile = str()
        footing = str()
        period = float()
        color = int()
        notes = str()
        iGUID = str()

        [ret, spring_option, point_springs, c_sys, 
            soil_profile, footing, period, color, notes, iGUID] = self.prop_point_spring.GetPointSpringProp(point_spring_name, spring_option, point_springs, 
                                                                                                        c_sys, soil_profile, footing, period, color, notes, iGUID)
        handle(ret)
        return list(point_springs)
    
    def set_point_spring_prop(self, point_spring_name: str, point_springs: list[float], spring_option: int) -> list[float]:
        """Creates a new named point spring property, or modifies an existig named point spring property

        :param point_spring_name: name of the new spring property to be defined or an existing point spring property to re-define
        :type point_spring_name: str
        :param spring_option: spring stiffness option, 1. User Specified/Link Properties, 2. Based on Soil Profile and Footing Dimensions
        :type spring_option: int
        :param point_springs: point spring stiffness matrix [U1, U2, U3, R1, R2, R3]
        :type: list[float]
        :return: point spring stiffness matrix [U1, U2, U3, R1, R2, R3]
        :rtype: list[float]
        """


        c_sys = str()
        soil_profile = str()
        footing = str()
        period = float()
        color = int()
        notes = str()
        iGUID = str()

        [ret, point_springs] = self.prop_point_spring.SetPointSpringProp(point_spring_name, spring_option, point_springs, c_sys, soil_profile, footing, period, color, notes, iGUID)
                                                          
        handle(ret)
        return list(point_springs)
    
PropPointSpring.set_point_spring_prop