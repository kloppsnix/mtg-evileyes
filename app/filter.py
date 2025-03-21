import pandas as pd

def filter_set_data(all_set_data, selection_box):
    filtered_data = []      # empty list
    for item in all_set_data["data"]:        # loop asd
        if item["set_type"] in selection_box:     # criteria
            filtered_data.append(item)      # append set to filtered_data
    
    return filtered_data

def filter_sort_columns_data(filtered_data, sel_fields):
    filtered_data = pd.DataFrame(filtered_data)
    filtered_data = filtered_data[["name", "released_at", "icon_svg_uri", "set_type"]]
    filtered_data = filtered_data.sort_values(["set_type", "released_at"], ascending = [True, False])

    filtered_data["Select Set(s)"] = sel_fields
    filtered_data = filtered_data[["Select Set(s)", "name", "released_at", "icon_svg_uri"]]

    # filtered_data = filtered_data.head(5)

    return filtered_data