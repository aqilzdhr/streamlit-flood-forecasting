import streamlit as st
from streamlit_option_menu import option_menu

# horizontal menu
selected = option_menu(
menu_title=None,
  options=["Home", "Prediction", "Video" "ABout Us"],
  orientation="horizontal"
)

if selected == "Home":
  st.title(f"you have select {selected}")
  if selected == "Prediction":
  st.title(f"you have selected {selected}")
  if selected == "Video":
  st.title(f"you have selected {selected}")
  if selected == "About Us":
  st.title(f"you have selected {selected}")
