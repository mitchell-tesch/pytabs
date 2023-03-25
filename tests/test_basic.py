from context import pytabs

import pytabs.model

from pytabs.error_handle import handle

# substantiate pyTABS EtabsModel
etabs_model = pytabs.model.EtabsModel()
# set the model units to 
etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)

# frame_added = etabs_model.frame_obj.add_by_coord(0.0, 8.0, 3.0, 8.0, 0.0, 3.0)
# print(frame_added)

# frame_added = etabs_model.frame_obj.add_by_point("65", "53")
# print(frame_added)

handle(0)

frame_groups = etabs_model.frame_obj.get_group_assign("37")
print(frame_groups)

frame_GUID = etabs_model.frame_obj.get_GUID("37")
print(frame_GUID)

frame_design_procedure = etabs_model.frame_obj.get_design_procedure("37")
print(frame_design_procedure)

frame_design_orientation = etabs_model.frame_obj.get_design_orientation("37")
print(frame_design_orientation)


frame_design_orientation = etabs_model.frame_obj.add_by_coord(1,2,3,10,20,30)
