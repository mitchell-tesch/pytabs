# pyTABS Example: Pier Force Extractor
# Mitchell Tesch
VERSION = '221204'

# Development Environment Configuration
# required for those working within the development repository
import sys, os
# import of pytabs package via examples context
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from context import pytabs
# workbook mock caller
WB_FN = os.path.join(os.path.dirname(__file__), 'pyTABS_PierForceExtractor.xlsm')

# Library imports
import xlwings as xw
import pandas as pd
import  datetime
from pytabs.model import *

# Constants
# Workbook Input sheet configuration
INPUT_SHEET = 'Input'
MODEL_FP_RANGE = 'B2'
MODEL_IS_OPEN_RANGE = 'B3'
LAST_RUN_RANGE = 'B4'
PIERS_RANGE = 'A6'
STORIES_RANGE = 'B6'
CASES_COMBOS_RANGE = 'C6'
# Workbook RawResults sheet configuration
RAW_RESULTS_SHEET = 'RawResults'
RAW_RESULTS_RANGE = 'A4'
# Workbook Pier summary sheet template configuration
PIER_RESULTS_SHEET = '_PierTemplate'
PIER_RESULTS_RANGE = 'A3'
# Rounding of pier forces - number of decimals
RESULTS_DECIMALS = 0
# Run start date and time for last run output
NOW = datetime.datetime.now().strftime('%x %X')


def extract_input_data(wb : xw.Book):
    """extract all inputs from pyTABS_PierForceExtractor.xlsm

    Args:
        wb (xw.Book): xlwings workbook object

    Returns:
        _type_: input data
    """
    wb.app.calculation = 'manual'
    input_sheet = wb.sheets[INPUT_SHEET]
    
    # read model file path
    model_fp = input_sheet.range(MODEL_FP_RANGE).value
    
    # read model is open setting
    model_is_open = input_sheet.range(MODEL_IS_OPEN_RANGE).value
    if model_is_open.lower() == 'yes':
        model_is_open = True
    else:
        model_is_open = False
    
    # read target piers
    target_piers = input_sheet.range(PIERS_RANGE).options(expand='down').value
    
    # read target stories
    target_stories = input_sheet.range(STORIES_RANGE).options(expand='down').value
    
    # read target piers
    target_cases_combos = input_sheet.range(CASES_COMBOS_RANGE).options(expand='down').value
    
    return model_fp, model_is_open, target_piers, target_stories, target_cases_combos


def write_result_data(wb : xw.Book, pier_forces_df, pier_summary_dfs):
    """write pier force data back into pyTABS_PierForceExtractor.xlsm

    Args:
        wb (xw.Book): xlwings workbook object
        pier_forces_df (Pandas.DataFrame): pier force results dataframe
        pier_summary_dfs (dict(Pandas.DataFrame)): pier wise summary dataframe
    """
    wb.app.screen_updating = False
    # write raw pier force data
    raw_sheet = wb.sheets[RAW_RESULTS_SHEET]
    raw_sheet.range(RAW_RESULTS_RANGE).expand('table').clear_contents()
    raw_sheet.range(RAW_RESULTS_RANGE).options(index=False, header=False).value = pier_forces_df
    
    # delete previous summary sheets
    for sheet in wb.sheets:
        if 'Pier_' in sheet.name:
            sheet.delete()
    
    # copy template sheet and write pier summary data
    template_sheet = wb.sheets[PIER_RESULTS_SHEET]
    for pier, summary_df in pier_summary_dfs.items():
        pier_sheet = template_sheet.copy(before=template_sheet, name=f"Pier_{pier}")
        if pier[:2] == 'SW':
            pier_sheet.range('A1').value = f"{pier} SHORING WALL LOADING SCHEDULE"
        else:
            pier_sheet.range('A1').value = f"{pier} BARRETTE LOADING SCHEDULE"
        pier_sheet.range(PIER_RESULTS_RANGE).options(index=False, header=False).value = summary_df
        pier_sheet.visible = True
        
    # write last run data
    wb.sheets[INPUT_SHEET].range(LAST_RUN_RANGE).value = NOW
    
    # set workbook back to automatic calculation and save
    raw_sheet.activate()
    wb.app.screen_updating = True
    wb.app.calculation = 'automatic'
    wb.save()


