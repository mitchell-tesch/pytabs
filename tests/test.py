from pytabs.model import *

# substantiate pyTABS EtabsModel
etabs_model = EtabsModel()
# set the model units to 
etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)


story_list = etabs_model.story.get_name_list()

print(story_list)
