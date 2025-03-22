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
