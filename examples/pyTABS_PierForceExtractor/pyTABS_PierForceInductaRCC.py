# pyTABS Example: Pier Force Extractor
# Mitchell Tesch
VERSION = '231115'

# Library imports
import os
import pytabs
import xlwings as xw
import csv
import  datetime


# workbook mock caller
WB_FN = os.path.join(os.path.dirname(__file__), 'pyTABS_PierForceExtractorInductaRCC.xlsm')

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
RESULTS_DECIMALS = 2
# Run start date and time for last run output
NOW = datetime.datetime.now().strftime('%x %X')


def main():
    print('--------------------------------------------------------------')
    print('pyTABS - Pier Force Extractor for Inducta RCC')
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
    etabs_model = pytabs.EtabsModel(attach_to_instance=model_is_open, model_path=model_fp)
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
    etabs_model.analysis_results_setup.deselect_all_cases_combos_for_output()
    available_cases = etabs_model.load_cases.get_name_list()
    available_combos = etabs_model.combo.get_name_list()
    error_target_case_combo = []
    selected_cases = []
    selected_combos = []
    for case_combo in target_cases_combos:
        if case_combo in available_cases:
            etabs_model.analysis_results_setup.set_case_selected_for_output(case_combo)
            selected_cases.append(case_combo)
        elif case_combo in available_combos:
            etabs_model.analysis_results_setup.set_combo_selected_for_output(case_combo)
            selected_combos.append(case_combo)
        else:
            error_target_case_combo.append(case_combo)
    if len(error_target_case_combo):
        print(f"\t> {len(error_target_case_combo)} cases/combos not found {', '.join(error_target_case_combo)}")
    
    # get pier forces
    print("\nExtracting and cleaning pier forces.")
    pier_forces = etabs_model.analysis_results.pier_force()
    # clean pier forces
    pier_forces_dict = {}
    for _r in range(0, pier_forces['number_results'], 2):
        story_name = pier_forces['story_name'][_r]
        if story_name not in target_stories:
            continue
        pier_name = pier_forces['pier_name'][_r]
        if pier_name not in target_piers:
            continue
        if pier_name not in pier_forces_dict:
            pier_forces_dict[pier_name] = []
        
        current_pier_props = target_pier_properties[pier_name]
        story_index = current_pier_props['story_name'].index(story_name)
        theta = round(current_pier_props['axis_angle'][story_index], 2)
        load_case = pier_forces['load_case'][_r]
        load_case_id = pier_forces['load_case'][_r].split(":")[0]

        pier_forces_dict[pier_name].append({"Tile": f"{pier_name}_{story_name}_{load_case_id}",
                                            "Story": story_name,
                                            "LoadCase": load_case,
                                            "Theta": theta,
                                            "N*top": pier_forces['axial'][_r],
                                            "N*bot": pier_forces['axial'][_r+1],
                                            "Mx*top": pier_forces['moment_2'][_r],
                                            "Mx*bot": pier_forces['moment_2'][_r+1],
                                            "My*top": pier_forces['moment_3'][_r],
                                            "My*bot": pier_forces['moment_3'][_r+1],
                                            "Vx*top": pier_forces['shear_2'][_r],
                                            "Vx*bot": pier_forces['shear_2'][_r+1],
                                            "Vy*top": pier_forces['shear_3'][_r],
                                            "Vy*bot": pier_forces['shear_3'][_r+1],
                                            })
    # write results back into workbook
    print("\nWriting pier force csv files")
    write_result_data(wb, pier_forces_dict)
    # exit ETABS if not attached
    if not model_is_open:
        etabs_model.exit_application()

    print('\nExtraction run complete, press any key to exit.')
    input('')


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
    # set workbook back to automatic calculation and save
    wb.app.calculation = 'automatic'
    wb.save()
    return model_fp, model_is_open, target_piers, target_stories, target_cases_combos


def write_result_data(wb : xw.Book, pier_forces_df):
    working_folder = os.path.dirname(__file__)
    for pier, results in pier_forces_df.items():
        headers = results[0].keys()
        file_path = os.path.join(working_folder, f"{pier}.csv")
        with open(file_path, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, headers)
            dict_writer.writeheader()
            dict_writer.writerows(results)
    # write last run data
    wb.sheets[INPUT_SHEET].range(LAST_RUN_RANGE).value = NOW


if __name__ == '__main__':
    # mock caller configured for run from development environment
    xw.Book(WB_FN).set_mock_caller()
    main()