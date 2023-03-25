# pyTABS - ETABS .NET API python wrapper
# DatabaseTables - cDatabaseTables
__all__ = ['DatabaseTables']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations


# import typing


class DatabaseTables:
    """DatabaseTables interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create DatabaseTables interface
        self.database_tables = etabs.cDatabaseTables(sap_model.DatabaseTables)
        
        # relate custom enumerations