# pyTABS Example: GroupAssigner
# Sam Cubis
VERSION = '230202'

import os
import xlwings as xw
from datetime import datetime
from src import pytabs

# workbook mock caller
WB_FN = os.path.join(os.path.dirname(__file__), 'NLStagedLCBulkSpreadsheet.xlsm')

NOW = datetime.now()

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

WB_RUNS_IN_RANGE = 'B41:R41'



WB_BATCH_RESULTS_OUT = 'A42'
WB_LOAD_PATTERN_RESULTS_OUT = 'J11'


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

def write_batch_results(batch_wb : xw.Book, run_results, load_patterns):
    input_sheet = batch_wb.sheets[WB_BATCH_IN_SHEET]
    input_sheet.range(WB_BATCH_RESULTS_OUT).expand('down').clear_contents()
    input_sheet.range(WB_BATCH_RESULTS_OUT).options(expand='down', transpose = True).value = run_results
    input_sheet.range(WB_LOAD_PATTERN_RESULTS_OUT).expand('down').clear_contents()
    input_sheet.range(WB_LOAD_PATTERN_RESULTS_OUT).options(expand='down', transpose = True).value = load_patterns


def main():
    print('Reading batching input...', end='')
    batch_wb = xw.Book.caller()
    header_input, batch_runs_headers, batch_runs_data = read_batch_input(batch_wb)
    print('done.')
    
    model_fp = header_input['model_fp']
    model_is_open = header_input['model_open']

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

    #get stories
    stories = etabs_model.story.get_name_list()
    stories_reversed = stories.reverse()

    #get load patterns
    load_patterns = etabs_model.load_patterns.get_name_list()

    # exit ETABS if not attached
    if not model_is_open:
        etabs_model.exit_application()

    print(f"Number of target stories imported: {len(stories)}")

    print('\nWriting to excel...', end='')

    write_batch_results(batch_wb, stories, load_patterns)
    
    print('done.')
    
    print('\nExtraction run complete, press any key to exit.')
    input('')


if __name__ == "__main__":
    xw.Book(WB_FN).set_mock_caller()
    main()