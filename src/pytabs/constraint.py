# PyTABS - ETABS .NET API python wrapper
# Constraint - cConstraint interface
__all__ = ['Constraint']

# import ETABS namespace and pyTABS error handler
from .etabs_config import *
from .error_handle import *

# import custom enumerations


class Constraint:
    """Constraint interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create Constraint interface
        self.constraint = etabs.cConstraint(sap_model.ConstraintDef)

        # relate relevant ETABS enumerations
        self.eConstraintAxis = etabs.eConstraintAxis
        """EtabsModel `ConstraintAxis` enumeration"""
        self.eConstraintType = etabs.eConstraintType
        """EtabsModel `ConstraintType` enumeration"""

        # relate custom enumerations
