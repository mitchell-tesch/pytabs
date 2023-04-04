from context import pytabs

import pytabs.model

from pytabs.error_handle import handle

# substantiate pyTABS EtabsModel
etabs_model = pytabs.model.EtabsModel()
# set the model units to kN, m and C.
etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)

# test methods