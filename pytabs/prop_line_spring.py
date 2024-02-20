# pyTABS - ETABS .NET API python wrapper
# PropLineSpring - cPropLineSpring
__all__ = ['PropLineSpring']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PropLineSpring:
    """PropLineSpring interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropLineSpring interface
        self.prop_line_spring = etabs.cPropLineSpring(sap_model.PropLineSpring)
        
        # relate custom enumerations

    def get_names_list (self) -> list[str]:
        """Retrieves the names of all existing defined line spring properties.

        :return line_spring_names: list of line spring names
        :rtype: list(str)
        """

        number_names = int()
        line_spring_names = [str()]
        [ret, number_names, line_spring_names] = self.prop_line_spring.GetNameList(number_names, line_spring_names) 
        handle(ret)
        return list(line_spring_names)
    

    def get_line_spring_prop (self, line_spring_name: str, NonLinearOption2: int, NonLinearOption3: int) -> list[float]:
        """Retrieves the line spring property of an existing named line spring.

        :param line_spring_name: name of an existing line spring property
        :type line_spring_name: str
        :param NonLinearOption2: nonlinear option for the local 2 direction. 0 = Linear, Resists Tension and Compression, 1 = Resists Compression only, 2 = Resists Tension only
        :type NonLinearOption2: int
        :param NonLinearOption3: nonlinear option for the local 3 direction. 0 = Linear, Resists Tension and Compression, 1 = Resists Compression only, 2 = Resists Tension only
        :type NonLinearOption3: int
        :return line_springs: line object spring stiffness matrix [U1, U2, U3, R1]  in associated line element's local coordinate system
        :rtype: list[float]
        """

        u1 = float()
        u2 = float()
        u3 = float()
        r1 = float()
        color = int()
        notes = str()
        iGUID = str()

        [ret, u1, u2, u3, r1, NonLinearOption2, 
        NonLinearOption3, color, notes, iGUID] = self.prop_line_spring.GetLineSpringProp(line_spring_name, u1, u2, u3, r1, NonLinearOption2, 
                                                                                        NonLinearOption3, color, notes, iGUID)
        
        line_springs = [u1, u2, u3, r1]

        handle(ret)
        return line_springs
    
    def set_line_spring_prop(self, line_spring_name: str, line_springs: list[float],  NonLinearOption2: int, NonLinearOption3: int) -> list[float]:
        """Creates a new named line spring property, or modifies an existig named line spring property

        :param line_spring_name: name of the new spring property to be defined or an existing line spring property to re-define
        :type line_spring_name: str
        :param line_springs: line spring stiffness matrix [U1, U2, U3, R1, R2, R3] in associated line element's local coordinate system
        :typ: list[float]
        :param NonLinearOption2: nonlinear option for the local 2 direction. 0 = Linear, Resists Tension and Compression, 1 = Resists Compression only, 2 = Resists Tension only
        :type NonLinearOption2: int
        :param NonLinearOption3: nonlinear option for the local 3 direction. 0 = Linear, Resists Tension and Compression, 1 = Resists Compression only, 2 = Resists Tension only
        :type NonLinearOption3: int
        :return: line spring stiffness matrix [U1, U2, U3, R1]  in associated line element's local coordinate system
        :rtype: list[float]
        """

        #Unpack spring values
        u1 = line_springs[0]
        u2 = line_springs[1]
        u3 = line_springs[2]
        r1 = line_springs[3]
        color = int()
        notes = str()
        iGUID = str()

        ret = self.prop_line_spring.SetLineSpringProp(line_spring_name, u1, u2, u3, r1, NonLinearOption2, NonLinearOption3, color, notes, iGUID)

        handle(ret)
        return #list(line_springs)
    