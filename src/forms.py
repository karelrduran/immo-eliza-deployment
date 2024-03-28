import streamlit as st


def apartment_form():
    from_apartment = st.form("form apartment")
    col1, col2 = from_apartment.columns([0.5, 3], gap='small')

    col1.write('')
    col1.image('assets/images/province.png', width=50)
    col1.write('')
    province = col2.selectbox('Province',
                              ('ANTWERPEN',
                               'BRUSSEL',
                               'HENEGOUWEN',
                               'LIMBURG',
                               'LUIK',
                               'LUXEMBURG',
                               'NAMEN',
                               'OOST-VLAANDEREN',
                               'VLAAMS-BRABANT',
                               'WAALS-BRABANT',
                               'WEST-VLAANDEREN'
                               )
                              )

    col1.image('assets/images/house_facade.png', width=50)
    col1.write('')
    facade = col2.number_input(label='Number of Facades', min_value=0)

    col1.image('assets/images/habitable_surface.png', width=50)
    col1.write('')
    habitable_surface = col2.number_input('Habitable Surface in m2', min_value=0.0)

    col1.image('assets/images/living_surface.png', width=50)
    col1.write('')
    living_surface = col2.number_input('Living Surface in m2', min_value=0.0)

    col1.image('assets/images/terrace.png', width=50)
    col1.write('')
    col2.write('')
    col2.write('')
    col2.write('')
    terrace = col2.checkbox('Has a Terrace?')

    col1.image('assets/images/terrace_surface.png', width=50)
    col1.write('')
    terrace_surface = col2.number_input('Terrace Surface in m2', min_value=0.0)

    col1.image('assets/images/garden.png', width=50)
    col1.write('')
    col2.write('')
    col2.write('')
    col2.write('')
    garden = col2.checkbox('Has a Garden?')

    col1.image('assets/images/bedroom.png', width=50)
    col1.write('')
    bedroom_count = col2.number_input('Number of Bedrooms', min_value=0)

    col1.image('assets/images/bathroom.png', width=50)
    col1.write('')
    bathroom_count = col2.number_input('Number of Bathrooms', min_value=0)

    col1.image('assets/images/toilet.png', width=50)
    col1.write('')
    toilet_count = col2.number_input('Number of Toilets', min_value=0)

    col1.image('assets/images/kitchen_type.png', width=50)
    col1.write('')
    kitchen_type = col2.selectbox('Kitchen Type',
                                  ('NOT_INSTALLED',
                                   'USA_UNINSTALLED',
                                   'INSTALLED',
                                   'USA_INSTALLED',
                                   'SEMI_EQUIPPED',
                                   'USA_SEMI_EQUIPPED',
                                   'HYPER_EQUIPPED',
                                   'USA_HYPER_EQUIPPED'
                                   )
                                  )

    col1.image('assets/images/furnished.png', width=50)
    col1.write('')
    col2.write('')
    col2.write('')
    col2.write('')
    furnished = col2.checkbox('Furnished')

    col1.image('assets/images/state_of_building.png', width=50)
    col1.write('')
    state_of_building = col2.selectbox('State of the Building',
                                       ('TO_RESTORE',
                                        'TO_RENOVATE',
                                        'TO_BE_DONE_UP',
                                        'GOOD',
                                        'JUST_RENOVATED',
                                        'AS_NEW'
                                        )
                                       )

    col1.image('assets/images/epc.png', width=50)
    col1.write('')
    epc = col2.selectbox('Energy Performance Certificate (EPC)', ('A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G'))

    col1.image('assets/images/consumption_m2.png', width=50)
    col1.write('')
    consumption_per_m2 = col2.number_input('Consumption Per m2', min_value=0.0)

    predict = from_apartment.form_submit_button("Predict")

    if predict:
        return {
            'facades': facade,
            'habitable_surface': habitable_surface,
            'bedroom_count': bedroom_count,
            'bathroom_count': bathroom_count,
            'toilet_count': toilet_count,
            'room_count': bedroom_count + bathroom_count + toilet_count,
            'kitchen_type': kitchen_type,
            'furnished': furnished,
            'terrace': terrace,
            'garden_exists': garden,
            'state_of_building': state_of_building,
            'living_surface': living_surface,
            'epc': epc,
            'consumption_per_m2': consumption_per_m2,
            'province': {
                'name': province
            },
            'terrace_surface': terrace_surface

        }


