import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Flood Forecasting", page_icon="tada:")

#header section
st.title("Flood Forecasting")

# horizontal menu
selected = option_menu(
menu_title=none,
  option=["Home", "Prediction",, "Video" "ABout Us"]
  icons=["house", "brain", "youtube", "man"]
  menu_icon="cast",
  default_index=0,
  orientation="horizontal"
)
