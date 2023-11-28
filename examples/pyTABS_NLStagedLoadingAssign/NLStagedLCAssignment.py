# pyTABS Example: GroupAssigner
# Sam Cubis
VERSION = '230202'

import os
import xlwings as xw
from datetime import datetime
import pytabs

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
                      'model_open': 'B9',
                      'sw_lp': 'B22',
                      'sdl_lp': 'B23',
                      'll_red_lp': 'B24',
                      'll_unred_lp': 'B25',
                      'facade_lp': 'B26'}

WB_RUNS_IN_RANGE = 'B41:Z41'


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

def staged_lc_create(headers, run_data, model_fp, model_is_open, load_patterns):
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

    sw_lp = load_patterns[0]
    sdl_lp = load_patterns[1]
    ll_red_lp = load_patterns[2]
    ll_unred_lp = load_patterns[3]
    facade_lp = load_patterns[4]

    #TODO - Add Content for Load_Case Adding Based on Pattern Inputs
    stage_list = []
    story_durations = []

    for stage_id in run_data:
        stage_list.append(stage_id[0])

    for durations in run_data:
        story_durations.append(durations[2])
    

    output_condition = [True]* len(stage_list)
    output_stage_name = [x for x in stage_list]
    output_comments = ['']* len(stage_list)

    #create load case with generic name
    etabs_model.load_cases.static_nonlinear_staged.set_case("pyTabs- GeneratedNLStagedLC")

    #set up all stages
    etabs_model.load_cases.static_nonlinear_staged.set_stage_definitions("pyTabs- GeneratedNLStagedLC", len(stage_list), story_durations, output_condition, output_stage_name, output_comments)
   
    #add operations for each stage

    for _stage in run_data:

        story_id = _stage[0]
        stage_number = _stage[1]
        stage_time = _stage[2]
        type_wall = _stage[3]
        name_wall = _stage[4]
        age_wall = _stage[5]
        type_floor = _stage[6]
        name_floor = _stage[7]
        age_floor = _stage[8]
        type_beam = _stage[9]
        name_beam = _stage[10]
        age_beam = _stage[11]
        type_col = _stage[12]
        name_col = _stage[13]
        age_col = _stage[14]
        add_sw = _stage[15]
        fact_sw = _stage[16]
        add_facade = _stage[17]
        fact_facade = _stage[18]
        add_sdl = _stage[19]
        fact_sdl = _stage[20]
        add_ll_red = _stage[21]
        fact_ll_red = _stage[22]
        add_ll_unred = _stage[23]
        fact_ll_unred = _stage[24]
        
        # create blank list to ammend total operations. 
        operations = []
        
        op_type = [] # I.e. Group. 

        op_name = []

        op_age = []

        op_load_type = []

        op_load_name = []

        op_scale_factor = []
        
        # add structure - WALL
        if name_wall != '':
            operations.append(etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.ADD_STRUCTURE)
            if type_wall == "Group":
                op_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP)
            op_age.append(age_wall)
            op_name.append(name_wall)
            op_load_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageMyType.NONE)
            op_load_name.append('')
            op_scale_factor.append(1.0)

        # add structure - Floor
        if name_floor != '':
            operations.append(etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.ADD_STRUCTURE)
            if type_floor == "Group":
                op_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP)
            op_age.append(age_floor)
            op_name.append(name_floor)
            op_load_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageMyType.NONE)
            op_load_name.append('')
            op_scale_factor.append(1.0)

        # add structure - Beam
        if name_beam != '':
            operations.append(etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.ADD_STRUCTURE)
            if type_beam == "Group":
                op_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP)
            op_age.append(age_beam)
            op_name.append(name_beam)
            op_load_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageMyType.NONE)
            op_load_name.append('')
            op_scale_factor.append(1.0)

        # add structure - Column
        if name_col != '':
            operations.append(etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.ADD_STRUCTURE)
            if type_col == "Group":
                op_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP)
            op_age.append(age_col)
            op_name.append(name_col)
            op_load_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageMyType.NONE)
            op_load_name.append('')
            op_scale_factor.append(1.0)

        # add load - SW
        if add_sw == 'IF_ADDED':
            operations.append(etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.LOAD_NEW)
            op_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP)
            op_age.append(0.0)
            op_name.append("All")
            op_load_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageMyType.LOAD)
            op_load_name.append(sw_lp)
            op_scale_factor.append(fact_sw)

        # add load - Facade
        if add_facade != '':
            operations.append(etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.LOAD_ALL)
            op_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP)
            op_age.append(0.0)
            op_name.append(add_facade)
            op_load_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageMyType.LOAD)
            op_load_name.append(facade_lp)
            op_scale_factor.append(fact_facade)

        # add load - SDL
        if add_sdl != '':
            operations.append(etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.LOAD_ALL)
            op_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP)
            op_age.append(0.0)
            op_name.append(add_sdl)
            op_load_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageMyType.LOAD)
            op_load_name.append(sdl_lp)
            op_scale_factor.append(fact_sdl)

        # add load - LL_Red
        if add_ll_red != '':
            operations.append(etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.LOAD_ALL)
            op_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP)
            op_age.append(0.0)
            op_name.append(add_ll_red)
            op_load_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageMyType.LOAD)
            op_load_name.append(ll_red_lp)
            op_scale_factor.append(fact_ll_red)

        # add load - LL_Red
        if add_ll_unred != '':
            operations.append(etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.LOAD_ALL)
            op_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP)
            op_age.append(0.0)
            op_name.append(add_ll_unred)
            op_load_type.append(etabs_model.load_cases.static_nonlinear_staged.eStageMyType.LOAD)
            op_load_name.append(ll_unred_lp)
            op_scale_factor.append(fact_ll_unred)

        number_ops = len(operations)

        etabs_model.load_cases.static_nonlinear_staged.set_stage_data("pyTabs- GeneratedNLStagedLC", int(stage_number), int(number_ops), operations, op_type, 
                                                                op_name, op_age, op_load_type, op_load_name, op_scale_factor)
        print("Stage "+ str(stage_number) + " complete..."  )      


    # exit ETABS if not attached
    if not model_is_open:
        etabs_model.exit_application()

    return None


def main():
    print('Reading batching input...', end='')
    batch_wb = xw.Book.caller()

    header_input, batch_runs_headers, batch_runs_data = read_batch_input(batch_wb)
    
    model_fp = header_input['model_fp']
    model_is_open = header_input['model_open']
    load_patterns = [header_input['sw_lp'], header_input['sdl_lp'], header_input['ll_red_lp'], 
                     header_input['ll_unred_lp'], header_input['facade_lp']]
    
    print('done.')
    
    #Assigning Groups
    print('Assigning Groups in ETABs')
    staged_lc_create(batch_runs_headers, batch_runs_data, model_fp, model_is_open, load_patterns)

    print('\Assignment complete, press any key to exit.')
    input('')

if __name__ == "__main__":
    xw.Book(WB_FN).set_mock_caller()
    main()