# PyTABS - ETABS .NET API python wrapper
# AnalysisResults - cAnalysisResults interface
__all__ = ['AnalysisResults']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations
from .enumerations import (eResultsSetupStepOutOption, eResultsSetupComboOutOption)

# import typing
from typing import TypedDict


class BaseReact(TypedDict):
    """TypedDict class for base_react return"""
    number_results: int
    load_case: list[str]
    step_type: list[str]
    step_number: list[float]
    force_x: list[float]
    force_y: list[float]
    force_z: list[float]
    moment_x: list[float]
    moment_y: list[float]
    moment_z: list[float]
    x_coordinate: list[float]
    y_coordinate: list[float]
    z_coordinate: list[float]


class BaseReactWithCentroid(TypedDict):
    """TypedDict class for base_react_with_centroid return"""
    number_results: int
    load_case: list[str]
    step_type: list[str]
    step_number: list[float]
    force_x: list[float]
    force_y: list[float]
    force_z: list[float]
    moment_x: list[float]
    moment_y: list[float]
    moment_z: list[float]
    x_coordinate: list[float]
    y_coordinate: list[float]
    z_coordinate: list[float]
    x_centroid_for_force_x: list[float]
    y_centroid_for_force_x: list[float]
    z_centroid_for_force_x: list[float]
    x_centroid_for_force_y: list[float]
    y_centroid_for_force_y: list[float]
    z_centroid_for_force_y: list[float]
    x_centroid_for_force_z: list[float]
    y_centroid_for_force_z: list[float]
    z_centroid_for_force_z: list[float]


class BucklingFactor(TypedDict):
    """TypedDict class for buckling_factor return"""
    number_results: int
    load_case: list[str]
    step_type: list[str]
    step_number: list[float]
    factor: list[float]

class FrameForce(TypedDict):
    """TypedDict class for frame_force return"""
    number_results: int
    object_name: list[str]
    object_station: list[float]
    element_name: list[str]
    element_station: list[float]
    load_case: list[str]
    step_type: list[str]
    step_number: list[int]
    axial_force: list[float]
    shear_2: list[float]
    shear_3: list[float]
    torsion: list[float]
    moment_2: list[float]
    moment_3: list[float]



class JointDisplacement(TypedDict):
    """TypedDict class for joint_displacement return"""
    number_results: int
    object_name: list[str]
    element_name: list[str]
    load_case: list[str]
    step_type: list[str]
    step_number: list[float]
    delta_1: list[float]
    delta_2: list[float]
    delta_3: list[float]
    rotation_1: list[float]
    rotation_2: list[float]
    rotation_3: list[float]


class ModalLoadParticipationRatios(TypedDict):
    """Typed class for modal_load_participation_ratios"""
    number_results: int
    load_case: list[str]
    item_type: list[str]
    item: list[str]
    static_ratios: list[float]
    dynamic_ratios: list[float]


class ModalParticipatingMassRatios(TypedDict):
    """TypedDict class for modal_participating_mass_ratios"""
    number_results: int
    load_case: list[str]
    step_type: list[str]
    step_number: list[float]
    period: list[float]
    delta_x: list[float]
    delta_y: list[float]
    delta_z: list[float]
    sum_delta_x: list[float]
    sum_delta_y: list[float]
    sum_delta_z: list[float]
    rotation_x: list[float]
    rotation_y: list[float]
    rotation_z: list[float]
    sum_rotation_x: list[float]
    sum_rotation_y: list[float]
    sum_rotation_z: list[float]


class ModalParticipationFactors(TypedDict):
    """TypedDict class for modal_participation_factors"""
    number_results: int
    load_case: list[str]
    step_type: list[str]
    step_number: list[float]
    period: list[float]
    delta_x: list[float]
    delta_y: list[float]
    delta_z: list[float]
    rotation_x: list[float]
    rotation_y: list[float]
    rotation_z: list[float]
    modal_mass: list[float]
    modal_stiff: list[float]


