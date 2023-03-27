# Development Environment Configuration
# required for those working within the development repository
import sys, os
# import of pytabs package via examples context
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from context import pytabs 
# workbook mock caller
WB_FN = os.path.join(os.path.dirname(__file__), 'pyTABS_TowerPrelimVerification.xlsm')

# Library imports
import xlwings as xl
import pandas as pd
from datetime import datetime

NOW = datetime.now()

from pytabs.model import *

# Testing the Modal Results 
from context import pytabs
import pytabs.model

# Modal workbook configuration 
WB_MODAL_IN_SHEET = 'Main'

WB_HEADER_IN_RANGE = {'job_number': 'B2',
                    'project': 'B3',
                    'element': 'B4',
                    'designer': 'B5',
                    'date': 'B6',
                    'notes': 'B7',
                    'model_fp':'B13',
                    'model_open': 'B14',
                    'joint_displacement_case' : 'B17',
                    'joint_label' : 'B16'} 

WB_RUNS_IN_RANGE = 'O31:AA31'
WB_MODAL_RESULTS_OUT = 'O31'

def extract_input_data (Joint_displacemnt_wb : xl.Book) : 
    """extract all inputs from pyTABS_TowerPrelimVerification.xlsm
    
    Args: 
        wb (xl.Book): xlwings workbook object 
        
    Returns: 
        _type_ : input data 
    """
    input_sheet = Joint_displacemnt_wb.sheets[WB_MODAL_IN_SHEET]


    # Defining the header input as values 
    header_input = {}
    for key, range in WB_HEADER_IN_RANGE.items():
        header_input[key] = input_sheet.range(range).value

    return header_input  


def write_batch_results(batch_wb : xl.Book, run_results):
    input_sheet = batch_wb.sheets[WB_MODAL_IN_SHEET]
    input_sheet.range(WB_MODAL_RESULTS_OUT).expand('down').clear_contents()
    input_sheet.range(WB_MODAL_RESULTS_OUT).options(expand = '', transpose = False).value = run_results



def joint_displacement_data (model_fp, model_is_open): 

    """
    Write the joint displacement data back into pyTABS_TowerPrelimVerification.xlsmThe 
    
    Args: 
        joint_displacement_wb (xw.Book): xlwings workbook object
        joint_displacement_df (Pandas.DataFrame): joint displacement results dataframe
    """

# substantiate pyTABS EtabsModel
    etabs_model = pytabs.model.EtabsModel(model_is_open, model_fp)
# set the model units to 
    etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)

    if not model_is_open: 
        etabs_model.exit_application()

    # The GetStoryName function is within story.py 
    story_name = etabs_model.story.get_name_list()
    

    # The GetNameFromLabel function is within group.py 
    label = '167'
    joint = []

    for story in story_name : 
        point_name = etabs_model.point_obj.get_name_from_label(label, story)
        joint.append(point_name)
        

    # Selecting the load Cases 
    deselect = etabs_model.analysis_results.deselect_all_cases_combos_for_output()
    print(deselect)
    joint_displacement_case = 'AW-X-0deg-NegT- 0.9G+Auto'
    load = etabs_model.analysis_results.set_combo_selected_for_output(joint_displacement_case, True)
    print(load)

    # Joint Displacement 
    # sustantiating Joint Displacement from analysis results in Etabs Model
    joint_displacement_dataframe = []

    for j in joint:
        joint_displacements = etabs_model.analysis_results.joint_displacement(j, item_type_element= etabs_model.eItemTypeElm.Element)
        joint_displacement_dataframe.append(joint_displacements)
        

    # Generating a Joint Displacement dataframe from Etabs values 
    joint_displacement_df = pd.DataFrame(joint_displacement_dataframe)
    print(joint_displacement_df)
    return joint_displacement_df
    


def main(): 
    print('Reading model period input...', end='')
    
    # extract input data from workbook 
    joint_displacement_wb = xl.Book.caller() 
    header_input = extract_input_data(joint_displacement_wb)

    model_fp = header_input['model_fp']
    model_is_open = header_input['model_open']
    
    

    # check if model is open 
    if model_is_open.lower() == 'yes' : 
        model_is_open = True 
    else : 
        model_is_open = False 

    # if model open set no model path 
    if model_is_open: 
        model_fp = ''
        print('\nAttching to open ETABS instance.')
    else: 
        print(f"\nOpening ETABS model: {model_fp}.")

    #Model Periods 
    print('Getting joint displacement results...')
    results = joint_displacement_data(model_fp, model_is_open)

    print('\nWriting to excel...', end='')

    print('Returning joint displacement results...')
    write_batch_results(joint_displacement_wb, results)

    print('Assignment complete, press any key to exit.')
    input('')


if __name__=="__main__" :
    # mock caller configured for run from development environement 
    xl.Book(WB_FN).set_mock_caller()
    main()
