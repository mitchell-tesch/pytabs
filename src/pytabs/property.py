# PyTABS - ETABS .NET API python wrapper
# Property - pyTABS interface to all prop type interfaces
__all__ = ['Property']

# import ETABS namespace and pyTABS error handler
from .etabs_config import *
from .error_handle import *

# import of interfaces of prop types
from .properties.prop_area_spring import PropAreaSpring
from .properties.prop_area import PropArea
from .properties.prop_frame import PropFrame
from .properties.prop_line_spring import PropLineSpring
from .properties.prop_link import PropLink
from .properties.prop_material import PropMaterial
from .properties.prop_point_spring import PropPointSpring
from .properties.prop_rebar import PropRebar
from .properties.prop_tendon import PropTendon


class Property:
    """Properties interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        
        # create interface for individual property types
        self.area_spring = PropAreaSpring(sap_model)
        self.area = PropArea(sap_model)
        self.frame = PropFrame(sap_model)
        self.line_spring = PropLineSpring(sap_model)
        self.link = PropLink(sap_model)
        self.material = PropMaterial(sap_model)
        self.point_spring = PropPointSpring(sap_model)
        self.rebar = PropRebar(sap_model)
        self.tendon = PropTendon(sap_model)
