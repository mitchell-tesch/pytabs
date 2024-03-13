import pytabs
import xlwings as xw
import excel_index as wb_index

UNIDIRECTIONAL_SUFFIX = 'U'
BIDIRECTIONAL_SUFFIX = 'B'
CORNER_SUFFIX = 'C'

TRIB_LENGTH = 1.2
TRIB_AREA = 1.2






def main():
    input_data = extract_excel_inputs()
    
    # substantiate pyTABS EtabsModel
    etabs_model = pytabs.EtabsModel()
    # set model units
    # etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)
    
    for prop_data in input_data:
        prop_base_name = prop_data['name']
        
        prop_set = [{'name': f'{prop_base_name}_{UNIDIRECTIONAL_SUFFIX}',
                     'dof': [False, False, True, False, False, False],
                     'ml_axes': [etabs_model.property.link.eLinkDof.U3],
                     'force_values': [0.] + prop_data['force_values'],
                     'delta_values': [-.0001] + prop_data['delta_values'],
                     },
                    {'name': f'{prop_base_name}_{BIDIRECTIONAL_SUFFIX}',
                     'dof': [False, False, True, False, False, False],
                     'ml_axes': [etabs_model.property.link.eLinkDof.U3],
                     'force_values': uni_to_bidirectional(prop_data['force_values']),
                     'delta_values': uni_to_bidirectional(prop_data['delta_values']),
                    },
                    {'name': f'{prop_base_name}_{UNIDIRECTIONAL_SUFFIX}_{CORNER_SUFFIX}',
                     'dof': [False, True, True, False, False, False],
                     'ml_axes': [etabs_model.property.link.eLinkDof.U2,
                                 etabs_model.property.link.eLinkDof.U3],
                     'force_values': [0.] + prop_data['force_values'],
                     'delta_values': [-.0001] + prop_data['delta_values'],
                    },
                    {'name': f'{prop_base_name}_{BIDIRECTIONAL_SUFFIX}_{CORNER_SUFFIX}',
                     'dof': [False, True, True, False, False, False],
                     'ml_axes': [etabs_model.property.link.eLinkDof.U2,
                                 etabs_model.property.link.eLinkDof.U3],
                     'force_values': uni_to_bidirectional(prop_data['force_values']),
                     'delta_values': uni_to_bidirectional(prop_data['delta_values']),
                    },
                    ]
 
        # create each property in the prop set
        for prop in prop_set:
            # create multi linear elastic link property
            etabs_model.property.link.set_multi_linear_elastic(name=prop['name'],
                                                               dof=prop['dof'],
                                                               is_fixed=[False, False, False, False, False, False],
                                                               nonlinear=prop['dof'],
                                                               ke=[0., 0., 0., 0., 0., 0.],
                                                               ce=[0., 0., 0., 0., 0., 0.],
                                                               dj2=0., dj3=0.)
            
            # provide spring data to link property
            etabs_model.property.link.set_spring_data(name=prop['name'], length=TRIB_LENGTH, area=TRIB_AREA)
            
            # populate multi linear points data to link property for each axis
            for axis in prop['ml_axes']:
                etabs_model.property.link.set_multi_linear_points(name=prop['name'],
                                                                  dof=axis,
                                                                  action_values=prop['force_values'],
                                                                  displacement_values=prop['delta_values'])

            # create line spring property for link assignment
            etabs_model.property.line_spring.set_line_spring_prop(name=prop['name'],
                                                                  stiffness=[0., 0., 0., 0.],
                                                                  nonlinear_option_2=etabs_model.property.line_spring.eSpringNonlinearOption.LINEAR,
                                                                  nonlinear_option_3=etabs_model.property.line_spring.eSpringNonlinearOption.LINEAR)
        
    # get database table for link to line spring association
    db_line_spring_table = etabs_model.database_tables.get_table_details('Spring Property Definitions - Line Springs')
    
    # get table data array for edit
    table_array = etabs_model.database_tables.get_table_data_array(table=db_line_spring_table, edit_mode=True)
    
    # edit table data array for all PW properties
    new_table_data = []
    for record in table_array.table_data:
        new_record = list(record)
        if record[0].startswith('PW'):
            new_record[1] = 'Link'  
            new_record[8] = record[0]
        new_table_data.append(new_record)

    # write data
    etabs_model.database_tables.set_table_data_array_edit(table=db_line_spring_table,
                                                          field_keys=table_array.fields_included,
                                                          table_data=new_table_data)
    
    # apply data write
    db_edit_log = etabs_model.database_tables.apply_table_edits(True)
    print(db_edit_log['import_log'])
    etabs_model.database_tables.discard_table_edits()
    print('')

def uni_to_bidirectional(values):
    return [-v for v in values][:0:-1] + values

def extract_excel_inputs():
    wb = xw.Book(wb_index.WB_FILE)
    sheet = wb.sheets(wb_index.WB_SHEET)
    input_data = []
    for table_name, start_cell in wb_index.TABLE_RANGES.items():
        raw_data = sheet.range(start_cell).options(expand = 'table').value
        delta_values = []
        force_values = []
        for delta, force in raw_data:
            delta_values.append(round(delta, 6))
            force_values.append(round(force, 6))
        input_data.append({'name': table_name,
                           'delta_values': delta_values,
                           'force_values': force_values})
    return input_data


if __name__ == '__main__':
    main()