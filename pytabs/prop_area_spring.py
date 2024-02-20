# pyTABS - ETABS .NET API python wrapper
# PropAreaSpring - cPropAreaSpring
__all__ = ['PropAreaSpring']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class PropAreaSpring:
    """PropAreaSpring interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropAreaSpring interface
        self.prop_area_spring = etabs.cPropAreaSpring(sap_model.PropAreaSpring)
        
        # relate custom enumerations

    def get_names_list(self) -> list[str]:
        """Retrieves the names of all existing defined area spring properties.

        :return line_spring_names: list of area spring names
        :rtype: list(str)
        """

        number_names = int()
        area_spring_names = [str()]
        [ret, number_names, area_spring_names] = self.prop_area_spring.GetNameList(number_names, area_spring_names) 
        handle(ret)
        return list(area_spring_names)
    
    def get_area_spring_prop (self, area_spring_name: str, NonLinearOption3: int) -> list[float]:
        """Retrieves the line spring property of an existing named area spring.

        :param area_spring_name: name of an existing area spring property
        :type area_spring_name: str
        :param NonLinearOption3: nonlinear option for the local 3 direction. 0 = Linear, Resists Tension and Compression, 1 = Resists Compression only, 2 = Resists Tension only
        :type NonLinearOption3: int
        :return area_springs: area object spring stiffness matrix [U1, U2, U3, R1]  in associated area element's local coordinate system
        :rtype: list[float]
        """

        u1 = float()
        u2 = float()
        u3 = float()
        SpringOption = int() #placeholder only - for future release
        SoilProfile = str() #placeholder only - for future release
        EndLengthRatio = float() #placeholder only - for future release
        period = float() #placeholder only - for future release
        color = int()
        notes = str()
        iGUID = str()

        [ret, u1, u2, u3, NonLinearOption3, SpringOption, 
         SoilProfile, EndLengthRatio, period,color, notes, iGUID] = self.prop_area_spring.GetAreaSpringProp(area_spring_name, u1, u2, u3, NonLinearOption3, SpringOption, 
                                                                                                            SoilProfile, EndLengthRatio, period,color, notes, iGUID)
        
        area_springs = [u1, u2, u3]

        handle(ret)
        return area_springs
    

    def set_area_spring_prop(self, area_spring_name: str, area_springs: list[float], NonLinearOption3: int) -> None:
        """Creates a new named area spring property, or modifies an existig named area spring property

        :param area_spring_name: name of the new spring property to be defined or an existing area spring property to re-define
        :type area_spring_name: str
        :param area_springs: area spring stiffness matrix [U1, U2, U3, R1, R2, R3] in associated area element's local coordinate system
        :typ: list[float]
        :param NonLinearOption3: nonlinear option for the local 3 direction. 0 = Linear, Resists Tension and Compression, 1 = Resists Compression only, 2 = Resists Tension only
        :type NonLinearOption3: int
        :return: area spring stiffness matrix [U1, U2, U3, R1]  in associated area element's local coordinate system
        :rtype: list[float]
        """

        #Unpack spring values
        u1 = area_springs[0]
        u2 = area_springs[1]
        u3 = area_springs[2]
        SpringOption = int() #placeholder only - for future release
        SoilProfile = str() #placeholder only - for future release
        EndLengthRatio = float() #placeholder only - for future release
        period = float() #placeholder only - for future release
        color = int()
        notes = str()
        iGUID = str()

        SpringOption = 1

        ret = self.prop_area_spring.SetAreaSpringProp(area_spring_name, u1, u2, u3, NonLinearOption3, SpringOption, SoilProfile, EndLengthRatio, period, color, notes, iGUID)

        handle(ret)
        return #list(line_springs)