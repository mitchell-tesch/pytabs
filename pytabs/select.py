# pyTABS - ETABS .NET API python wrapper
# Select - cSelect
__all__ = ['Select']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import *
from pytabs.error_handle import *

# import custom enumerations
from pytabs.enumerations import eSelectObjectType


# import typing
from typing import TypedDict

class SelectedObjects(TypedDict):
    """TypedDict class for get_selected return"""
    number_items : int
    object_types : list[eSelectObjectType]
    object_names : list[str]


class Select:
    """Select interface"""
    def __init__(self, sap_model : etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create SelectObj interface
        self.select = etabs.cSelect(sap_model.SelectObj)
        
        # relate custom enumerations
        self.eSelectObjectType = eSelectObjectType


    def all(self, deselect : bool = False) -> None:
        """Selects or deselects all objects in the model.

        :param deselect: `False` if objects are to be selected and `True` if they are to be deselected, defaults to False
        :type deselect: bool, optional
        """
        handle(self.select.All(deselect))


    def clear_selection(self) -> None:
        """Deselects all objects in the model.
        """
        handle(self.select.ClearSelection())


    def get_selected(self) -> SelectedObjects:
        """Retrieves a list of selected objects.

        :return: Quantity, Type and Names of the selected objects
        :rtype: `SelectedObjects`
        """
        number_items = int()
        object_types = [int()]
        object_names = [str()]
        [ret, number_items, object_types, object_names] = self.select.GetSelected(number_items, object_types, object_names)
        handle(ret)
        return {'number_items': number_items,
                'object_types': [eSelectObjectType(o) for o in object_types],
                'object_names': list(object_names)}


    def group(self, name : str, deselect : bool = False) -> None:
        """Selects or deselects all objects in the specified group.

        :param name: The name of an existing group
        :type name: str
        :param deselect: `False` if objects are to be selected and `True` if they are to be deselected, defaults to False
        :type deselect: bool, optional
        """
        handle(self.select.Group(name, deselect))


    def invert_selection(self) -> None:
        """Deselects all selected objects and selects all unselected objects; that is, it inverts the selection.
        """
        handle(self.select.InvertSelection())


    def previous_selection(self) -> None:
        """Restores the previous selection.
        """
        handle(self.select.PreviousSelection())