# pyTABS Frame/Shell Spandrel Assigner
# Samuel Cubis
VERSION = '230110'
from cProfile import label
from tokenize import group
from context import pytabs
# Library imports
import xlwings as xw
import pandas as pd
import  datetime
import pytabs.model


model_fp = r''


def main():
    print('--------------------------------------------------------------')
    print('pyTABS - Frame/Shell Spandrel Assigner')
    print('Samuel Cubis')
    print(f'Version {VERSION}')
    print('--------------------------------------------------------------\n')

    target_stories = ['Story5']

    print(f"Number of target stories: {len(target_stories)}")
    
    model_is_open = "yes"
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
    
    # get pier section properties
    print("\nSetting Frames and Shell Spandrel Assignments")
    error_target_story = []
    target_frame_names = {}
    target_area_names = {}

    for story_label in target_stories:
        stories = etabs_model.story.get_name_list()
        
        if story_label in stories:
            target_frame_names[story_label] = etabs_model.frame.get_name_list_on_story(story_label)
            target_area_names[story_label] = etabs_model.area.get_name_list_on_story(story_label)
            
        else: 
            error_target_story.append(story_label)

    print(f"\t> {len(target_frame_names.keys())} storys found: {', '.join(target_frame_names.keys())}")
    if len(error_target_story):
        print(f"\t> {len(error_target_story)} storys not found: {', '.join(error_target_story)}")

    for story, frames in target_frame_names.items():
        group_name = story+"_Frame"
        etabs_model.group.set_group_1(group_name)
        for frame_id in frames:
            etabs_model.frame.set_group(frame_id, group_name)

    for story, areas in target_area_names.items():
        for shell_id in areas:
            label = etabs_model.area.get_label_from_name(shell_id)
            if 'W' in label:
                group_name = story+"_Wall"
                etabs_model.group.set_group_1(group_name)
                etabs_model.area.set_group(shell_id, group_name)

            if 'F' in label:
                group_name = story+"_Floor"
                etabs_model.group.set_group_1(group_name)
                etabs_model.area.set_group(shell_id, group_name)


if __name__ == '__main__':
    main()