import pytabs



def main():
    # substantiate pyTABS EtabsModel
    etabs_model = pytabs.EtabsModel()
    
    # etabs_model.set_present_units(etabs_model.eUnits.kN_m_C)
    
    # etabs_model.property.link.set_multi_linear_elastic(name='TestLinkProp',
    #                                                    dof=[True, False, False, False, False, False],
    #                                                    is_fixed=[False, True, False, False, False, False],
    #                                                    nonlinear=[True, False, False, False, False, False],
    #                                                    ke=[0., 0., 0., 0., 0., 0.],
    #                                                    ce=[0., 0., 0., 0., 0., 0.],
    #                                                    dj2=100., dj3=200.)
    
    # etabs_model.property.link.set_spring_data(name='TestLinkProp', length=1.2, area=1.5)
    
    # etabs_model.property.link.set_multi_linear_points(name='TestLinkProp',
    #                                                   dof=etabs_model.property.link.eLinkDof.U1,
    #                                                   action_values=[-1000., -500., 0., 100., 600., 1000],
    #                                                   displacement_values=[-0.5, -0.4, 0., 0.2, 0.6, 0.8],
    #                                                   hysteresis_type=etabs_model.property.link.eLinkHysteresisType.KINEMATIC)


    # etabs_model.property.line_spring.set_line_spring_prop(name='TestLineSpringProp',
    #                                                       stiffness=[1., 2., 3., 4.],
    #                                                       nonlinear_option_2=etabs_model.property.line_spring.eSpringNonlinearOption.LINEAR,
    #                                                       nonlinear_option_3=etabs_model.property.line_spring.eSpringNonlinearOption.COMPRESSION_ONLY)

    # print(etabs_model.property.line_spring.get_line_spring_prop('TestLineSpringProp'))
    
    
    table = etabs_model.database_tables.get_table_details('Spring Property Definitions - Line Springs')
    
    table_data_array = etabs_model.database_tables.get_table_data_array(table, edit_mode=True)
    print('')

if __name__ == '__main__':
    main()