
# pyTABS Example: GroupAssigner
# Sam Cubis
VERSION = '230202'

import os
import pytabs
import xlwings as xw
from datetime import datetime


# workbook mock caller
WB_FN = os.path.join(os.path.dirname(__file__), 'GroupAssignmentBatchMaster.xlsm')

NOW = datetime.now()

# MOCK_WB_FP = 'SpreadsheetBatchMaster.xlsm'

# batch workbook configuration
WB_BATCH_IN_SHEET = 'Main'

WB_HEADER_IN_RANGE = {'job_number': 'B2',
                      'project': 'B3',
                      'element': 'B4',
                      'designer': 'B5',
                      'date': 'B6',
                      'notes': 'B7',
                      'model_fp':'B8',
                      'model_open': 'B9'}

WB_RUNS_IN_RANGE = 'A13:E13'


WB_BATCH_RESULTS_OUT = 'A14'


def read_batch_input(batch_wb : xw.Book):
    input_sheet = batch_wb.sheets[WB_BATCH_IN_SHEET]
    # read header information
    header_input = {}
    for key, range in WB_HEADER_IN_RANGE.items():
        header_input[key] = input_sheet.range(range).value
    
    batch_runs_input =  input_sheet.range(WB_RUNS_IN_RANGE).options(empty='', expand='down').value
    batch_runs_headers = batch_runs_input[0]
    batch_runs_data = batch_runs_input[1:]
    
    return header_input, batch_runs_headers, batch_runs_data 

def group_assign(run_data, model_fp, model_is_open):
    
    """
    The main function of the script that sets the frames and shell assignments for target stories.
    
    """

    # Check if the model is open
    if model_is_open.lower() == 'yes':
        model_is_open = True
    else:
        model_is_open = False

    # if model open set no model path
    if model_is_open:
        model_fp = ''
        print('\nAttaching to open ETABS instance.')
    else:
        print(f"\nOpening ETABS model: {model_fp}.")
    
    # substantiate pyTABS EtabsModel
    etabs_model = pytabs.EtabsModel(attach_to_instance=model_is_open, model_path=model_fp)
    
    # set the model units to 
    etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)

    print(f"Number of target stories: {len(run_data)}")

    # Lists to store error stories and target frame and area names
    error_target_story = []
    target_frame_names = {}
    target_area_names = {}

    for conditions in run_data:
        #get stories and condition data 
        story_label = conditions[0]
        column_condition = conditions[1]
        beam_condition = conditions[2]
        wall_condition = conditions[3]
        floor_condition = conditions[4]

        # Get a list of all stories in the model
        stories = etabs_model.story.get_name_list()

        # Loop through target stories
        if story_label in stories:

            # Get the list of frame names on the target story
            target_frame_names[story_label] = etabs_model.frame_obj.get_name_list_on_story(story_label)
            
            # Get the list of area names on the target story
            target_area_names[story_label] = etabs_model.area_obj.get_name_list_on_story(story_label)
            
        else: 
            # Add the story to the error list if it's not found
            error_target_story.append(story_label)

        print(f'\t> Story: {story_label} .....')
        #set groups for frame elements. 
        for story, frames in target_frame_names.items():

            #add each frame element to Group
            for frame_id in frames:
                #get typeddict
                label = etabs_model.frame_obj.get_label_from_name(frame_id)
                #check if Column or Beam/brace element based on Label.            
                if 'C' in label['frame_label'] and column_condition == "YES":
                    #create label in Etabs Model. (if not yet existing)
                    group_name = story+"_Column"
                    #set Column frame to group. 
                    etabs_model.group.set_group_1(group_name)
                    etabs_model.frame_obj.set_group_assign(frame_id, group_name)

                if 'B' in label['frame_label'] and beam_condition == "YES":
                    #create label in Etabs Model. (if not yet existing)
                    group_name = story+"_Beam"
                    #set beam/frame frame to group. 
                    etabs_model.group.set_group_1(group_name)
                    etabs_model.frame_obj.set_group_assign(frame_id, group_name)
        print(f'\t> Frames: Assigned.....')

        #set groups for shell/area elements. 
        for story, areas in target_area_names.items():
            for shell_id in areas:
                #get typeddict
                label = etabs_model.area_obj.get_label_from_name(shell_id)
                #check if Wall or Floor element based on Label. 
                if 'W' in label['area_label'] and wall_condition == "YES":
                    #create label in Etabs Model. (if not yet existing)
                    group_name = story+"_Wall"
                    etabs_model.group.set_group_1(group_name)
                    #set wall shell to group. 
                    etabs_model.area_obj.set_group_assign(shell_id, group_name)

                if 'F' in label['area_label'] and floor_condition == "YES":
                    #create label in Etabs Model. (if not yet existing)
                    group_name = story+"_Floor"
                    etabs_model.group.set_group_1(group_name)
                    #set floor shell to group. 
                    etabs_model.area_obj.set_group_assign(shell_id, group_name)
        print(f'\t> Shells: Assigned.....')

    # exit ETABS if not attached
    if not model_is_open:
        etabs_model.exit_application()


def main():
    print('Reading batching input...', end='')
    batch_wb = xw.Book.caller()

    header_input, batch_runs_headers, batch_runs_data = read_batch_input(batch_wb)
    
    model_fp = header_input['model_fp']
    model_is_open = header_input['model_open']
    print(f'\t>done.')
    
    #Assigning Groups
    print('Assigning Groups in ETABs')
    group_assign(batch_runs_data, model_fp, model_is_open )

    print('Assignment complete, press any key to exit.')
    input('')

if __name__ == "__main__":
    xw.Book(WB_FN).set_mock_caller()
    main()