# PyTABS - ETABS .NET API python wrapper
# PropFrame - cPropFrame interface
__all__ = ['PropFrame']

# import ETABS namespace and pyTABS error handler


# import custom enumerations


# import typing


class PropFrame:
    """PropFrame interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropFrame interface
        self.prop_frame = etabs.cPropFrame(sap_model.PropFrame)

        # relate relevant ETABS enumerations
        self.eFramePropType = etabs.eFramePropType
        """EtabsModel `FramePropType` enumeration"""

        # relate custom enumerations
