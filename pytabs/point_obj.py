# pyTABS - ETABS .NET API python wrapper
# CaseStaticLinear - cCaseStaticLinear
__all__ = ['PointObj']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations
from pytabs.enumerations import *

class PointObj:
    """PointObj Interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PointObj interface
        self.point_obj= etabs.cPointObj(sap_model.PointObj)


    def get_name_from_label (self, label : str, story : str) -> str:
        """Retrieves the unique name of a point object, given the label and story level

        :param label: The point object label 
        :type label: str
        :param story: The point object story level  
        :type label: str
        :return point_name: The unique name of the point object
        :rtype: str
        """

        point_name = str()

        [ret, point_name] = self.point_obj.GetNameFromLabel(label, story, point_name)
        
        #handle(ret) 
        return point_name


