# PyTABS - ETABS .NET API python wrapper
# PropRebar - cPropRebar interface
__all__ = ['PropRebar']

# import ETABS namespace and pyTABS error handler


# import custom enumerations


# import typing


class PropRebar:
    """PropRebar interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropRebar interface
        self.prop_rebar = etabs.cPropRebar(sap_model.PropRebar)

        # relate custom enumerations
