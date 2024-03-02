# PyTABS - ETABS .NET API python wrapper
# PropMaterial - cPropMaterial interface
__all__ = ['PropMaterial']

# import ETABS namespace and pyTABS error handler


# import custom enumerations


# import typing


class PropMaterial:
    """PropMaterial interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropMaterial interface
        self.prop_material = etabs.cPropMaterial(sap_model.PropMaterial)

        # relate relevant ETABS enumerations
        self.eMatType = etabs.eMatType
        """EtabsModel `MatType` enumeration"""

        # relate custom enumerations
