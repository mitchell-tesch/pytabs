# PyTABS - ETABS .NET API python wrapper
# DatabaseTables - cDatabaseTables interface
__all__ = ['DatabaseTables']

# import ETABS namespace and pyTABS error handler
from .etabs_config import etabs
from .error_handle import handle

# import custom enumerations
from .enumerations import eTableImportableType

# import typing
from typing import TypedDict


class DbEditLog(TypedDict):
    num_fatal_errors: int
    num_error_msgs: int
    num_warn_msgs: int
    num_info_msgs: int
    import_log: str
    

class DbField:
    def __init__(self, field_key: str, field_name: str,
                 description: str, units_string: str, is_importable: bool):
        self._field_key = field_key
        self._field_name = field_name
        self._description = description
        self._units_string = units_string
        self._is_importable = is_importable

    @property
    def field_key(self):
        return self._field_key

    @property
    def field_name(self):
        return self._field_name

    @property
    def description (self):
        return self._description

    @property
    def units_string(self):
        return self._units_string

    @property
    def is_importable(self):
        return self._is_importable


class DbTable:
    def __init__(self, table_key: str, table_name: str, importable_type: eTableImportableType,
                 is_empty: bool):
        self._table_key = table_key
        self._table_name = table_name
        self._importable_type = importable_type
        self._is_empty = is_empty
        self._fields: list[DbField] = []
 
    @property
    def table_key(self):
        return self._table_key

    @property
    def table_name(self):
        return self._table_name

    @property
    def importable_type(self):
        return self._importable_type

    @property
    def is_empty(self):
        return self._is_empty

    @property
    def fields(self):
        return self._fields

    def add_table_fields(self, fields: DbField):
        self._fields.extend(fields)


class DbTableDataArray:
    def __init__(self, table_version: int, fields_included: list[str], number_records: int,
                 records: list[str], group_name: str = ''):
        self._table_version = table_version
        self._fields_included = fields_included
        self._group_name = group_name
        self._num_fields = len(self._fields_included)
        self._num_records = number_records
        self._table_data = self._reshape_data(records)
        
    @property
    def table_version(self):
        return self._table_version
    
    @property
    def fields_included(self):
        return self._fields_included
    
    @property
    def group_name(self):
        return self._group_name
    
    @property
    def table_data(self):
        return self._table_data

    def _reshape_data(self, records):
        return list(zip(*[iter(records)] * self._num_fields))


class DatabaseTables:
    """DatabaseTables interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create DatabaseTables interface
        self.database_tables = etabs.cDatabaseTables(sap_model.DatabaseTables)

        # relate custom enumerations
        self.eTableImportableType = eTableImportableType

    def get_all_table_details(self) -> list[DbTable]:
        number_tables, table_key, table_name, is_importable, is_empty = self._get_all_tables()
        tables: list[DbTable] = []
        for _t in range(number_tables):
            table = DbTable(table_key[_t], table_name[_t], eTableImportableType(is_importable[_t]), is_empty[_t])
            fields = self.get_table_fields(table_key[_t])
            table.add_table_fields(fields)
            tables.append(table)
        return tables

    def get_table_details(self, key) -> DbTable:
        number_tables, table_key, table_name, is_importable, is_empty = self._get_all_tables()
        for _t in range(number_tables):
            table = DbTable(table_key[_t], table_name[_t], eTableImportableType(is_importable[_t]), is_empty[_t])
            if key == table_key[_t]:
                fields = self.get_table_fields(table_key[_t])
                table.add_table_fields(fields)
                return table

    def get_table_fields(self, table_key) -> list[DbField]:
        table_version = int()
        number_fields = int()
        field_key = [str()]
        field_name = [str()]
        description = [str()]
        units_string = [str()]
        is_importable = [bool()]
        [ret, _table_version, number_fields,
         field_key, field_name, description,
         units_string, is_importable] = self.database_tables.GetAllFieldsInTable(table_key, table_version, number_fields,
                                                                                 field_key, field_name, description,
                                                                                 units_string, is_importable)
        handle(ret)
        fields: list[DbField] = []
        for _f in range(number_fields):
            fields.append(DbField(field_key[_f], field_name[_f], description[_f], units_string[_f], is_importable[_f]))
        return fields

    def get_table_data_array(self, table: DbTable, edit_mode: bool = False,
                             group_name: str = '', field_key: list[str] = ['']):
        table_version = int()
        field_keys_out = [str()]
        number_records = int()
        records = [str()]
        if edit_mode:
            # not active in current version of ETABS - refer manual.
            group_name = ''
            [ret, table_version, field_keys_out,
             number_records, records] = self.database_tables.GetTableForEditingArray(table.table_key, group_name,
                                                                                     table_version, field_keys_out,
                                                                                     number_records, records)
            handle(ret)
            return DbTableDataArray(table_version, list(field_keys_out), number_records, records)
             
        else:
            [ret, field_key, table_version,
             field_keys_out, number_records,
             records] = self.database_tables.GetTableForDisplayArray(table.table_key, field_key, group_name,
                                                                     table_version, field_keys_out, number_records,
                                                                     records)
            handle(ret)
            return DbTableDataArray(table_version, list(field_keys_out), number_records, records, group_name)

    def set_table_data_array_edit(self, table: DbTable, field_keys: list[str], table_data: list[list]) -> None:
        table_version = int()
        num_records = len(table(table_data))
        records = [item for record in table_data for item in record]
        [ret, _table_version, 
         _field_keys_out, _table_data] = self.database_tables.SetTableForEditingArray(table.table_key, table_version,
                                                                                      field_keys, num_records, records)
         handle(ret)

    def apply_table_edits(self, log_import: bool = False) -> DbEditLog:
        num_fatal_errors = int()
        num_error_msgs = int()
        num_warn_msgs = int()
        num_info_msgs = int()
        import_log = str()
        handle(self.database_tables.ApplyEditedTables(log_import, num_fatal_errors, num_error_msgs,
                                                      num_warn_msgs, num_info_msgs,
                                                      import_log))
        return {'num_fatal_errors': num_fatal_errors,
                'num_error_msgs': num_error_msgs,
                'num_warn_msgs': num_warn_msgs,
                'num_info_msgs': num_info_msgs,
                'import_log': import_log}
    
    def discard_table_edits(self):
        handle(self.database_tables.CancelTableEditing())
    
    def _get_all_tables(self):
        number_tables = int()
        table_key = [str()]
        table_name = [str()]
        is_importable = [int()]
        is_empty = [bool()]
        [ret, number_tables, table_key,
         table_name, is_importable, is_empty] = self.database_tables.GetAllTables(number_tables, table_key,
                                                                                  table_name, is_importable, is_empty)
        handle(ret)
        return number_tables, table_key, table_name, is_importable, is_empty
