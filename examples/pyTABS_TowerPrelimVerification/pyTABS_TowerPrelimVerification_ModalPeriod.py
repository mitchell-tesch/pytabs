# Development Environment Configuration
# required for those working within the development repository
import sys, os
# import of pytabs package via examples context
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from context import pytabs
# workbook mock caller
WB_FN = os.path.join(os.path.dirname(__file__), 'PyTABS_TowerPrelimVerification.xlsm')

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
                    'model_fp':'B8',
                    'model_open': 'B9',
                    'modal_case' : 'B10'}

WB_RUNS_IN_RANGE = 'A14:F14'
WB_MODAL_RESULTS_OUT = 'O15'

def extract_input_data (modal_period_wb : xl.Book) : 
    """extract all inputs from pyTABS_TowerPrelimVerification.xlsm
    
    Args: 
        wb (xw.Book): xlwings workbook object 
        
    Returns: 
        _type_ : input data 
    """
    input_sheet = modal_period_wb.sheets[WB_MODAL_IN_SHEET]


    # Defining the header input as values 
    header_input = {}
    for key, range in WB_HEADER_IN_RANGE.items():
        header_input[key] = input_sheet.range(range).value

    return header_input  


def write_batch_results(batch_wb : xl.Book, run_results):
    input_sheet = batch_wb.sheets[WB_MODAL_IN_SHEET]
    input_sheet.range(WB_MODAL_RESULTS_OUT).expand('down').clear_contents()
    input_sheet.range(WB_MODAL_RESULTS_OUT).options(expand = '', transpose = False).value = run_results


def modal_period_results_data (model_fp, model_is_open, modal_case): 

    """
    Write the modal period data back into pyTABS_TowerPrelimVerification.xlsmThe 
    
    Args: 
        wb (xw.Book): xlwings workbook object
        modal_period_df (Pandas.DataFrame): modal period results dataframe
        modal_period_df2 (dict(Pandas.DataFrame)): first 5 row of modal period results dataframe
    """
    
    # substantiate pyTABS EtabsModel
    etabs_model = pytabs.model.EtabsModel(model_is_open, model_fp)
    # set the model units to 
    etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)

    if not model_is_open: 
        etabs_model.exit_application()

    # Deselecting the cases 
    etabs_model.analysis_results.deselect_all_cases_combos_for_output()
    
    #Selecting the Modal case 
    etabs_model.analysis_results.set_case_selected_for_output(modal_case, True)

    # Modal Period 
    # sustantiating modal period from analysis results in Etabs Model 
    modal_periods = etabs_model.analysis_results.modal_period()

    # Generating a modal period dataframe from Etabs values 
    modal_period_df = pd.DataFrame(modal_periods)

    # get first five mode shapes. 
    modal_period_df_2 = modal_period_df.drop(range(5, len(modal_period_df.index.to_list())))
    return modal_period_df_2


def main(): 
    print('Reading model period input...', end='')
    
    # extract input data from workbook 
    model_period_wb = xl.Book.caller() 
    header_input = extract_input_data(model_period_wb)

    model_fp = header_input['model_fp']
    model_is_open = header_input['model_open']
    modal_case = header_input['modal_case']

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
    print('Getting modal results...')
    results = modal_period_results_data(model_fp, model_is_open, modal_case)
    # results = 'hello'

    print('\nWriting to excel...', end='')

    print('Returning modal results...')
    write_batch_results(model_period_wb, results)

    print('Assignment complete, press any key to exit.')
    input('')


if __name__=="__main__" :
    # mock caller configured for run from development environement 
    xl.Book(WB_FN).set_mock_caller()
    main()










