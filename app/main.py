import streamlit as st
# import time
# import requests
import pandas as pd

from state import toggle_session_state
from filter import filter_sort_columns_data
from cache import load_filter_sets

st.write(st.session_state)      # display state
# st.session_state["search_clicked"] = False

base_url = "https://api.scryfall.com"
set_url = base_url + "/" + "sets"

st.title("Set-Labler")

sel_box = st.multiselect("Choose Sets",
                         ["core", "expansion"],     # Selection-Items
                         ["core", "expansion"],     # default
                         on_change = toggle_session_state
                        )

btn_search = st.button("Search")
if btn_search:      # = if btn_search = true | button clicked
    st.session_state["search_clicked"] = True

st.write(st.session_state)      # display state

if st.session_state.get("search_clicked", False):       # search_clicked = False
    asd = load_filter_sets(set_url = set_url, sel_box = sel_box)

    chkb_sel_all = st.checkbox("Select all")     

    filtered_data = filter_sort_columns_data(filtered_data = asd, sel_fields = chkb_sel_all)

    usr_selection = st.data_editor(
        filtered_data, 
        column_config={     # preview set-icons
            "icon_svg_uri": st.column_config.ImageColumn(
                "Preview Image", help="Streamlit app preview screenshots", width = "small"
            )
        },
        hide_index=True
    )