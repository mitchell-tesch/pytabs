# PyTABS - ETABS .NET API python wrapper
# PropFrame - cPropFrame interface
__all__ = ['PropFrame']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import etabs
from pytabs.error_handle import handle

# import custom enumerations


# import typing
from typing import TypedDict


class FrameProp(TypedDict):
    """TypedDict class for frame_prop return"""

    number_results: int
    name: list[str]
    prop_type: list[etabs.eFramePropType]
    t3: list[float]
    t2: list[float]
    tf: list[float]
    tw: list[float]
    t2b: list[float]
    tfb: list[float]
    area: list[float]


class PropFrame:
    """PropFrame interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropFrame interface
        self.prop_frame = etabs.cPropFrame(sap_model.PropFrame)

        # relate relevant ETABS enumerations
        self.eFramePropType = etabs.eFramePropType
        """EtabsModel `FramePropType` enumeration"""

        # relate custom enumerations

    def get_all_frame_prop(self) -> FrameProp:
        """Retrieves select data for all frame properties in the model

        :return: All frame properties defined in the model
        :rtype: FrameProp
        """

        number_results = int()
        name = [str()]
        prop_type = []  # self.eFramePropType(int)
        t3 = [float()]
        t2 = [float()]
        tf = [float()]
        tw = [float()]
        t2b = [float()]
        tfb = [float()]
        area = [float()]

        [ret, number_results, name, prop_type, t3, t2, tf, tw, t2b, tfb, area] = (
            self.prop_frame.GetAllFrameProperties_2(number_results, name, prop_type, t3, t2, tf, tw, t2b, tfb, area)
        )

        handle(ret)

        return {
            'number_results': number_results,
            'prop_name': list(name),
            #'prop_type': self.eFramePropType(list(prop_type)), ## enum to be resolved
            'prop_type': prop_type,
            't3': list(t3),
            't2': list(t2),
            'tf': list(tf),
            'tw': list(tw),
            't2b': list(t2b),
            'tfb': list(tfb),
            'area': list(area),
        }

    def set_rectangle_prop(
        self,
        name: str,
        mat_prop: str,
        t3: float,
        t2: float,
        colour: float = -1,
        notes: str = '',
        guid: str = '',
    ) -> None:
        """Initializes a solid rectangular frame section property. If this function is called for an existing frame section property,
        all items for the section are reset to their default value.

        :param name: name of the fame section property
        :type name: str
        :param mat_prop: name of the material property to assign
        :type mat_prop: str
        :param t3: section depth, defined according to model units
        :type t3: float
        :param t2: section width, defined according to model units
        :type t2: float
        :param colour: _description_, defaults to -1
        :type colour: float, optional
        :param notes: _description_, defaults to ''
        :type notes: str, optional
        :param guid: _description_, defaults to ''
        :type guid: str, optional
        :return: _description_
        :rtype: _type_
        """

        return handle(self.prop_frame.SetRectangle(name, mat_prop, t3, t2, colour, notes, guid))
