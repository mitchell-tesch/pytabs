# pyTABS - ETABS .NET API python wrapper
# EtabsModel object and cFile interface
__all__ = ['EtabsModel']

# general library imports
import clr # pythonnet clr-loader
from pathlib import Path
from typing import Union, TypedDict


# pythonnet clr-loader import of Marshal - ETABS API requirement
clr.AddReference("System.Runtime.InteropServices")
from System.Runtime.InteropServices import Marshal

# import pyTABS error handler and default settings
from pytabs.error_handle import handle, EtabsError
from pytabs.settings import ETABS_DIR, ETABS_API_DLL, ETABS_EXE
default_etabs_api_path = Path(ETABS_DIR) / ETABS_API_DLL
default_etabs_exe_path = Path(ETABS_DIR) / ETABS_EXE

# pythonnet clr-loader import of ETABS API .dll
clr.AddReference(str(default_etabs_api_path))
from ETABSv1 import *

# import of ETABS API interface wrappers
from pytabs.pier_label import *
from pytabs.analysis_results import *
from pytabs.load_cases import *
from pytabs.resp_combo import *
from pytabs.story import *


class UnitsComponents(TypedDict):
    """TypedDict class for Units components return"""
    force_units : eForce
    length_units : eLength
    temperature_units : eTemperature


class EtabsModel():
    """pyTABS ETABS Model Object (EtabsObject)
    """
    def __init__(self,
                 attach_to_instance : bool = True,
                 specific_etabs : bool = True,
                 specific_etabs_path : Union[str, Path] = default_etabs_exe_path,
                 model_path : Union[str, Path] = '',
                 remote_computer : str = '') -> None:
        """Substantiates the EtabsModel class 

        Args:
            attach_to_instance (bool, optional): attach to active ETABS instance. Defaults to True.
            specific_etabs (bool, optional): use a specific ETABS install. Defaults to True.
            specific_etabs_path (Union[str, Path], optional): path to specific ETABS install. Defaults to default_etabs_exe_path.
            model_path (Union[str, Path], optional): model file path to open specific model file on launch. Defaults to ''.
            remote_computer (str, optional): name of remote machine running csi server. Defaults to ''.

        Raises:
            EtabsError: No running instance ETABS found or failed to attach.
            EtabsError: Cannot start a new instance of the ETABS form {specific_etabs_path}.
            EtabsError: Cannot start a new instance of ETABS.
        """
        # EtabsModel initial properties
        self.active : bool = False
        self.model_open : bool = False
        self.model_path : Union[str, Path] = ''
        
        # create ETABS API helper interface and try to initialise EtabsObject
        helper = cHelper(Helper())
        if attach_to_instance:
            #attach to a running instance of ETABS
            try:
                #get the active ETABS object        
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
                    #'create an instance of the ETABS object from the specified path
                    if remote_computer:
                        self.etabs_object = cOAPI(helper.CreateObjectHost(remote_computer, str(specific_etabs_path)))
                    else:
                        self.etabs_object = cOAPI(helper.CreateObject(str(specific_etabs_path)))
                    self.active = True
                except :
                    raise EtabsError(-1, f"Cannot start a new instance of the ETABS from {str(specific_etabs_path)}")
            else:
                try: 
                    #create an instance of the ETABS object from the latest installed ETABS
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
            # create File interface
            self.file = cFile(self.sap_model.File)
            
            # relate external pyTABS interfaces
            self.pier_label = PierLabel(self.sap_model)
            self.analysis_results = AnalysisResults(self.sap_model)
            self.load_cases = LoadCases(self.sap_model)
            self.resp_combo = RespCombo(self.sap_model)
            self.story = Story(self.sap_model)
            
            # relate ETABS fixed enumerations
            self.eLoadCaseType = eLoadCaseType
            self.eUnits = eUnits
            self.eForce = eForce
            self.eLength = eLength
            self.eTemperature = eTemperature
            
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

        Args:
            model_path (Union[str, Path]): file path to ETABS model file
        """
        handle(self.file.OpenFile(str(model_path)))
        self.model_path = model_path
        self.model_open = True


    def new_model(self, new_model_path: Union[str, Path]) -> None:
        """Creates new blank ETABS model and saves.

        Args:
            new_model_path (Union[str, Path]): file path to save new blank ETABS model file
        """
        handle(self.file.NewBlank())
        handle(self.file.Save(str(new_model_path)))
        self.model_path = new_model_path
        self.model_open = True
        
        
    def get_database_units(self) -> eUnits:
        """Returns a value from the eUnits enumeration indicating the database units for the model.
        All data is internally stored in the model in these units and converted to the present units as needed. 

        Returns:
            eUnits: eUnits enumeration
        """
        ret = self.sap_model.GetDatabaseUnits()
        if ret == 0:
            raise EtabsError(0, "Database units could not be returned.")
        else:
            return ret
    
    
    def get_database_units_components(self) -> UnitsComponents:
        """Retrieves the database units for the model.
        All data is internally stored in the model in these units and converted to the present units as needed. 

        Returns:
            UnitsComponents: TypedDictionary UnitsComponents for force, length and temperature units
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

        Returns:
            bool: model is locked?
        """
        return self.sap_model.GetModelIsLocked()
    
    
    def get_present_coord_system(self) -> str:
        """Retrieves model present coordinate system.

        Returns:
            str: name of coordinate system
        """
        return self.sap_model.GetPresentCoordSystem()
    
    
    def get_present_units(self) -> eUnits:
        """Returns a value from the eUnits enumeration indicating the units presently specified for the model. 

        Returns:
            eUnits: eUnits enumeration
        """
        ret = self.sap_model.GetPresentUnits()
        if ret == 0:
            raise EtabsError(0, "Present units could not be returned.")
        else:
            return ret


    def get_present_units_components(self) -> UnitsComponents:
        """Retrieves the units presently specified for the model.

        Returns:
            UnitsComponents: TypedDictionary UnitsComponents for force, length and temperature units
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

        Args:
            lock_it (bool, optional): Lock model? Defaults to True.
        """
        handle(self.sap_model.SetModelIsLocked(lock_it))
    
    
    def set_present_units(self, units : eUnits):
        """Sets the display (present) units.

        Args:
            units (eUnits): eUnits enumeration to set.
        """
        handle(self.sap_model.SetPresentUnits(units))
        
        
    def set_present_units_components(self, force_units : eForce, length_units : eLength, temperature_units : eTemperature):
        """Specifies the units for the model.

        Args:
            force_units (eForce): eForce enumeration to set.
            length_units (eLength): eLength enumeration to set.
            temperature_units (eTemperature): eTemperature enumeration to set.
        """
        handle(self.sap_model.SetPresentUnits_2(force_units, length_units, temperature_units))