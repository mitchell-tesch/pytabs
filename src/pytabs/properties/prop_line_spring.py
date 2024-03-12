# PyTABS - ETABS .NET API python wrapper
# PropLineSpring - cPropLineSpring interface
__all__ = ['PropLineSpring']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import etabs
from pytabs.error_handle import handle

# import custom enumerations
from pytabs.enumerations import eSpringNonlinearOption

# import typing
from typing import TypedDict


class LineSpringProperties(TypedDict):
    """TypedDict class for line spring properties return"""
    line_spring_name: str
    u1: float
    u2: float
    u3: float
    r1: float
    nonlinear_option_2: eSpringNonlinearOption
    nonlinear_option_3: eSpringNonlinearOption
    colour: int
    notes: str
    guid: str


class PropLineSpring:
    """PropLineSpring interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropLineSpring interface
        self.prop_line_spring = etabs.cPropLineSpring(sap_model.PropLineSpring)

        # relate custom enumerations
        self.eSpringNonlinearOption = eSpringNonlinearOption

    def get_names_list(self) -> list[str]:
        """Retrieves the names of all existing defined line spring properties.

        :return line_spring_names: list of line spring names
        :rtype: list(str)
        """
        _number_names = int()
        line_spring_names = [str()]
        [ret, _number_names, line_spring_names] = self.prop_line_spring.GetNameList(_number_names, line_spring_names)
        handle(ret)
        return list(line_spring_names)

    def get_line_spring_prop(self, name: str) -> LineSpringProperties:
        """Retrieves the line spring property of an existing named line spring.

        :param line_spring_name: name of an existing line spring property
        :type line_spring_name: str
        :return line_springs: properties of line spring
        :rtype: LineSpringProperties
        """
        u1 = float()
        u2 = float()
        u3 = float()
        r1 = float()
        nonlinear_option_2 = int()
        nonlinear_option_3 = int()
        colour = int()
        notes = str()
        guid = str()
        [ret, u1, u2, u3, r1, nonlinear_option_2,
         nonlinear_option_3, colour, notes, guid] = self.prop_line_spring.GetLineSpringProp(name, u1, u2, u3, r1,
                                                                                            nonlinear_option_2, nonlinear_option_3,
                                                                                            colour, notes, guid)
        handle(ret)
        return {'line_spring_name': name,
                'u1': u1,
                'u2': u2,
                'u3': u3,
                'r1': r1,
                'nonlinear_option_2': eSpringNonlinearOption(nonlinear_option_2),
                'nonlinear_option_3': eSpringNonlinearOption(nonlinear_option_3),
                'colour': colour,
                'notes': notes,
                'guid': guid}

    def set_line_spring_prop(self, name: str, stiffness: list[float],
                             nonlinear_option_2: eSpringNonlinearOption, nonlinear_option_3: eSpringNonlinearOption,
                             colour: int = 0, notes: str = '', guid: str = '') -> None:
        """Creates a new named line spring property, or modifies an existing named line spring property

        :param name: name of the new spring property to be defined or an existing line spring property to re-define
        :type name: str
        :param stiffness: line spring stiffness matrix [U1, U2, U3, R1] in associated line element's local coordinate system
        :type: list[float]
        :param nonlinear_option_2: nonlinear option for the local 2 direction
        :type nonlinear_option_2: eSpringNonlinearOption
        :param nonlinear_option_3: nonlinear option for the local 3 direction
        :type nonlinear_option_3: eSpringNonlinearOption
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
        r1 = stiffness[3]
        handle(self.prop_line_spring.SetLineSpringProp(name, u1, u2, u3, r1, nonlinear_option_2.value,
                                                       nonlinear_option_3.value, colour, notes, guid))