def main():
    print('--------------------------------------------------------------')
    print('pyTABS - Pier Force Extractor')
    print('Mitchell Tesch')
    print(f'Version {VERSION}')
    print('--------------------------------------------------------------\n')
    # extract input data from workbook
    wb = xw.Book.caller()
    model_fp, model_is_open, target_piers, target_stories, target_cases_combos = extract_input_data(wb)
    print(f"Number of target piers: {len(target_piers)}")
    print(f"Number of target stories: {len(target_stories)}")
    print(f"Number of target cases/combos: {len(target_cases_combos)}")

    # if model open set no model path
    if model_is_open:
        model_fp = ''
        print('\nAttaching to open ETABS instance.')
    else:
        print(f"\nOpening ETABS model: {model_fp}.")
    # substantiate pyTABS EtabsModel
    etabs_model = EtabsModel(attach_to_instance=model_is_open, model_path=model_fp)
    # set the model units to 
    etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)
    
    # get pier section properties
    print("\nExtracting pier section properties.")
    error_target_piers = []
    target_pier_properties = {}
    for pier_label in target_piers:
        pier_exists = etabs_model.pier_label.get_pier(pier_label)
        if pier_exists:
            target_pier_properties[pier_label] = etabs_model.pier_label.get_section_properties(pier_label)
        else:
            error_target_piers.append(pier_label)
    print(f"\t> {len(target_pier_properties.keys())} piers found: {', '.join(target_pier_properties.keys())}")
    if len(error_target_piers):
        print(f"\t> {len(error_target_piers)} piers not found: {', '.join(error_target_piers)}")
    
    # set-up results cases / combos for extraction
    print("\nConfiguring analysis results extraction.")
    etabs_model.analysis_results.deselect_all_cases_combos_for_output()
    available_cases = etabs_model.load_cases.get_name_list()
    available_combos = etabs_model.resp_combo.get_name_list()
    error_target_case_combo = []
    selected_cases = []
    selected_combos = []
    for case_combo in target_cases_combos:
        if case_combo in available_cases:
            etabs_model.analysis_results.set_case_selected_for_output(case_combo)
            selected_cases.append(case_combo)
        elif case_combo in available_combos:
            etabs_model.analysis_results.set_combo_selected_for_output(case_combo)
            selected_combos.append(case_combo)
        else:
            error_target_case_combo.append(case_combo)
    if len(error_target_case_combo):
        print(f"\t> {len(error_target_case_combo)} cases/combos not found {', '.join(error_target_case_combo)}")
    
    # get pier forces
    print("\nExtracting and cleaning pier forces.")
    pier_forces = etabs_model.analysis_results.pier_force()
    # clean pier forces
    pier_forces_df = pd.DataFrame()
    for _r, story_name in enumerate(pier_forces['story_name']):
        if story_name not in target_stories:
            continue
        pier_name = pier_forces['pier_name'][_r]
        if pier_name not in target_piers:
            continue
        try:
            pier_properties = target_pier_properties[pier_name]
            theta = pier_properties['axis_angle'][pier_properties['story_name'].index(story_name)]
        except ValueError:
            continue
        row_df = pd.DataFrame([{'id': pier_name,
                               'story': story_name,
                               'theta': round(theta, 1),
                               'case': pier_forces['load_case'][_r],
                               'location': pier_forces['location'][_r],
                               'p': round(pier_forces['p'][_r], RESULTS_DECIMALS),
                               'v2': round(pier_forces['v2'][_r], RESULTS_DECIMALS),
                               'v3': round(pier_forces['v3'][_r], RESULTS_DECIMALS),
                               't': round(pier_forces['t'][_r], RESULTS_DECIMALS),
                               'm2': round(pier_forces['m2'][_r], RESULTS_DECIMALS),
                               'm3': round(pier_forces['m3'][_r], RESULTS_DECIMALS)}])
        pier_forces_df = pd.concat([pier_forces_df, row_df], ignore_index=True)
    
    # create a set of unique piers for summary ie. grouping of shoring wall panels
    summary_target_piers = set()
    for pier in target_pier_properties:
        if pier[:2] == 'SW':
            summary_target_piers.add(pier.split('-')[0])
        else:
            summary_target_piers.add(pier)
    summary_target_piers = sorted(summary_target_piers)
    
    # create summary data frames for each pier
    print("\nCreating summary force tables for each pier.")
    pier_summary_dfs = {}
    for _p, pier in enumerate(summary_target_piers):
        print(f"\t> Pier {_p+1}/{len(summary_target_piers)} - {pier}\r")
        pier_summary_df = pd.DataFrame()
        for case in target_cases_combos:
            filtered_df = pier_forces_df.loc[(pier_forces_df.id.str.startswith(pier)) & (pier_forces_df.case == case)]
            header_df = pd.DataFrame({'id': [pier, pier],
                                      'theta': [filtered_df.theta.iloc[0], filtered_df.theta.iloc[0]],
                                      'case': [case, case],
                                      'envelope': ['Min', 'Max']})
            actions_df = filtered_df[['p','v2', 'v3', 't', 'm2', 'm3']]
            filtered_summary_df = pd.concat([actions_df .min(numeric_only=True).to_frame().T,
                                             actions_df .max(numeric_only=True).to_frame().T], ignore_index=True)
            filtered_summary_df = pd.concat([header_df, filtered_summary_df], axis=1)
            pier_summary_df = pd.concat([pier_summary_df, filtered_summary_df], ignore_index=True)
        pier_summary_dfs[pier] = pier_summary_df
    
    # write results back into workbook
    print("\nWriting pier forces back into workbook")
    write_result_data(wb, pier_forces_df, pier_summary_dfs)
    
    # exit ETABS if not attached
    if not model_is_open:
        etabs_model.exit_application()
    
    print('\nExtraction run complete, press any key to exit.')
    input('')


if __name__ == '__main__':
    # mock caller configured for run from development environment
    xw.Book(WB_FN).set_mock_caller()
    main()