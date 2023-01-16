# pyTABS Frame/Shell Spandrel Assigner
# Samuel Cubis
VERSION = '230110'
from context import pytabs
import pytabs.model


# Library imports
import xlwings as xw
import pandas as pd
import  datetime

model_fp = r''


def main():
    """
    The main function of the script that sets the frames and shell assignments for target stories.
    
    """

    print('--------------------------------------------------------------')
    print('pyTABS - Frame/Shell Spandrel Assigner')
    print('Samuel Cubis')
    print(f'Version {VERSION}')
    print('--------------------------------------------------------------\n')
    
    # List of target stories
    target_stories = ['Story5'] #TODO - Hardcoded Levels, fix this. Add option for Target Stories or ALL. 

    print(f"Number of target stories: {len(target_stories)}")
    
    model_is_open = "yes" #TODO - Hardcoded model is open, fix this. Compare to example file 

    # Check if the model is open
    if model_is_open.lower() == 'yes':
        model_is_open = True

    # if model open set no model path
    if model_is_open:
        model_fp = ''
        print('\nAttaching to open ETABS instance.')
    else:
        print(f"\nOpening ETABS model: {model_fp}.")
    
    # substantiate pyTABS EtabsModel
    etabs_model = pytabs.model.EtabsModel(attach_to_instance=model_is_open, model_path=model_fp)
    
    # set the model units to 
    etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)

    #begin setting assignments
    print("\nSetting Frames and Shell Spandrel Assignments")

    # Lists to store error stories and target frame and area names
    error_target_story = []
    target_frame_names = {}
    target_area_names = {}

    # Loop through target stories
    for story_label in target_stories:

        # Get a list of all stories in the model
        stories = etabs_model.story.get_name_list()
        
        # Check if the target story is in the list of stories
        if story_label in stories:
            # Get the list of frame names on the target story
            target_frame_names[story_label] = etabs_model.frame_obj.get_name_list_on_story(story_label)
            
            # Get the list of area names on the target story
            target_area_names[story_label] = etabs_model.area_obj.get_name_list_on_story(story_label)
            
        else: 
            # Add the story to the error list if it's not found
            error_target_story.append(story_label)

    print(f"\t> {len(target_frame_names.keys())} storys found: {', '.join(target_frame_names.keys())}")
    if len(error_target_story):
        print(f"\t> {len(error_target_story)} storys not found: {', '.join(error_target_story)}")

    #set groups for frame elements. 
    for story, frames in target_frame_names.items():

        #add each frame element to Group
        for frame_id in frames:
            #get typeddict
            label = etabs_model.frame_obj.get_label_from_name(frame_id)
            #check if Column or Beam/brace element based on Label.            
            if 'C' in label['frame_label']:
                #create label in Etabs Model. (if not yet existing)
                group_name = story+"_Column"
                #set Column frame to group. 
                etabs_model.group.set_group_1(group_name)
                etabs_model.frame_obj.set_group_assign(frame_id, group_name)

            if 'B' in label['frame_label']:
                #create label in Etabs Model. (if not yet existing)
                group_name = story+"_Beam"
                #set beam/frame frame to group. 
                etabs_model.group.set_group_1(group_name)
                etabs_model.frame_obj.set_group_assign(frame_id, group_name)

    #set groups for shell/area elements. 
    for story, areas in target_area_names.items():
        for shell_id in areas:
            #get typeddict
            label = etabs_model.area_obj.get_label_from_name(shell_id)
            #check if Wall or Floor element based on Label. 
            if 'W' in label['area_label']:
                #create label in Etabs Model. (if not yet existing)
                group_name = story+"_Wall"
                etabs_model.group.set_group_1(group_name)
                #set wall shell to group. 
                etabs_model.area_obj.set_group_assign(shell_id, group_name)

            if 'F' in label['area_label']:
                #create label in Etabs Model. (if not yet existing)
                group_name = story+"_Floor"
                etabs_model.group.set_group_1(group_name)
                #set floor shell to group. 
                etabs_model.area_obj.set_group_assign(shell_id, group_name)


if __name__ == '__main__':
    main()