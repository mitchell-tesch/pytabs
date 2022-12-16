from context import pytabs




# substantiate pyTABS EtabsModel
etabs_model = pytabs.EtabsModel()
# set the model units to 
etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)


story_list = etabs_model.story.get_name_list()

for story in story_list:
    elevation = etabs_model.story.get_elevation(story_name=story)
    height = etabs_model.story.get_height(story_name=story)
    status = etabs_model.story.get_master_story(story_name=story)
    similar_story = etabs_model.story.get_similar_to(story_name=story)
    
    print(f"{story} | {height} | {elevation} |  {status} | {similar_story}")
    
    