# PyTABS - ETABS .NET API python wrapper
# PropAreaSpring - cPropAreaSpring interface
__all__ = ['PropAreaSpring']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import etabs
from pytabs.error_handle import handle

# import custom enumerations
from pytabs.enumerations import eSpringNonlinearOption

# import typing
from typing import TypedDict


class AreaSpringProperties(TypedDict):
    """TypedDict class for area spring properties return"""

    area_spring_name: str
    u1: float
    u2: float
    u3: float
    nonlinear_option_3: eSpringNonlinearOption
    spring_option: int
    soil_profile: str
    end_length_ratio: float
    period: float
    colour: int
    notes: str
    guid: str


class PropAreaSpring:
    """PropAreaSpring interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropAreaSpring interface
        self.prop_area_spring = etabs.cPropAreaSpring(sap_model.PropAreaSpring)

        # relate custom enumerations
        self.eSpringNonlinearOption = eSpringNonlinearOption

    def get_names_list(self) -> list[str]:
        """Retrieves the names of all existing defined area spring properties.

        :return line_spring_names: list of area spring names
        :rtype: list(str)
        """
        _number_names = int()
        area_spring_names = [str()]
        [ret, _number_names, area_spring_names] = self.prop_area_spring.GetNameList(_number_names, area_spring_names)
        handle(ret)
        return list(area_spring_names)

    def get_area_spring_prop(self, area_spring_name: str) -> AreaSpringProperties:
        """Retrieves the line spring property of an existing named area spring.

        :param area_spring_name: name of an existing area spring property
        :type area_spring_name: str
        :return area_springs: properties of area spring
        :rtype: AreaSpringProperties
        """
        u1 = float()
        u2 = float()
        u3 = float()
        nonlinear_option_3 = int()
        spring_option = int()  # placeholder only - for future release
        soil_profile = str()  # placeholder only - for future release
        end_length_ratio = float()  # placeholder only - for future release
        period = float()  # placeholder only - for future release
        colour = int()
        notes = str()
        guid = str()

        [
            ret,
            u1,
            u2,
            u3,
            nonlinear_option_3,
            spring_option,
            soil_profile,
            end_length_ratio,
            period,
            colour,
            notes,
            guid,
        ] = self.prop_area_spring.GetAreaSpringProp(
            area_spring_name,
            u1,
            u2,
            u3,
            nonlinear_option_3,
            spring_option,
            soil_profile,
            end_length_ratio,
            period,
            colour,
            notes,
            guid,
        )
        handle(ret)
        return {
            'area_spring_name': area_spring_name,
            'u1': u1,
            'u2': u2,
            'u3': u3,
            'nonlinear_option_3': eSpringNonlinearOption(nonlinear_option_3),
            'spring_option': spring_option,
            'soil_profile': soil_profile,
            'end_length_ratio': end_length_ratio,
            'period': period,
            'colour': colour,
            'notes': notes,
            'guid': guid,
        }

    def set_area_spring_prop(
        self,
        area_spring_name: str,
        stiffness: list[float],
        nonlinear_option_3: eSpringNonlinearOption,
        spring_option: int = 1,
        soil_profile: str = '',
        end_length_ratio: float = 0.0,
        period: float = 0.0,
        colour: int = 0,
        notes: str = '',
        guid: str = '',
    ) -> None:
        """Creates a new named area spring property, or modifies an existing named area spring property

        :param area_spring_name: name of the new spring property to be defined or an existing area spring property to re-define
        :type area_spring_name: str
        :param stiffness: area spring stiffness matrix [U1, U2, U3] in associated area element's local coordinate system
        :type: list[float]
        :param nonlinear_option_3: nonlinear option for the local 3 direction
        :type nonlinear_option_3: eSpringNonlinearOption
        :param spring_option: argument is for a future release
        :type spring_option: int, optional
        :param soil_profile: argument is for a future release
        :type soil_profile: str, optional
        :param end_length_ratio: argument is for a future release
        :type end_length_ratio: float, optional
        :param period: argument is for a future release
        :type period: float, optional
        :param colour: display color for the property specified as an integer
        :type colour: int, optional
        :param notes: notes, if any, assigned to the property
        :type notes: str, optional
        :param guid: global unique identifier
        :type guid: str, optional
        """
        # Unpack spring values
        u1 = stiffness[0]
        u2 = stiffness[1]
        u3 = stiffness[2]
        handle(
            self.prop_area_spring.SetAreaSpringProp(
                area_spring_name,
                u1,
                u2,
                u3,
                nonlinear_option_3.value,
                spring_option,
                soil_profile,
                end_length_ratio,
                period,
                colour,
                notes,
                guid,
            )
        )
