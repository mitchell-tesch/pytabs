import pytabs


def main():
    etabs_model = pytabs.EtabsModel()

    etabs_model.analysis_results_setup.deselect_all_cases_combos_for_output()

    combos = etabs_model.combo.get_name_list()
    # select all combos
    for combo in combos:
        etabs_model.analysis_results_setup.set_combo_selected_for_output(combo)
    # check selection of combos
    for combo in combos:
        check_status = etabs_model.analysis_results_setup.get_combo_selected_for_output(combo)
        print(check_status)

    # get beam design forces
    beam_design_forces = etabs_model.design_results.beam_design_forces('541', etabs_model.eItemType.Objects)

if __name__ == "__main__":
    main()
