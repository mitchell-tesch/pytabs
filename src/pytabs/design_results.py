# PyTABS - ETABS .NET API python wrapper
# DesignResults - cDesignResults interface
__all__ = ['DesignForces']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations

# import typing
from typing import TypedDict


class BeamDesignForce(TypedDict):
    """TypedDict class for beam_design_force return"""
    number_results: int
    frame_name: list[str]
    combo_name: list[str]
    station: list[float]
    axial: list[float]
    shear_2: list[float]
    shear_3: list[float]
    torsion: list[float]
    moment_2: list[float]
    moment_3: list[float]


class DesignResults:
    """DesignForcesResults interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create DesignResults interface
        self.design_forces = etabs.cDesignForces(sap_model.DesignResults.DesignForces)

        # relate custom enumerations
        # self.eResultsSetupStepOutOption = eResultsSetupStepOutOption
        # self.eResultsSetupComboOutOption = eResultsSetupComboOutOption

    # Design Results Methods
    def beam_design_forces(self, name: str, item_type_element: etabs.eItemType) -> BeamDesignForce:
        number_results = int()
        frame_name = [str()]
        combo_name = [str()]
        station = [float()]
        axial = [float()]
        shear_2 = [float()]
        shear_3 = [float()]
        torsion = [float()]
        moment_2 = [float()]
        moment_3 = [float()]

        [ret, number_results, frame_name,
         combo_name,station,
         axial, shear_2, shear_3,
         torsion, moment_2, moment_3] = self.design_forces.BeamDesignForces(name, number_results, frame_name,
                                                                            combo_name,station,
                                                                            axial, shear_2, shear_3,
                                                                            torsion, moment_2, moment_3,
                                                                            item_type_element)
        handle(ret)
        return {'number_results': number_results,
                'frame_name': list(frame_name),
                'combo_name': list(combo_name),
                'station': list(station),
                'axial': list(axial),
                'shear_2': list(shear_2),
                'shear_3': list(shear_3),
                'torsion': list(torsion),
                'moment_2': list(moment_2),
                'moment_3': list(moment_3)}
