import streamlit as st

def toggle_session_state():

    if "search_clicked" in st.session_state:
        if st.session_state["search_clicked"]:      ## = st.session_state["search_clicked"] = true
            st.session_state["search_clicked"] = False
        else:
            st.session_state["search_clicked"] = True