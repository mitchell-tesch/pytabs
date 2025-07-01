# PyTABS - ETABS .NET API python wrapper
# EtabsModel object and cFile interface
__all__ = ['EtabsModel']

# general library imports
from pathlib import Path

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs, pytabs_config
from .error_handle import handle, EtabsError

# import pyTABS custom enumerations
from .enumerations import eFrameDesignProcedure

# import typing
from typing import Union, TypedDict

# import of ETABS API interface wrappers
from .analyse import Analyse
from .analysis_results import AnalysisResults
from .analysis_results_setup import AnalysisResultsSetup
from .area_elm import AreaElm
from .area_obj import AreaObj
from .combo import Combo
from .constraint import Constraint
from .database_tables import DatabaseTables
from .design_results import DesignResults
from .diaphragm import Diaphragm
from .frame_obj import FrameObj
from .grid_sys import GridSys
from .group import Group
from .line_elm import LineElm
from .link_obj import LinkObj
from .load_cases import LoadCases
from .load_patterns import LoadPatterns
from .pier_label import PierLabel
from .point_elm import PointElm
from .point_obj import PointObj
from .property import Property
from .select import Select
from .spandrel_label import SpandrelLabel
from .story import Story
from .tendon_obj import TendonObj
from .tower import Tower
from .view import View


class UnitsComponents(TypedDict):
    """TypedDict class for Units components return"""

    force_units: etabs.eForce
    length_units: etabs.eLength
    temperature_units: etabs.eTemperature


