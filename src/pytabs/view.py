# PyTABS - ETABS .NET API python wrapper
# View - cView interface
__all__ = ['View']

# import ETABS namespace and pyTABS error handler
from .etabs_config import *
from .error_handle import *

# import custom enumerations


class View:
    """View interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create View interface
        self.view = etabs.cView(sap_model.View)

    def refresh_view(self, window: int = 0, zoom: bool = True) -> None:
        """Refreshes the view for the specified window(s).

        :param window: window number, with 0 for all windows, defaults to 0
        :type window: int, optional
        :param zoom: `True` to maintain window current zoom level, `False` to reset window zoom level to default, defaults to True
        :type zoom: bool, optional
        """
        handle(self.view.RefreshView(window, zoom))

    # RefreshWindow method redundant with the above.
