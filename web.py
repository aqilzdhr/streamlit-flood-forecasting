import streamlit as st
from streamlit_option_menu import option_menu

# horizontal menu
selected = option_menu(
menu_title=none,
  option=["Home", "Prediction", "Video" "ABout Us"],
  icons=["house", "brain", "book", "man"],
  menu_icon="cast",
  default_index=0,
  orientation="horizontal"
)

if selected == "Home":
  st.title(f"{selected}")
  if selected == "Prediction":
  st.title(f"{selected}")
  if selected == "Video":
  st.title(f"{selected}")
  if selected == "About Us":
  st.title(f"{selected}")