def house_form():
    from_house = st.form("form house")
    col1, col2 = from_house.columns([0.5, 3], gap='small')

    col1.write('')
    col1.image('assets/images/province.png', width=50)
    col1.write('')
    province = col2.selectbox('Province',
                              ('ANTWERPEN',
                               'BRUSSEL',
                               'HENEGOUWEN',
                               'LIMBURG',
                               'LUIK',
                               'LUXEMBURG',
                               'NAMEN',
                               'OOST-VLAANDEREN',
                               'VLAAMS-BRABANT',
                               'WAALS-BRABANT',
                               'WEST-VLAANDEREN'
                               )
                              )

    col1.image('assets/images/house_facade.png', width=50)
    col1.write('')
    facade = col2.number_input(label='Number of Facades', min_value=0)

    col1.image('assets/images/habitable_surface.png', width=50)
    col1.write('')
    habitable_surface = col2.number_input('Habitable Surface in m2', min_value=0.0)

    col1.image('assets/images/land_surface.png', width=50)
    col1.write('')
    land_surface = col2.number_input('Land Surface in m2', min_value=0.0)

    col1.image('assets/images/living_surface.png', width=50)
    col1.write('')
    living_surface = col2.number_input('Living Surface in m2', min_value=0.0)

    col1.image('assets/images/terrace.png', width=50)
    col1.write('')
    col2.write('')
    col2.write('')
    col2.write('')
    terrace = col2.checkbox('Has a Terrace?')

    col1.image('assets/images/garden.png', width=50)
    col1.write('')
    col2.write('')
    col2.write('')
    col2.write('')
    garden = col2.checkbox('Has a Garden?')

    col1.image('assets/images/bedroom.png', width=50)
    col1.write('')
    bedroom_count = col2.number_input('Number of Bedrooms', min_value=0)

    col1.image('assets/images/bathroom.png', width=50)
    col1.write('')
    bathroom_count = col2.number_input('Number of Bathrooms', min_value=0)

    col1.image('assets/images/toilet.png', width=50)
    col1.write('')
    toilet_count = col2.number_input('Number of Toilets', min_value=0)

    col1.image('assets/images/kitchen_type.png', width=50)
    col1.write('')
    kitchen_type = col2.selectbox('Kitchen Type',
                                  ('NOT_INSTALLED',
                                   'USA_UNINSTALLED',
                                   'INSTALLED',
                                   'USA_INSTALLED',
                                   'SEMI_EQUIPPED',
                                   'USA_SEMI_EQUIPPED',
                                   'HYPER_EQUIPPED',
                                   'USA_HYPER_EQUIPPED'
                                   )
                                  )

    col1.image('assets/images/furnished.png', width=50)
    col1.write('')
    col2.write('')
    col2.write('')
    col2.write('')
    furnished = col2.checkbox('Furnished')

    col1.image('assets/images/state_of_building.png', width=50)
    col1.write('')
    state_of_building = col2.selectbox('State of the Building',
                                       ('TO_RESTORE',
                                        'TO_RENOVATE',
                                        'TO_BE_DONE_UP',
                                        'GOOD',
                                        'JUST_RENOVATED',
                                        'AS_NEW'
                                        )
                                       )

    col1.image('assets/images/epc.png', width=50)
    col1.write('')
    epc = col2.selectbox('Energy Performance Certificate (EPC)', ('A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G'))

    col1.image('assets/images/consumption_m2.png', width=50)
    col1.write('')
    consumption_per_m2 = col2.number_input('Consumption Per m2', min_value=0.0)

    predict = from_house.form_submit_button("Predict")

    if predict:
        return {
            'facades': facade,
            'habitable_surface': habitable_surface,
            'bedroom_count': bedroom_count,
            'bathroom_count': bathroom_count,
            'toilet_count': toilet_count,
            'room_count': bedroom_count + bathroom_count + toilet_count,
            'kitchen_type': kitchen_type,
            'furnished': furnished,
            'terrace': terrace,
            'garden_exists': garden,
            'state_of_building': state_of_building,
            'living_surface': living_surface,
            'epc': epc,
            'consumption_per_m2': consumption_per_m2,
            'province': {
                'name': province
            },
            'land_surface': land_surface

        }
