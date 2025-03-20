import streamlit as st
import time
import requests
import pandas as pd

base_url = "https://api.scryfall.com"
set_url = base_url + "/" + "sets"

st.title("Set-Labler")

sel_box = st.multiselect("Choose Sets",
                         ["core", "expansion"],
                         ["core", "expansion"]
                        )

btn_search = st.button("Search")
if btn_search:
    with st.spinner("Wait for it...", show_time=True):
        all_sets_data = requests.get(url = set_url)
        asd = all_sets_data.json()

        filtered_data = []
        for item in asd["data"]:
            if item["set_type"] in sel_box:
                filtered_data.append(item)      

    filtered_data = pd.DataFrame(filtered_data)
    filtered_data = filtered_data[["name", "released_at", "icon_svg_uri", "set_type"]]
    filtered_data = filtered_data.sort_values("set_type")

    filtered_data["Select Set(s)"] = False
    filtered_data = filtered_data[["Select Set(s)", "name", "released_at", "icon_svg_uri"]]

    filtered_data = filtered_data.head(5)

    usr_selection = st.data_editor(
        filtered_data, 
        column_config={
            "icon_svg_uri": st.column_config.ImageColumn(
                "Preview Image", help="Streamlit app preview screenshots", width = "large"
            )
        },
        hide_index=True
    )