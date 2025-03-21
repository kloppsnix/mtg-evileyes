import streamlit as st
import requests
from filter import filter_set_data

@st.cache_data
def load_filter_sets(set_url, sel_box):
    with st.spinner("Searching Sets...", show_time = True):
        all_sets_data = requests.get(url = set_url)     # get data from api
        asd = all_sets_data.json()

        asd = filter_set_data(all_set_data = asd, selection_box = sel_box)

    return asd