class ModalPeriod(TypedDict):
    """TypedDict class for modal_period return"""
    number_results: int
    load_case: list[str]
    step_type: list[str]
    step_number: list[int]
    period: list[float]
    frequency: list[float]
    circular_frequency: list[float]
    eigen_value: list[float]


class PierForce(TypedDict):
    """TypedDict class for pir_force return"""
    number_results: int
    story_name: list[str]
    pier_name: list[str]
    load_case: list[str]
    location: list[str]
    axial: list[float]
    shear_2: list[float]
    shear_3: list[float]
    torsion: list[float]
    moment_2: list[float]
    moment_3: list[float]


class SectionCutAnalysis(TypedDict):
    """TypedDict class for section_cut_analysis return"""
    number_results: int
    section_cut: list[str]
    load_case: list[str]
    step_type: list[str]
    step_number: list[float]
    force_1: list[float]
    force_2: list[float]
    force_3: list[float]
    moment_1: list[float]
    moment_2: list[float]
    moment_3: list[float]


class SectionCutDesign(TypedDict):
    """TypedDict class for section_cut_design return"""
    number_results: int
    section_cut: list[str]
    load_case: list[str]
    step_type: list[str]
    step_number: list[float]
    axial: list[float]
    shear_2: list[float]
    shear_3: list[float]
    torsion: list[float]
    moment_2: list[float]
    moment_3: list[float]


class SpandrelForce(TypedDict):
    """TypedDict class for spandrel_force return"""
    number_results: int
    story_name: list[str]
    spandrel_name: list[str]
    load_case: list[str]
    location: list[str]
    axial: list[float]
    shear_2: list[float]
    shear_3: list[float]
    torsion: list[float]
    moment_2: list[float]
    moment_3: list[float]


class StoryDrift(TypedDict):
    """TypedDict class for story_drift return"""
    number_results: int
    story: list[str]
    load_case: list[str]
    step_type: list[str]
    step_number: list[float]
    direction: list[str]
    drift: list[float]
    label: list[str]
    delta_x: list[float]
    delta_y: list[float]
    delta_z: list[float]


