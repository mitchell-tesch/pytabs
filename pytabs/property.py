# pyTABS - ETABS .NET API python wrapper
# Property - pyTABS interface to all prop type interfaces
__all__ = ['Property']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import of interfaces of prop types
from pytabs.prop_area_spring import PropAreaSpring
from pytabs.prop_area import PropArea
from pytabs.prop_frame import PropFrame
from pytabs.prop_line_spring import PropLineSpring
from pytabs.prop_link import PropLink
from pytabs.prop_material import PropMaterial
from pytabs.prop_point_spring import PropPointSpring
from pytabs.prop_rebar import PropRebar
from pytabs.prop_tendon import PropTendon


class Property:
    """Properties interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
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