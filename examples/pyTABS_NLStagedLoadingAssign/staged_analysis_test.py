# pyTABS Example: NLStagedAnalysisSet
# Sam Cubis
VERSION = '230202'

from datetime import datetime
from src import pytabs

# workbook mock caller
# WB_FN = os.path.join(os.path.dirname(__file__), 'GroupAssignmentBatchMaster.xlsm')

NOW = datetime.now()


def main():

    model_fp = r'C:\Dev\PyTabs ETABs Example Model\Model.EDB'
    model_is_open = 'YES'
    #Assigning Stages
    print('Assigning Stages in ETABs')

    staged_lc_create(model_fp, model_is_open)

    print('\Assignment complete, press any key to exit.')
    input('')


def staged_lc_create(model_fp, model_is_open):
    
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

    #TODO - Add Content for Load_Case Adding Based on Pattern Inputs. 
    case_title = "Test3"
    story_list = ["GROUND", "Story1", 'Story2', 'Story3', 'Story4', 'Story5', 'Story6']
    story_durations = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    
    output_condition = [True]* len(story_list)
    output_stage_name = [x + '_out' for x in story_list]
    output_comments = ['']* len(story_list)
    etabs_model.load_cases.static_nonlinear_staged.set_case(case_title)
    etabs_model.load_cases.static_nonlinear_staged.set_stage_definitions(case_title, len(story_list), story_durations, output_condition, output_stage_name, output_comments)

    # for i, story in enumerate(story_list):

    etabs_model.load_cases.static_nonlinear_staged.set_stage_data(case_title, 1, 1, 
                                                            [etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.ADD_STRUCTURE],
                                                            [etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP], 
                                                            ['Story5_Wall'],
                                                            [float(69)],
                                                            [etabs_model.load_cases.static_nonlinear_staged.eStageMyType.NONE],
                                                            [''],
                                                            [float(0)])
    # etabs_model.cases.static_nonlinear_staged.set_stage_data(case_title, 2, 2,
    #                                                         [etabs_model.cases.static_nonlinear_staged.eStageOperationType.ADD_STRUCTURE, None],
    #                                                         [etabs_model.cases.static_nonlinear_staged.eStageObjectType.GROUP, None],
    #                                                         ['Story6_Wall', ''],
    #                                                         [float(69), 0.0],
    #                                                         [etabs_model.cases.static_nonlinear_staged.eStageMyType.NONE, etabs_model.cases.static_nonlinear_staged.eStageMyType.NONE],
    #                                                         ['', ''],
    #                                                         [float(1), 1.0])

    etabs_model.load_cases.static_nonlinear_staged.set_stage_data(case_title, 2, 2, 
                                                            [etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.ADD_STRUCTURE,etabs_model.load_cases.static_nonlinear_staged.eStageOperationType.LOAD_NEW],
                                                            [etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP,etabs_model.load_cases.static_nonlinear_staged.eStageObjectType.GROUP], 
                                                            ['Story7_Wall', 'All'],
                                                            [float(69), 0.0],
                                                            [etabs_model.load_cases.static_nonlinear_staged.eStageMyType.NONE, etabs_model.load_cases.static_nonlinear_staged.eStageMyType.LOAD],
                                                            ['', 'Dead'],
                                                            [float(1), 1.0])
    # exit ETABS if not attached
    if not model_is_open:
        etabs_model.exit_application()




if __name__ == "__main__":
    # xw.Book(WB_FN).set_mock_caller()
    main()