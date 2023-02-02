# pyTABS - ETABS .NET API python wrapper
# EtabsModel object and cFile interface
__all__ = ['EtabsModel']

# general library imports
from pathlib import Path

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import handle, EtabsError

# import typing
from typing import Union, TypedDict

# import of ETABS API interface wrappers
from pytabs.pier_label import PierLabel
from pytabs.analysis_results import AnalysisResults
from pytabs.load_patterns import LoadPatterns
from pytabs.load_cases import LoadCases
from pytabs.resp_combo import RespCombo
from pytabs.story import Story
from pytabs.group import Group
from pytabs.frame_obj import FrameObj
from pytabs.area_obj import AreaObj


class UnitsComponents(TypedDict):
    """TypedDict class for Units components return"""
    force_units : eForce
    length_units : eLength
    temperature_units : eTemperature


class EtabsModel():
    """pytabs ETABS Model Object `EtabsObject` 🏢. 
    
    All interfaces and enumerations to the Etabs model objects are accessed as properties - refer below.
    
    """
    def __init__(self,
                 attach_to_instance : bool = True,
                 specific_etabs : bool = False,
                 specific_etabs_path : Union[str, Path] = '',
                 model_path : Union[str, Path] = '',
                 remote_computer : str = '') -> None:
        
        # relate ETABS interfaces
        self.pier_label : PierLabel
        """EtabsModel `PierLabel` interface."""
        self.analysis_results : AnalysisResults
        """EtabsModel `AnalysisResults` interface."""
        self.load_patterns : LoadPatterns
        """EtabsModel `LoadPatterns` interface."""
        self.load_cases : LoadCases
        """EtabsModel `LoadCases` interface."""
        self.resp_combo : RespCombo
        """EtabsModel `RespCombo` interface."""
        self.story : Story
        """EtabsModel `Story` interface."""
        self.group : Group
        """EtabsModel `Group` interface."""
        self.frame_obj : FrameObj
        """EtabsModel `FrameObj` interface."""
        self.area_obj : AreaObj
        """EtabsModel `AreaObj` interface."""
        
        # relate ETABS fixed enumerations
        self.eUnits = eUnits
        """EtabsModel `Units` enumeration."""
        self.eForce = eForce
        """EtabsModel `Force` enumeration."""
        self.eLength = eLength
        """EtabsModel `Length` enumeration."""
        self.eTemperature = eTemperature
        """EtabsModel `Temperature` enumeration."""
        self.eItemType = eItemType
        """EtabsModel `ItemType` enumeration"""
        self.eLoadCaseType = eLoadCaseType
        """EtabsModel `LoadCaseType` enumeration"""
        self.eLoadPatternType = eLoadPatternType
        """EtabsModel `LoadPatternType` enumeration"""
        
        # EtabsModel initial properties
        self.pytabs_config = pytabs_config
        """pyTABS config file (pytabs_config.ini)"""
        self.active : bool = False
        """`True` if EtabsModel is active, otherwise `False`."""
        self.model_open : bool = False
        """`True` if model open, otherwise `False`."""
        self.model_path : Union[str, Path] = ''
        """Etabs model filepath."""
        
        # create ETABS API helper interface and try to initialise EtabsObject
        helper = cHelper(Helper())
        if attach_to_instance:
            # attach to a running instance of ETABS
            try:
                # get the active ETABS object        
                if remote_computer:
                    self.etabs_object = cOAPI(helper.GetObjectHost(remote_computer, "CSI.ETABS.API.ETABSObject"))
                else:
                    self.etabs_object = cOAPI(helper.GetObject("CSI.ETABS.API.ETABSObject"))
                self.active = True
            except:
                raise EtabsError(-1, "No running instance ETABS found or failed to attach.")
        else:
            if specific_etabs:
                try:
                    # create an instance of the ETABS object from the specified path
                    if remote_computer:
                        self.etabs_object = cOAPI(helper.CreateObjectHost(remote_computer, str(specific_etabs_path)))
                    else:
                        self.etabs_object = cOAPI(helper.CreateObject(str(specific_etabs_path)))
                    self.active = True
                except :
                    raise EtabsError(-1, f"Cannot start a new instance of the ETABS from {str(specific_etabs_path)}")
            else:
                try: 
                    # create an instance of the ETABS object from the latest installed ETABS
                    if remote_computer:
                        self.etabs_object = cOAPI(helper.CreateObjectProgIDHost(remote_computer, "CSI.ETABS.API.ETABSObject"))
                    else:
                        self.etabs_object = cOAPI(helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject"))
                    self.active = True
                except:
                    raise EtabsError(-1, "Cannot start a new instance of ETABS.")
            # start etabs application
            self.etabs_object.ApplicationStart()
        
        # if EtabsObject active 
        if self.active:
            # create SapModel interface
            self.sap_model = cSapModel(self.etabs_object.SapModel)
            """EtabsModel `SapModel` interface."""
            # create File interface
            self.file = cFile(self.sap_model.File)
            
            # relate external pyTABS interfaces
            self.pier_label = PierLabel(self.sap_model)
            self.analysis_results = AnalysisResults(self.sap_model)
            self.load_patterns = LoadPatterns(self.sap_model)
            self.load_cases = LoadCases(self.sap_model)
            self.resp_combo = RespCombo(self.sap_model)
            self.story = Story(self.sap_model)
            self.frame_obj = FrameObj(self.sap_model)
            self.group = Group(self.sap_model)
            self.area_obj = AreaObj(self.sap_model)

            # if not attached to instance and model path supplied open model
            if (not attach_to_instance) and model_path:
                self.open_model(model_path)


    def exit_application(self):
        '''Terminates ETABS application severing API connection'''
        self.etabs_object.ApplicationExit(False)
        self.model_open = False
        self.model_path = ''
        self.sap_model = None
        self.active = False


    def open_model(self, model_path: Union[str, Path]) -> None:
        """Opens ETABS model file.

        :param model_path: file path to ETABS model file
        :type model_path: Union[str, Path]
        """
        handle(self.file.OpenFile(str(model_path)))
        self.model_path = model_path
        self.model_open = True


    def new_model(self, new_model_path: Union[str, Path]) -> None:
        """Creates new blank ETABS model and saves.

        :param new_model_path: file path to save new blank ETABS model file
        :type new_model_path: Union[str, Path]
        """
        handle(self.file.NewBlank())
        handle(self.file.Save(str(new_model_path)))
        self.model_path = new_model_path
        self.model_open = True
        
        
    def get_database_units(self) -> eUnits:
        """Returns a value from the eUnits enumeration indicating the database units for the model.
        All data is internally stored in the model in these units and converted to the present units as needed.

        :raises EtabsError: Database units could not be returned
        :return: Units enumeration
        :rtype: eUnits
        """
        ret = self.sap_model.GetDatabaseUnits()
        if ret == 0:
            raise EtabsError(0, "Database units could not be returned.")
        else:
            return ret
    
    
    def get_database_units_components(self) -> UnitsComponents:
        """Retrieves the database units for the model.
        All data is internally stored in the model in these units and converted to the present units as needed.

        :return: units for force, length and temperature units
        :rtype: UnitsComponents
        """
        force_units = eForce.NotApplicable
        length_units = eLength.NotApplicable
        temperature_units = eTemperature.NotApplicable
        [ret, force_units, length_units, temperature_units] =  self.sap_model.GetDatabaseUnits_2(force_units, length_units, temperature_units)
        handle(ret)
        return {'force_units': force_units,
                'length_units': length_units,
                'temperature_units': temperature_units}


    def get_model_is_locked(self) -> bool:
        """Retrieves locked status of the model.

        :return: True if model is looked, otherwise False
        :rtype: bool
        """
        return self.sap_model.GetModelIsLocked()
    
    
    def get_present_coord_system(self) -> str:
        """Retrieves model present coordinate system.

        :return: name of coordinate system
        :rtype: str
        """
        return self.sap_model.GetPresentCoordSystem()
    
    
    def get_present_units(self) -> eUnits:
        """Returns a value from the eUnits enumeration indicating the units presently specified for the model.

        :raises EtabsError: Present units could not be returned
        :return: Units enumeration
        :rtype: eUnits
        """
        ret = self.sap_model.GetPresentUnits()
        if ret == 0:
            raise EtabsError(0, "Present units could not be returned.")
        else:
            return ret


    def get_present_units_components(self) -> UnitsComponents:
        """Retrieves the units presently specified for the model.

        :return: units components for force, length and temperature units
        :rtype: UnitsComponents
        """
        force_units = eForce.NotApplicable
        length_units = eLength.NotApplicable
        temperature_units = eTemperature.NotApplicable
        [ret, force_units, length_units, temperature_units] =  self.sap_model.GetPresentUnits_2(force_units, length_units, temperature_units)
        handle(ret)
        return {'force_units': force_units,
                'length_units': length_units,
                'temperature_units': temperature_units}
        
        
    def set_model_is_locked(self, lock_it : bool = True):
        """Locks or unlocks the model.

        :param lock_it: True to lock mode, False to unlock, defaults to True
        :type lock_it: bool, optional
        """
        handle(self.sap_model.SetModelIsLocked(lock_it))
    
    
    def set_present_units(self, units : eUnits):
        """Sets the display (present) units.

        :param units: Units enumeration to set.
        :type units: eUnits
        """
        handle(self.sap_model.SetPresentUnits(units))
        
        
    def set_present_units_components(self, force_units : eForce, length_units : eLength, temperature_units : eTemperature):
        """Specifies the units for the model.

        :param force_units: Force enumeration to set
        :type force_units: eForce
        :param length_units: Length enumeration to set
        :type length_units: eLength
        :param temperature_units: Temperature enumeration to set
        :type temperature_units: eTemperature
        """
        handle(self.sap_model.SetPresentUnits_2(force_units, length_units, temperature_units))