class EtabsModel:
    """pytabs ETABS Model Object `EtabsObject` 🏢.

    All interfaces and enumerations to the Etabs model objects are accessed as properties - refer below.

    """

    def __init__(
        self,
        attach_to_instance: bool = True,
        specific_etabs: bool = False,
        specific_etabs_path: Union[str, Path] = '',
        model_path: Union[str, Path] = '',
        remote_computer: str = '',
    ) -> None:
        # relate ETABS interfaces
        self.analyse: Analyse
        """EtabsModel `Analyse` interface."""
        self.analysis_results_setup: AnalysisResultsSetup
        """EtabsModel `AnalysisResultsSetup` interface."""
        self.analysis_results: AnalysisResults
        """EtabsModel `AnalysisResults` interface."""
        self.area_elm: AreaElm
        """EtabsModel `AreaElm` interface."""
        self.area_obj: AreaObj
        """EtabsModel `AreaObj` interface."""
        # individual case interfaces to be accessed via LoadCase interface
        self.combo: Combo
        """EtabsModel `Combo` interface."""
        self.constraint: Constraint
        """EtabsModel `Constraint` interface."""
        self.database_tables: DatabaseTables
        """EtabsModel `DatabaseTables` interface."""
        self.design_results: DesignResults
        """EtabsModel `DesignResults` interface."""
        self.diaphragm: Diaphragm
        """EtabsModel `Diaphragm` interface."""
        self.frame_obj: FrameObj
        """EtabsModel `FrameObj` interface."""
        self.grid_sys: GridSys
        """EtabsModel `GridSys` interface."""
        self.group: Group
        """EtabsModel `Group` interface."""
        self.line_elm: LineElm
        """EtabsModel `LineElm` interface."""
        self.link_obj: LinkObj
        """EtabsModel `LinkObj` interface."""
        self.load_cases: LoadCases
        """EtabsModel `LoadCases` interface."""
        self.load_patterns: LoadPatterns
        """EtabsModel `LoadPatterns` interface."""
        self.point_elm: PointElm
        """EtabsModel `PointElm` interface."""
        self.point_obj: PointObj
        """EtabsModel `PointObj` interface."""
        self.pier_label: PierLabel
        """EtabsModel `PierLabel` interface."""
        # individual prop interfaces to be accessed via Property interface
        self.property: Property
        """EtabsModel `Property` interface."""
        self.select: Select
        """EtabsModel `Select` interface."""
        self.spandrel_label: SpandrelLabel
        """EtabsModel `SpandrelLabel` interface."""
        self.story: Story
        """EtabsModel `Story` interface."""
        self.tendon_obj: TendonObj
        """EtabsModel `TendonObj` interface."""
        self.tower: Tower
        """EtabsModel `Tower` interface."""
        self.view: View
        """EtabsModel `View` interface."""

        # relate ETABS cross interface enumerations
        self.eAreaDesignOrientation = etabs.eAreaDesignOrientation
        """EtabsModel `AreaDesignOrientation` enumeration."""
        self.eForce = etabs.eForce
        """EtabsModel `Force` enumeration."""
        self.eFrameDesignOrientation = etabs.eFrameDesignOrientation
        """EtabsModel `FrameDesignOrientation` enumeration."""
        self.eItemType = etabs.eItemType
        """EtabsModel `ItemType` enumeration"""
        self.eItemTypeElm = etabs.eItemTypeElm
        """EtabsModel `ItemTypeElm` enumeration"""
        self.eLength = etabs.eLength
        """EtabsModel `Length` enumeration."""
        self.eLoadPatternType = etabs.eLoadPatternType
        """EtabsModel `LoadPatternType` enumeration"""
        self.eObjType = etabs.eObjType
        """EtabsModel `ObjType` enumeration"""
        self.eTemperature = etabs.eTemperature
        """EtabsModel `Temperature` enumeration."""
        self.eUnits = etabs.eUnits
        """EtabsModel `Units` enumeration."""

        # relate pyTABS custom enumerations
        self.eFrameDesignProcedure = eFrameDesignProcedure

        # EtabsModel initial properties
        self.pytabs_config = pytabs_config
        """pyTABS config file (pytabs_config.ini)"""
        self.active: bool = False
        """`True` if EtabsModel is active, otherwise `False`."""
        self.model_open: bool = False
        """`True` if model open, otherwise `False`."""
        self.model_path: Union[str, Path] = ''
        """Etabs model filepath."""

        # create ETABS API helper interface and try to initialise EtabsObject
        helper = etabs.cHelper(etabs.Helper())
        if attach_to_instance:
            # attach to a running instance of ETABS
            try:
                # get the active ETABS object
                if remote_computer:
                    self.etabs_object = etabs.cOAPI(helper.GetObjectHost(remote_computer, 'CSI.ETABS.API.ETABSObject'))
                else:
                    self.etabs_object = etabs.cOAPI(helper.GetObject('CSI.ETABS.API.ETABSObject'))
                self.active = True
            except Exception as e:
                raise EtabsError(
                    -1,
                    'No running instance ETABS found or failed to attach.' + f'\n[{e}]',
                )
            # create an instance of the ETABS object from
        else:
            if specific_etabs:
                try:
                    # create an instance of the ETABS object from the specified path
                    if remote_computer:
                        self.etabs_object = etabs.cOAPI(
                            helper.CreateObjectHost(remote_computer, str(specific_etabs_path))
                        )
                    else:
                        self.etabs_object = etabs.cOAPI(helper.CreateObject(str(specific_etabs_path)))
                    self.active = True
                except Exception as e:
                    raise EtabsError(
                        -1,
                        f'Cannot start a new instance of the ETABS from {str(specific_etabs_path)}' + f'\n[{e}]',
                    )
            else:
                try:
                    # create an instance of the ETABS object from the latest installed ETABS
                    if remote_computer:
                        self.etabs_object = etabs.cOAPI(
                            helper.CreateObjectProgIDHost(remote_computer, 'CSI.ETABS.API.ETABSObject')
                        )
                    else:
                        self.etabs_object = etabs.cOAPI(helper.CreateObjectProgID('CSI.ETABS.API.ETABSObject'))
                    self.active = True
                except Exception as e:
                    raise EtabsError(-1, 'Cannot start a new instance of ETABS.' + f'\n[{e}]')
            # start etabs application
            self.etabs_object.ApplicationStart()

        # if EtabsObject active
        if self.active:
            # create SapModel interface
            self.sap_model = etabs.cSapModel(self.etabs_object.SapModel)
            """EtabsModel `SapModel` interface."""
            # create File interface
            self.file = etabs.cFile(self.sap_model.File)

            # relate external pyTABS interfaces
            self.analyse = Analyse(self.sap_model)
            self.analysis_results_setup = AnalysisResultsSetup(self.sap_model)
            self.analysis_results = AnalysisResults(self.sap_model)
            self.area_elm = AreaElm(self.sap_model)
            self.area_obj = AreaObj(self.sap_model)
            self.combo = Combo(self.sap_model)
            self.constraint = Constraint(self.sap_model)
            self.database_tables = DatabaseTables(self.sap_model)
            self.design_results = DesignResults(self.sap_model)
            self.diaphragm = Diaphragm(self.sap_model)
            self.frame_obj = FrameObj(self.sap_model)
            self.grid_sys = GridSys(self.sap_model)
            self.group = Group(self.sap_model)
            self.line_elm = LineElm(self.sap_model)
            self.link_obj = LinkObj(self.sap_model)
            # individual case interfaces to be accessed via LoadCase interface
            self.load_cases = LoadCases(self.sap_model)
            self.load_patterns = LoadPatterns(self.sap_model)
            self.pier_label = PierLabel(self.sap_model)
            self.point_obj = PointObj(self.sap_model)
            # individual property interfaces to be accessed via Property interface
            self.property = Property(self.sap_model)
            self.select = Select(self.sap_model)
            self.spandrel_label = SpandrelLabel(self.sap_model)
            self.story = Story(self.sap_model)
            self.tendon_obj = TendonObj(self.sap_model)
            self.tower = Tower(self.sap_model)
            self.view = View(self.sap_model)

            # if not attached to instance and model path supplied open model
            if (not attach_to_instance) and model_path:
                self.open_model(model_path)

    def exit_application(self):
        """Terminates ETABS application severing API connection"""
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

    def save_model(self, save_model_path: Union[str, Path]) -> None:
        """Saves the present model.
        If no file name is specified, the file is saved using its current name.
        If there is no current name for the file (the file has not been saved previously)
        and this function is called with no file name specified, an error will be returned.

        :param save_model_path: file path to save new blank ETABS model file
        :type save_model_path: Union[str, Path]
        """

        handle(self.file.Save(str(save_model_path)))
        self.model_path = save_model_path
        self.model_open = True

    def get_model_file_name(self, IncludePath: bool = True) -> str:
        """Returns a string that represents the filename of the current model, with or without the full path

        :param IncludePath: Include full path or not, defaults to True
        :type IncludePath: bool, optional
        :return: filename of current model, with or without the full path
        :rtype: str
        """

        return str(self.sap_model.GetModelFilename(IncludePath))

    def get_database_units(self) -> etabs.eUnits:
        """Returns a value from the eUnits enumeration indicating the database units for the model.
        All data is internally stored in the model in these units and converted to the present units as needed.

        :raises EtabsError: Database units could not be returned
        :return: Units enumeration
        :rtype: eUnits
        """
        ret = self.sap_model.GetDatabaseUnits()
        if ret == 0:
            raise EtabsError(0, 'Database units could not be returned.')
        else:
            return ret

    def get_database_units_components(self) -> UnitsComponents:
        """Retrieves the database units for the model.
        All data is internally stored in the model in these units and converted to the present units as needed.

        :return: units for force, length and temperature units
        :rtype: UnitsComponents
        """
        force_units = etabs.eForce.NotApplicable
        length_units = etabs.eLength.NotApplicable
        temperature_units = etabs.eTemperature.NotApplicable
        [ret, force_units, length_units, temperature_units] = self.sap_model.GetDatabaseUnits_2(
            force_units, length_units, temperature_units
        )
        handle(ret)
        return {
            'force_units': force_units,
            'length_units': length_units,
            'temperature_units': temperature_units,
        }

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

    def get_present_units(self) -> etabs.eUnits:
        """Returns a value from the eUnits enumeration indicating the units presently specified for the model.

        :raises EtabsError: Present units could not be returned
        :return: Units enumeration
        :rtype: eUnits
        """
        ret = self.sap_model.GetPresentUnits()
        if ret == 0:
            raise EtabsError(0, 'Present units could not be returned.')
        else:
            return ret

    def get_present_units_components(self) -> UnitsComponents:
        """Retrieves the units presently specified for the model.

        :return: units components for force, length and temperature units
        :rtype: UnitsComponents
        """
        force_units = etabs.eForce.NotApplicable
        length_units = etabs.eLength.NotApplicable
        temperature_units = etabs.eTemperature.NotApplicable
        [ret, force_units, length_units, temperature_units] = self.sap_model.GetPresentUnits_2(
            force_units, length_units, temperature_units
        )
        handle(ret)
        return {
            'force_units': force_units,
            'length_units': length_units,
            'temperature_units': temperature_units,
        }

    def set_model_is_locked(self, lock_it: bool = True):
        """Locks or unlocks the model.

        :param lock_it: True to lock mode, False to unlock, defaults to True
        :type lock_it: bool, optional
        """
        handle(self.sap_model.SetModelIsLocked(lock_it))

    def set_present_units(self, units: etabs.eUnits):
        """Sets the display (present) units.

        :param units: Units enumeration to set.
        :type units: eUnits
        """
        handle(self.sap_model.SetPresentUnits(units))

    def set_present_units_components(
        self,
        force_units: etabs.eForce,
        length_units: etabs.eLength,
        temperature_units: etabs.eTemperature,
    ):
        """Specifies the units for the model.

        :param force_units: Force enumeration to set
        :type force_units: eForce
        :param length_units: Length enumeration to set
        :type length_units: eLength
        :param temperature_units: Temperature enumeration to set
        :type temperature_units: eTemperature
        """
        handle(self.sap_model.SetPresentUnits_2(force_units, length_units, temperature_units))
