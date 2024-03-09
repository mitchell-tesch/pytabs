# PyTABS - ETABS .NET API python wrapper
# DatabaseTables - cDatabaseTables interface
__all__ = ['DatabaseTables']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations


class DatabaseTables:
    """DatabaseTables interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create DatabaseTables interface
        self.database_tables = etabs.cDatabaseTables(sap_model.DatabaseTables)

        # relate custom enumerations
