# PyTABS - ETABS .NET API python wrapper
# PropLink - cPropLink interface
__all__ = ['PropLink']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import etabs
from pytabs.error_handle import handle

# import custom enumerations
from pytabs.enumerations import eLinkDof, eLinkHysteresisType

# import typing


class PropLink:
    """PropLink interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropLink interface
        self.prop_link = etabs.cPropLink(sap_model.PropLink)

        # relate relevant ETABS enumerations
        self.eLinkPropType = etabs.eLinkPropType
        """EtabsModel `LinkPropType` enumeration"""

        # relate custom enumerations
        self.eLinkDof = eLinkDof
        self.eLinkHysteresisType = eLinkHysteresisType

    def get_name_list(self, link_type: etabs.eLinkPropType = None) -> list[str]:
        _number_names = int()
        link_names = [str()]
        if link_type:
            [ret, _number_names, link_names] = self.prop_link.GetNameList(_number_names, link_names, link_type)
        else:
            [ret, _number_names, link_names] = self.prop_link.GetNameList(_number_names, link_names)
        handle(ret)
        return list(link_names)

    def set_linear(
        self,
        name: str,
        dof: list[bool],
        is_fixed: list[bool],
        ke: list[float],
        ce: list[float],
        dj2: float,
        dj3: float,
        ke_is_coupled: bool = False,
        ce_is_coupled: bool = False,
        notes: str = '',
        guid: str = '',
    ) -> None:
        [ret, _dof, _is_fixed, _ke, _ce] = self.prop_link.SetLinear(
            name,
            dof,
            is_fixed,
            ke,
            ce,
            dj2,
            dj3,
            ke_is_coupled,
            ce_is_coupled,
            notes,
            guid,
        )
        handle(ret)

    def set_multi_linear_elastic(
        self,
        name: str,
        dof: list[bool],
        is_fixed: list[bool],
        nonlinear: list[bool],
        ke: list[float],
        ce: list[float],
        dj2: float,
        dj3: float,
        notes: str = '',
        guid: str = '',
    ) -> None:
        [ret, _dof, _is_fixed, _nonlinear, _ke, _ce] = self.prop_link.SetMultiLinearElastic(
            name, dof, is_fixed, nonlinear, ke, ce, dj2, dj3, notes, guid
        )
        handle(ret)

    def set_multi_linear_plastic(
        self,
        name: str,
        dof: list[bool],
        is_fixed: list[bool],
        nonlinear: list[bool],
        ke: list[float],
        ce: list[float],
        dj2: float,
        dj3: float,
        notes: str = '',
        guid: str = '',
    ) -> None:
        [ret, _dof, _is_fixed, _nonlinear, _ke, _ce] = self.prop_link.SetMultiLinearPlastic(
            name, dof, is_fixed, nonlinear, ke, ce, dj2, dj3, notes, guid
        )
        handle(ret)

    def set_multi_linear_points(
        self,
        name,
        dof: eLinkDof,
        action_values: list[float],
        displacement_values: list[float],
        hysteresis_type: eLinkHysteresisType = eLinkHysteresisType.KINEMATIC,
        alpha_1: int = 0,
        alpha_2: int = 0,
        beta_1: int = 0,
        beta_2: int = 0,
        eta: int = 0,
    ) -> None:
        number_points = min(len(action_values), len(displacement_values))
        [ret, _action_values, _displacement_values] = self.prop_link.SetMultiLinearPoints(
            name,
            dof.value,
            number_points,
            action_values,
            displacement_values,
            hysteresis_type.value,
            alpha_1,
            alpha_2,
            beta_1,
            beta_2,
            eta,
        )
        handle(ret)

    def set_spring_data(self, name, length: float, area: float) -> None:
        handle(self.prop_link.SetSpringData(name, length, area))
