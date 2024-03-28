import streamlit as st

from streamlit_image_select import image_select
from src.forms import house_form, apartment_form
from src.data_predict import predict

# age Configuration

# with st.set_page_config:
st.set_page_config(page_title="🦀 Price predictor for houses and apartments in Belgium")

# Title section
st.markdown("<h1 style='text-align: center; color: grey;'>🦀 Price predictor for houses and apartments in Belgium</h1>",
            unsafe_allow_html=True)

# Sidebar section

house_img_path = "assets/images/house.jpg"
apartment_img_path = "assets/images/apartment_select.png"

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

if 'house' in img:
    predicted_price = predict(house_form(), property_type='house')
    if predicted_price:
        with st.container(border=True):
            green_style = '<span style="color:green;">{:.2f}</span>'.format(predicted_price)
            st.write(f"According to the data provided, the property is valued at: {green_style} euros",
                     unsafe_allow_html=True)
else:
    predicted_price = predict(apartment_form(), property_type='apartment')
    if predicted_price:
        with st.container(border=True):
            green_style = '<span style="color:green;">{:.2f}</span>'.format(predicted_price)
            st.write(f"According to the data provided, the property is valued at: {green_style} euros",
                     unsafe_allow_html=True)