class AnalysisResults:
    """AnalysisResults interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create AnalysisResults interface
        self.analysis_results = etabs.cAnalysisResults(sap_model.Results)

        # relate custom enumerations
        self.eResultsSetupStepOutOption = eResultsSetupStepOutOption
        self.eResultsSetupComboOutOption = eResultsSetupComboOutOption

    # Analysis Results Methods
    # TODO: AreaForceShell
    # TODO: AreaJointForceShell
    # TODO: AreaStrainShell
    # TODO: AreaStrainShellLayered
    # TODO: AreaStressShell
    # TODO: AreaStressShellLayered,
    # TODO: AssembledJoinMass

    def base_react(self) -> BaseReact:
        """Reports the structure total base reactions.
        
        :return: total base reactions analysis results 
        :rtype: BaseReact
        """
        number_results = int()
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        force_x = [float()]
        force_y = [float()]
        force_z = [float()]
        moment_x = [float()]
        moment_y = [float()]
        moment_z = [float()]
        x_coordinate = float()
        y_coordinate = float()
        z_coordinate = float()

        [ret, number_results, load_case, step_type, step_number, force_x,
         force_y, force_z, moment_x, moment_y,
         moment_z, x_coordinate, y_coordinate, z_coordinate] = self.analysis_results.BaseReact(number_results,
                                                                                               load_case, step_type,
                                                                                               step_number, force_x,
                                                                                               force_y,
                                                                                               force_z, moment_x,
                                                                                               moment_y, moment_z,
                                                                                               x_coordinate,
                                                                                               y_coordinate,
                                                                                               z_coordinate)
        handle(ret)
        return {'number_results': number_results,
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'force_x': list(force_x),
                'force_y': list(force_y),
                'force_z': list(force_z),
                'moment_x': list(moment_x),
                'moment_y': list(moment_y),
                'moment_z': list(moment_z),
                'x_coordinate': x_coordinate,
                'y_coordinate': y_coordinate,
                'z_coordinate': z_coordinate}

    def base_react_with_centroid(self) -> BaseReactWithCentroid:
        """Reports the structure total base reactions and includes information on the centroid of the translational reaction forces.
        
        :return: Base reaction with centriod analysis results 
        :rtype: BaseReactWithCentroid
        """
        number_results = int()
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        force_x = [float()]
        force_y = [float()]
        force_z = [float()]
        moment_x = [float()]
        moment_y = [float()]
        moment_z = [float()]
        x_coordinate = float()
        y_coordinate = float()
        z_coordinate = float()
        x_centroid_for_force_x = [float()]
        y_centroid_for_force_x = [float()]
        z_centroid_for_force_x = [float()]
        x_centroid_for_force_y = [float()]
        y_centroid_for_force_y = [float()]
        z_centroid_for_force_y = [float()]
        x_centroid_for_force_z = [float()]
        y_centroid_for_force_z = [float()]
        z_centroid_for_force_z = [float()]

        [ret, number_results, load_case, step_type, step_number,
         force_x, force_y, force_z, moment_x, moment_y, moment_z,
         x_coordinate, y_coordinate, z_coordinate,
         x_centroid_for_force_x, y_centroid_for_force_x, z_centroid_for_force_x,
         x_centroid_for_force_y, y_centroid_for_force_y, z_centroid_for_force_y,
         x_centroid_for_force_z, y_centroid_for_force_z,
         z_centroid_for_force_z] = self.analysis_results.BaseReactWithCentroid(number_results, load_case, step_type,
                                                                               step_number,
                                                                               force_x, force_y, force_z, moment_x,
                                                                               moment_y, moment_z,
                                                                               x_coordinate, y_coordinate, z_coordinate,
                                                                               x_centroid_for_force_x,
                                                                               y_centroid_for_force_x,
                                                                               z_centroid_for_force_x,
                                                                               x_centroid_for_force_y,
                                                                               y_centroid_for_force_y,
                                                                               z_centroid_for_force_y,
                                                                               x_centroid_for_force_z,
                                                                               y_centroid_for_force_z,
                                                                               z_centroid_for_force_z)
        handle(ret)
        return {'number_results': number_results,
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'force_x': list(force_x),
                'force_y': list(force_y),
                'force_z': list(force_z),
                'moment_x': list(moment_x),
                'moment_y': list(moment_y),
                'moment_z': list(moment_z),
                'x_coordinate': x_coordinate,
                'y_coordinate': y_coordinate,
                'z_coordinate': z_coordinate,
                'x_centroid_for_force_x': list(x_centroid_for_force_x),
                'y_centroid_for_force_x': list(y_centroid_for_force_x),
                'z_centroid_for_force_x': list(z_centroid_for_force_x),
                'x_centroid_for_force_y': list(x_centroid_for_force_y),
                'y_centroid_for_force_y': list(y_centroid_for_force_y),
                'z_centroid_for_force_y': list(z_centroid_for_force_y),
                'x_centroid_for_force_z': list(x_centroid_for_force_z),
                'y_centroid_for_force_z': list(y_centroid_for_force_z),
                'z_centroid_for_force_z': list(z_centroid_for_force_z)}

    def buckling_factor(self) -> BucklingFactor:
        """Reports buckling factors obtained from buckling load cases. 
        
        :return: Buckling factors analysis results 
        :rtype: BucklingFactor
        """
        number_results = int()
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        factor = [float()]

        [ret, number_results, load_case,
         step_type, step_number, factor] = self.analysis_results.BucklingFactor(number_results, load_case,
                                                                                step_type, step_number, factor)
        handle(ret)
        return {'number_results': number_results,
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'factor': list(factor)}


    def frame_force(self, name, item_type_element: etabs.eItemTypeElm) -> FrameForce:
        """Reports the frame forces for specified line elements

        :param name: The name of an existing point object, point element, or group of objects depending on the value of the ItemTypeElm item
        :type name: str
        :param item_type_element: one of the following items in the `eItemTypeElm` enumeration.
            `ObjectElm` - the point element corresponding to the point object specified by the `name`
            `Element` - the point element specified by `name`
            `GroupElm` - all point elements directly or indirectly specified in the group specified by `name`
            `SelectionElm` - all point elements directly or indirectly selected and `name` is ignored
        :type item_type_element: etabs.eItemTypeElm
        :return: Frame force analysis results
        :rtype: FrameForce
        """

        number_results = int()
        object_name = [str()]
        object_station = [float()]
        element_name = [str()]
        element_station = [float()]
        load_case = [str()]
        step_type = [str()]
        step_number = [int()]
        axial_force = [float()]
        shear_2 = [float()]
        shear_3 = [float()]
        torsion = [float()]
        moment_2 = [float()]
        moment_3 = [float()]

        [ret, number_results, object_name, object_station, 
         element_name, element_station, load_case, step_type, 
         step_number, axial_force, shear_2, shear_3, torsion, 
                                        moment_2, moment_3] = self.analysis_results.FrameForce(name, item_type_element, number_results, object_name, object_station, 
                                                                                                element_name, element_station, load_case, step_type, 
                                                                                                step_number, axial_force, shear_2, shear_3, torsion, 
                                                                                                                                moment_2, moment_3)

        handle(ret)
        return {'number_results': number_results,
                'object_name': list(object_name),
                'object_station': list(object_station),
                'element_name': list(element_name),
                'element_station': list(element_station),
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'axial_force': list(axial_force),
                'shear_2': list(shear_2),
                'shear_3': list(shear_3),
                'torsion': list(torsion),
                'moment_2': list(moment_2),
                'moment_3': list(moment_3)}


    # TODO: FrameJointForce
    # TODO: GeneraliszeDispl
    # TODO: JointAcc
    # TODO: JointAccAbs

    def joint_displacement(self, name: str, item_type_element: etabs.eItemTypeElm) -> JointDisplacement:
        """Reports the joint displacements for the specified point elements.
        The displacements reported by this function are relative displacements.

        :param name: The name of an existing point object, point element, or group of objects depending on the value of the ItemTypeElm item
        :type name: str
        :param item_type_element: one of the following items in the `eItemTypeElm` enumeration.
            `ObjectElm` - the point element corresponding to the point object specified by the `name`
            `Element` - the point element specified by `name`
            `GroupElm` - all point elements directly or indirectly specified in the group specified by `name`
            `SelectionElm` - all point elements directly or indirectly selected and `name` is ignored
        :type item_type_element: etabs.eItemTypeElm
        :return: Joint Displacement analysis results 
        :rtype: JointDisplacement
        """
        number_results = int()
        object_name = [str()]
        element_name = [str()]
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        delta_1 = [float()]
        delta_2 = [float()]
        delta_3 = [float()]
        rotation_1 = [float()]
        rotation_2 = [float()]
        rotation_3 = [float()]

        [ret, number_results, object_name, element_name,
         load_case, step_type, step_number,
         delta_1, delta_2, delta_3,
         rotation_1, rotation_2, rotation_3] = self.analysis_results.JointDispl(name, item_type_element, number_results,
                                                                                object_name, element_name,
                                                                                load_case, step_type, step_number,
                                                                                delta_1, delta_2, delta_3,
                                                                                rotation_1, rotation_2, rotation_3)
        handle(ret)
        return {'number_results': number_results,
                'object_name': list(object_name),
                'element_name': list(element_name),
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'delta_1': list(delta_1),
                'delta_2': list(delta_2),
                'delta_3': list(delta_3),
                'rotation_1': list(rotation_1),
                'rotation_2': list(rotation_2),
                'rotation_3': list(rotation_3)}

    # TODO: JointDisplAbs
    # TODO: JointDrifts
    # TODO: JointReact
    # TODO: JointVel
    # TODO: JointVelAbs
    # TODO: LinkDeformation
    # TODO: LinkForce
    # TODO: LinkJointForce

    def modal_load_participation_ratios(self) -> ModalLoadParticipationRatios:
        """Reports the modal load participation ratios for each selected modal analysis case
        
        :return: Modal load participation ratios analysis results 
        :rtype: ModalLoadParticipationRatios
        """
        number_results = int()
        load_case = [str()]
        item_type = [str()]
        item = [str()]
        static_ratios = [float()]
        dynamic_ratios = [float()]

        [ret, number_results,
         load_case, item_type, item,
         static_ratios, dynamic_ratios] = self.analysis_results.ModalLoadParticipationRatios(number_results, load_case,
                                                                                             item_type, item,
                                                                                             static_ratios,
                                                                                             dynamic_ratios)
        handle(ret)
        return {'number_results': number_results,
                'load_case': list(load_case),
                'item_type': list(item_type),
                'item': list(item),
                'static_ratios': list(static_ratios),
                'dynamic_ratios': list(dynamic_ratios)}

    def modal_participating_mass_ratios(self) -> ModalParticipatingMassRatios:
        """Reports the modal participating mass ratios for each mode of each selected modal analysis case.
        
        :return: Modal participating mass ratios analysis results 
        :rtype: ModalParticipatingMassRatios
        """
        number_results = int()
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        period = [float()]
        delta_x = [float()]
        delta_y = [float()]
        delta_z = [float()]
        sum_delta_x = [float()]
        sum_delta_y = [float()]
        sum_delta_z = [float()]
        rotation_x = [float()]
        rotation_y = [float()]
        rotation_z = [float()]
        sum_rotation_x = [float()]
        sum_rotation_y = [float()]
        sum_rotation_z = [float()]

        [ret, number_results, load_case,
         step_type, step_number, period,
         delta_x, delta_y, delta_z,
         sum_delta_x, sum_delta_y, sum_delta_z,
         rotation_x, rotation_y, rotation_z,
         sum_rotation_x, sum_rotation_y, sum_rotation_z] = self.analysis_results.ModalParticipatingMassRatios(
            number_results, load_case,
            step_type, step_number, period,
            delta_x, delta_y, delta_z,
            sum_delta_x, sum_delta_y, sum_delta_z,
            rotation_x, rotation_y, rotation_z,
            sum_rotation_x, sum_rotation_y, sum_rotation_z)
        handle(ret)
        return {'number_results': number_results,
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'period': list(period),
                'delta_x': list(delta_x),
                'delta_y': list(delta_y),
                'delta_z': list(delta_z),
                'sum_delta_x': list(sum_delta_x),
                'sum_delta_y': list(sum_delta_y),
                'sum_delta_z': list(sum_delta_z),
                'rotation_x': list(rotation_x),
                'rotation_y': list(rotation_y),
                'rotation_z': list(rotation_z),
                'sum_rotation_x': list(sum_rotation_x),
                'sum_rotation_y': list(sum_rotation_y),
                'sum_rotation_z': list(sum_rotation_z)}

    def modal_participation_factors(self) -> ModalParticipationFactors:
        """Reports the modal participation factors for each mode of each selected modal analysis case.
        
        :return: Modal participation factors analysis results
        :rtype: ModalParticipationFactors
        """
        number_results = int()
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        period = [float()]
        delta_x = [float()]
        delta_y = [float()]
        delta_z = [float()]
        rotation_x = [float()]
        rotation_y = [float()]
        rotation_z = [float()]
        modal_mass = [float()]
        modal_stiff = [float()]

        [ret, number_results, load_case,
         step_type, step_number, period,
         delta_x, delta_y, delta_z,
         rotation_x, rotation_y, rotation_z,
         modal_mass, modal_stiff] = self.analysis_results.ModalParticipationFactors(number_results, load_case,
                                                                                    step_type, step_number, period,
                                                                                    delta_x, delta_y, delta_z,
                                                                                    rotation_x, rotation_y, rotation_z,
                                                                                    modal_mass, modal_stiff)
        handle(ret)
        return {'number_results': number_results,
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'period': list(period),
                'delta_x': list(delta_x),
                'delta_y': list(delta_y),
                'delta_z': list(delta_z),
                'rotation_x': list(rotation_x),
                'rotation_y': list(rotation_y),
                'rotation_z': list(rotation_z),
                'modal_mass': list(modal_mass),
                'modal_stiff': list(modal_stiff)}

    def modal_period(self) -> ModalPeriod:
        """Reports the modal period, cyclic frequency, circular frequency and eigenvalue for each selected modal load case.
        
        :return: Modal period analysis results
        :rtype: ModalPeriod
        """
        number_results = int()
        load_case = [str()]
        step_type = [str()]
        step_number = [int()]
        period = [float()]
        frequency = [float()]
        circular_frequency = [float()]
        eigen_value = [float()]

        [ret, number_results, load_case, step_type, step_number,
         period, frequency, circular_frequency, eigen_value] = self.analysis_results.ModalPeriod(number_results,
                                                                                                 load_case, step_type,
                                                                                                 step_number,
                                                                                                 period, frequency,
                                                                                                 circular_frequency,
                                                                                                 eigen_value)
        handle(ret)
        return {'number_results': number_results,
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'period': list(period),
                'frequency': list(frequency),
                'circular_frequency': list(circular_frequency),
                'eigen_value': list(eigen_value)}

    # TODO: ModalShape
    # TODO: PanelZoneDeformation
    # TODO: PanelZoneForce

    def pier_force(self) -> PierForce:
        """Retrieves pier forces for any defined pier objects in the model.
        
        :return: Pier force analysis results
        :rtype: PierForce
        """
        number_results = int()
        story_name = [str()]
        pier_name = [str()]
        load_case = [str()]
        location = [str()]
        axial = [float()]
        shear_2 = [float()]
        shear_3 = [float()]
        torsion = [float()]
        moment_2 = [float()]
        moment_3 = [float()]

        [ret, number_results, story_name, pier_name,
         load_case, location, axial, shear_2, shear_3,
         torsion, moment_2, moment_3] = self.analysis_results.PierForce(number_results, story_name, pier_name,
                                                                        load_case, location, axial, shear_2, shear_3,
                                                                        torsion, moment_2, moment_3)
        handle(ret)
        return {'number_results': number_results,
                'story_name': list(story_name),
                'pier_name': list(pier_name),
                'load_case': list(load_case),
                'location': list(location),
                'axial': list(axial),
                'shear_2': list(shear_2),
                'shear_3': list(shear_3),
                'torsion': list(torsion),
                'moment_2': list(moment_2),
                'moment_3': list(moment_3)}

    def section_cut_analysis(self) -> SectionCutAnalysis:
        """Reports the section cut force for sections cuts that are specified to have an analysis 
        (force_1, force_2, force_3, moment_1, moment_2, moment_3) result type.
        
        :return: section cut analysis results
        :rtype: SectionCutAnalysis
        """
        number_results = int()
        section_cut = [str()]
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        force_1 = [float()]
        force_2 = [float()]
        force_3 = [float()]
        moment_1 = [float()]
        moment_2 = [float()]
        moment_3 = [float()]

        [ret, number_results, section_cut,
         load_case, step_type, step_number,
         force_1, force_2, force_3,
         moment_1, moment_2, moment_3] = self.analysis_results.SectionCutAnalysis(number_results, section_cut,
                                                                                  load_case, step_type, step_number,
                                                                                  force_1, force_2, force_3,
                                                                                  moment_1, moment_2, moment_3)
        handle(ret)
        return {'number_results': number_results,
                'section_cut': list(section_cut),
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'force_1': list(force_1),
                'force_2': list(force_2),
                'force_3': list(force_3),
                'moment_1': list(moment_1),
                'moment_2': list(moment_2),
                'moment_3': list(moment_3)}

    def section_cut_design(self) -> SectionCutDesign:
        """Report the section cut force for sections cuts that are specified to have a design 
        (axial force, shear force 2, shear force 3, torsion, moment 2, moment 3) result type.
        
        :return: Section cut design results 
        :rtype: SectionCutDesign
        """
        number_results = int()
        section_cut = [str()]
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        axial = [float()]
        shear_2 = [float()]
        shear_3 = [float()]
        torsion = [float()]
        moment_2 = [float()]
        moment_3 = [float()]

        [ret, number_results, section_cut,
         load_case, step_type, step_number,
         axial, shear_2, shear_3,
         torsion, moment_2, moment_3] = self.analysis_results.SectionCutAnalysis(number_results, section_cut,
                                                                                 load_case, step_type, step_number,
                                                                                 axial, shear_2, shear_3,
                                                                                 torsion, moment_2, moment_3)
        handle(ret)
        return {'number_results': number_results,
                'section_cut': list(section_cut),
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'axial': list(axial),
                'shear_2': list(shear_2),
                'shear_3': list(shear_3),
                'torsion': list(torsion),
                'moment_2': list(moment_2),
                'moment_3': list(moment_3)}

    def spandrel_force(self) -> SpandrelForce:
        """Retrieves spandrel forces for any defined spandrel objects in the model.
        
        :return: Spandrel force analysis results 
        :rtype: SpandrelForce
        """
        number_results = int()
        story_name = [str()]
        spandrel_name = [str()]
        load_case = [str()]
        location = [str()]
        axial = [float()]
        shear_2 = [float()]
        shear_3 = [float()]
        torsion = [float()]
        moment_2 = [float()]
        moment_3 = [float()]

        [ret, number_results, story_name,
         spandrel_name, load_case, location,
         axial, shear_2, shear_3,
         torsion, moment_2, moment_3] = self.analysis_results.SpandrelForce(number_results, story_name,
                                                                            spandrel_name, load_case, location,
                                                                            axial, shear_2, shear_3,
                                                                            torsion, moment_2, moment_3)
        handle(ret)
        return {'number_results': number_results,
                'story_name': list(story_name),
                'spandrel_name': list(spandrel_name),
                'load_case': list(load_case),
                'location': list(location),
                'axial': list(axial),
                'shear_2': list(shear_2),
                'shear_3': list(shear_3),
                'torsion': list(torsion),
                'moment_2': list(moment_2),
                'moment_3': list(moment_3)}

    def story_drifts(self) -> StoryDrift:
        """Reports the story drifts.
        
        :return: Story drifts analysis results 
        :rtype: StoryDrift
        """
        number_results = int()
        story = [str()]
        load_case = [str()]
        step_type = [str()]
        step_number = [float()]
        direction = [str()]
        drift = [float()]
        label = [str()]
        delta_x = [float()]
        delta_y = [float()]
        delta_z = [float()]

        [ret, number_results, story, load_case,
         step_type, step_number,
         direction, drift, label,
         delta_x, delta_y, delta_z] = self.analysis_results.StoryDrifts(number_results, story, load_case,
                                                                        step_type, step_number,
                                                                        direction, drift, label,
                                                                        delta_x, delta_y, delta_z)
        handle(ret)
        return {'number_results': number_results,
                'story': list(story),
                'load_case': list(load_case),
                'step_type': list(step_type),
                'step_number': list(step_number),
                'direction': list(direction),
                'drift': list(drift),
                'label': list(label),
                'delta_x': list(delta_x),
                'delta_y': list(delta_y),
                'delta_z': list(delta_z)}
