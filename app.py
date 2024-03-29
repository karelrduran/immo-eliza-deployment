import time
import streamlit as st

from streamlit_image_select import image_select
from src.forms import house_form, apartment_form
from src.data_predict import predict

# Page Configuration

st.set_page_config(
    page_title="🦀 Price predictor for houses and apartments in Belgium",
    page_icon="🦀",
    layout="wide",
    initial_sidebar_state='expanded'
)

st.markdown(
    """
    <style>
    body {
        background-color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Banner

st.image('assets/images/banner.png')

# Sidebar section

house_img_path = "assets/images/house.jpg"
apartment_img_path = "assets/images/apartment.jpg"

with st.sidebar:
    side_bar = st.sidebar.title('Choose a type of property')
    img = image_select(
        label="",
        images=[
            house_img_path,
            apartment_img_path,
        ],
        captions=["House", "Apartment"],
    )

# Body section

predicted_price = 0

property_type = 'apartment'

if 'house' in img:
    property_type = 'house'
    data = house_form()
else:
    data = apartment_form()

predicted_price = predict(data=data, property_type=property_type)

if predicted_price:
    with st.container(border=True):
        with st.spinner('Processing...'):
            time.sleep(1)
            green_style = '<span style="color:green;">{:.2f}</span>'.format(predicted_price)
            st.write(f"According to the data provided, the property is valued at: {green_style} euros",
                     unsafe_allow_html=True)

# Footer section

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        padding: 10px 0;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="footer">
        <p>© 2024 HermitCrab. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
