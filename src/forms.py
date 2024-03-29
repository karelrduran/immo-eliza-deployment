import streamlit as st


def apartment_form():
    """
    Generates a form using Streamlit for collecting information related to an apartment.

    Returns:
    dict: A dictionary containing the collected information.
        The dictionary contains the following keys:
            - 'facades': Number of facades of the apartment.
            - 'habitable_surface': Habitable surface area of the apartment in square meters.
            - 'bedroom_count': Number of bedrooms in the apartment.
            - 'bathroom_count': Number of bathrooms in the apartment.
            - 'toilet_count': Number of toilets in the apartment.
            - 'room_count': Total number of rooms in the apartment (sum of bedrooms, bathrooms, and toilets).
            - 'kitchen_type': Type of kitchen in the apartment.
            - 'furnished': Boolean indicating whether the apartment is furnished or not.
            - 'terrace': Boolean indicating whether the apartment has a terrace or not.
            - 'garden_exists': Boolean indicating whether the apartment has a garden or not.
            - 'state_of_building': State of the building where the apartment is located.
            - 'living_surface': Living surface area of the apartment in square meters.
            - 'epc': Energy Performance Certificate (EPC) rating of the apartment.
            - 'consumption_per_m2': Energy consumption per square meter of the apartment.
            - 'province': Dictionary containing information about the province where the apartment is located.
                The dictionary contains the following key:
                    - 'name': Name of the province.
            - 'terrace_surface': Surface area of the terrace in square meters.
    """
    st.write(
        "<h3>🦀 Apartment information:</h3>",
        unsafe_allow_html=True
    )
    from_apartment = st.form("form apartment")
    col1, col2, col3, col4 = from_apartment.columns([0.2, 1, 0.2, 1], gap='small')

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

    col1.image('assets/images/state_of_building.png', width=50)
    col1.write('')
    state_of_building = col2.selectbox('State of the Building',
                                       ('AS_NEW',
                                        'JUST_RENOVATED',
                                        'GOOD',
                                        'TO_BE_DONE_UP',
                                        'TO_RENOVATE',
                                        'TO_RESTORE'
                                        )
                                       )

    col1.image('assets/images/habitable_surface.png', width=50)
    col1.write('')
    habitable_surface = col2.number_input('Habitable Surface in m2', min_value=0.0)

    col1.image('assets/images/living_surface.png', width=50)
    col1.write('')
    living_surface = col2.number_input('Living Surface in m2', min_value=0.0)

    col1.image('assets/images/kitchen_type.png', width=50)
    col1.write('')
    kitchen_type = col2.selectbox('Kitchen Type',
                                  ('USA_HYPER_EQUIPPED',
                                   'HYPER_EQUIPPED',
                                   'USA_SEMI_EQUIPPED',
                                   'SEMI_EQUIPPED',
                                   'USA_INSTALLED',
                                   'INSTALLED',
                                   'USA_UNINSTALLED',
                                   'NOT_INSTALLED',
                                   )
                                  )

    col1.image('assets/images/epc.png', width=50)
    col1.write('')
    epc = col2.selectbox('Energy Performance Certificate (EPC)', ('A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G'))

    col1.image('assets/images/consumption_m2.png', width=50)
    col1.write('')
    consumption_per_m2 = col2.number_input('Consumption Per m2', min_value=0.0)

    col3.write('')
    col3.image('assets/images/house_facade.png', width=50)
    col3.write('')
    facade = col4.number_input(label='Number of Facades', min_value=0)

    col3.image('assets/images/bedroom.png', width=50)
    col3.write('')
    bedroom_count = col4.number_input('Number of Bedrooms', min_value=0)

    col3.image('assets/images/bathroom.png', width=50)
    col3.write('')
    bathroom_count = col4.number_input('Number of Bathrooms', min_value=0)

    col3.image('assets/images/toilet.png', width=50)
    col3.write('')
    toilet_count = col4.number_input('Number of Toilets', min_value=0)

    col3.image('assets/images/garden.png', width=50)
    col4.write('')
    col4.write('')
    col4.write('')
    garden = col4.toggle('Has a Garden?')

    col3.write('')
    col3.image('assets/images/furnished.png', width=50)
    col4.write('')
    col4.write('')
    furnished = col4.toggle('Furnished')

    col3.image('assets/images/terrace.png', width=50)
    col4.write('')
    col4.write('')

    with col4.popover('Terrace Surface'):
        terrace_surface = st.number_input('Terrace Surface in m2', min_value=0.0)

    predict = from_apartment.form_submit_button("Get Price", type="primary")

    terrace = False

    if predict:
        if terrace_surface != 0.0:
            terrace = True
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
    """
    Generates a form using Streamlit for collecting information related to a house.

    Returns:
    dict: A dictionary containing the collected information.
        The dictionary contains the following keys:
            - 'facades': Number of facades of the house.
            - 'habitable_surface': Habitable surface area of the house in square meters.
            - 'bedroom_count': Number of bedrooms in the house.
            - 'bathroom_count': Number of bathrooms in the house.
            - 'toilet_count': Number of toilets in the house.
            - 'room_count': Total number of rooms in the house (sum of bedrooms, bathrooms, and toilets).
            - 'kitchen_type': Type of kitchen in the house.
            - 'furnished': Boolean indicating whether the house is furnished or not.
            - 'terrace': Boolean indicating whether the house has a terrace or not.
            - 'garden_exists': Boolean indicating whether the house has a garden or not.
            - 'state_of_building': State of the building where the house is located.
            - 'living_surface': Living surface area of the house in square meters.
            - 'epc': Energy Performance Certificate (EPC) rating of the house.
            - 'consumption_per_m2': Energy consumption per square meter of the house.
            - 'province': Dictionary containing information about the province where the house is located.
                The dictionary contains the following key:
                    - 'name': Name of the province.
            - 'land_surface': Land surface area of the house in square meters.
    """
    st.write(
        "<h3>🦀 House information:</h3>",
        unsafe_allow_html=True
    )
    from_house = st.form("form house")
    col1, col2, col3, col4 = from_house.columns([0.2, 1, 0.2, 1], gap='small')

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

    col1.image('assets/images/state_of_building.png', width=50)
    col1.write('')
    state_of_building = col2.selectbox('State of the Building',
                                       ('AS_NEW',
                                        'JUST_RENOVATED',
                                        'GOOD',
                                        'TO_BE_DONE_UP',
                                        'TO_RENOVATE',
                                        'TO_RESTORE'
                                        )
                                       )

    col3.write('')
    col3.image('assets/images/house_facade.png', width=50)
    col3.write('')
    facade = col4.number_input(label='Number of Facades', min_value=0)

    col1.image('assets/images/habitable_surface.png', width=50)
    col1.write('')
    habitable_surface = col2.number_input('Habitable Surface in m2', min_value=0.0)

    col1.image('assets/images/land_surface.png', width=50)
    col1.write('')
    land_surface = col2.number_input('Land Surface in m2', min_value=0.0)

    col1.image('assets/images/living_surface.png', width=50)
    col1.write('')
    living_surface = col2.number_input('Living Surface in m2', min_value=0.0)

    col3.image('assets/images/bedroom.png', width=50)
    col3.write('')
    bedroom_count = col4.number_input('Number of Bedrooms', min_value=0)

    col3.image('assets/images/bathroom.png', width=50)
    col3.write('')
    bathroom_count = col4.number_input('Number of Bathrooms', min_value=0)

    col3.image('assets/images/toilet.png', width=50)
    col3.write('')
    toilet_count = col4.number_input('Number of Toilets', min_value=0)

    col1.image('assets/images/kitchen_type.png', width=50)
    col1.write('')
    kitchen_type = col2.selectbox('Kitchen Type',
                                  ('USA_HYPER_EQUIPPED',
                                   'HYPER_EQUIPPED',
                                   'USA_SEMI_EQUIPPED',
                                   'SEMI_EQUIPPED',
                                   'USA_INSTALLED',
                                   'INSTALLED',
                                   'USA_UNINSTALLED',
                                   'NOT_INSTALLED',
                                   )
                                  )

    col1.image('assets/images/epc.png', width=50)
    col1.write('')
    epc = col2.selectbox('Energy Performance Certificate (EPC)', ('A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G'))

    col1.image('assets/images/consumption_m2.png', width=50)
    col1.write('')
    consumption_per_m2 = col2.number_input('Consumption Per m2', min_value=0.0)

    col3.image('assets/images/terrace.png', width=50)
    col3.write('')
    col4.write('')
    col4.write('')
    col4.write('')
    terrace = col4.toggle('Has a Terrace?')

    col3.image('assets/images/garden.png', width=50)
    col3.write('')
    col4.write('')
    col4.write('')
    garden = col4.toggle('Has a Garden?')

    col3.image('assets/images/furnished.png', width=50)
    col3.write('')
    col4.write('')
    col4.write('')
    col4.write('')
    furnished = col4.toggle('Furnished')

    predict = from_house.form_submit_button("Get Price", type="primary")

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
