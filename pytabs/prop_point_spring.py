# PyTABS - ETABS .NET API python wrapper
# PropPointSpring - cPropPointSpring interface
__all__ = ['PropPointSpring']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations
from pytabs.enumerations import ePointSpringStiffnessOption

# import typing
from typing import TypedDict


class PointSpringProperties(TypedDict):
    """TypedDict class for point spring properties return"""
    point_spring_name: str
    spring_option: ePointSpringStiffnessOption
    stiffness: list[float]
    coord_sys: str
    soil_profile: str
    footing: str
    period: float
    colour: int
    notes: str
    guid: str


class PropPointSpring:
    """PropPointSpring interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropPointSpring interface
        self.prop_point_spring = etabs.cPropPointSpring(sap_model.PropPointSpring)

        # relate custom enumerations
        self.ePointSpringStiffnessOption = ePointSpringStiffnessOption

    def get_names_list(self) -> list[str]:
        """Retrieves the names of all existing defined point spring properties.

        :return point_spring_names: list of point spring names
        :rtype: list(str)
        """
        _number_names = int()
        point_spring_names = [str()]
        [ret, _number_names, point_spring_names] = self.prop_point_spring.GetNameList(_number_names, point_spring_names)
        handle(ret)
        return list(point_spring_names)

    def get_point_spring_prop(self, point_spring_name: str) -> PointSpringProperties:
        """Retrieves the point spring property of an existing named point spring.

        :param point_spring_name: name of an existing point spring property
        :type point_spring_name: str
        :return stiffness: point object spring stiffness matrix [U1, U2, U3, R1, R2, R3]
        :rtype: PointSpringProperties
        """
        spring_option = int()
        stiffness = [float()]
        coord_sys = str()
        soil_profile = str()
        footing = str()
        period = float()
        colour = int()
        notes = str()
        guid = str()
        [ret, spring_option, stiffness,
         coord_sys, soil_profile, footing,
         period, colour, notes, guid] = self.prop_point_spring.GetPointSpringProp(point_spring_name, spring_option,
                                                                                  stiffness, coord_sys, soil_profile,
                                                                                  footing, period, colour, notes, guid)
        handle(ret)
        return {'point_spring_name': point_spring_name,
                'spring_option': ePointSpringStiffnessOption(spring_option),
                'stiffness': stiffness,
                'coord_sys': coord_sys,
                'soil_profile': soil_profile,
                'footing': footing,
                'period': period,
                'colour': colour,
                'notes': notes,
                'guid': guid}

    def set_point_spring_prop(self, point_spring_name: str, spring_option: ePointSpringStiffnessOption,
                              stiffness: list[float], coord_sys: str = '', soil_profile: str = '', footing: str = '',
                              period: float = 0., colour: int = 0, notes: str = '', guid: str = '') -> None:
        """Creates a new named point spring property, or modifies an existing named point spring property.

        :param point_spring_name: name of an existing point spring property
        :type point_spring_name: str
        :param spring_option: spring stiffness definition option one of `ePointSpringStiffnessOption`
        :type spring_option: ePointSpringStiffnessOption
        :param stiffness: point object spring stiffness matrix [U1, U2, U3, R1, R2, R3] (applies when `sping_option = ePointSpringStiffnessOption.USER_OR_LINK`)
        :type stiffness: list[float]
        :param coord_sys: name of the coordinate system in which the property is defined, if blank Global is used (applies when `sping_option = ePointSpringStiffnessOption.USER_OR_LINK`)
        :type coord_sys: str, optional
        :param soil_profile: name of an existing Soil Profile (applies when `sping_option = ePointSpringStiffnessOption.SOIL_OR_FOOTING`)
        :type soil_profile: str, optional
        :param footing: name of an existing Isolated Column Footing (applies when `sping_option = ePointSpringStiffnessOption.SOIL_OR_FOOTING`)
        :type footing: str, optional
        :param period: first-mode time period [sec] (applies when `sping_option = ePointSpringStiffnessOption.SOIL_OR_FOOTING`)
        :type period: float, optional
        :param colour: display color for the property specified as an integer
        :type colour: int, optional
        :param notes: notes, if any, assigned to the property
        :type notes: str, optional
        :param guid: global unique identifier
        :type guid: str, optional
        """
        [ret, _point_springs] = self.prop_point_spring.SetPointSpringProp(point_spring_name, spring_option.value,
                                                                          stiffness, coord_sys, soil_profile, footing,
                                                                          period, colour, notes, guid)
        handle(ret)
