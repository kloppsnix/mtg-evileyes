from jinja2 import Environment, FileSystemLoader

def create_labels(label_data):

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("set_print_template.svg")

    label_data = label_data[label_data["Select Set(s)"] == True]
    label_data = label_data.iloc[0]

    # name = label_data["name"]
    # add_name = label_data["add_name"]
    # released_at = label_data["released_at"],
    # icon_svg_uri = label_data["icon_svg_uri"]

    filename = "rendered.svg"
    content = template.render(
        name = label_data["name"],
        # add_name = label_data["add_name"],
        released_at = label_data["released_at"],
        icon_svg_uri = label_data["icon_svg_uri"]
        )
    #with open(filename, mode="w", encoding="utf-8") as message:
    #    message.write(content)
    #print(f"... wrote {filename}")

    return content

def set_xy_positions(
    dataset, 
    n_columns = 4, 
    n_rows = 15,
    height_mm = 19.133333,
    width_mm = 50., 
    x_init = 5., 
    y_init= 5.
):
    
    # Number of rows
    n_data = len(dataset)
    n_max = n_rows * n_columns

    if n_data > n_max:
        raise ValueError(
            f"Data contains more than {n_max} items "
            "which is not allowed!"
        )

    positions = []

    # Iterate through the set of items and calculate positions
    for i in range(n_data):
        row = i // n_columns
        col = i % n_columns
        x = x_init + col * width_mm
        y = y_init + row * height_mm
        positions.append((x, y))

    x, y = list(zip(*positions))

    dataset["x"] = x
    dataset["y"] = y

    return dataset