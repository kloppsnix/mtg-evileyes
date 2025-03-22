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