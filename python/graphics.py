layers = [
    ("Application", 7),
    ("Presentation", 6),
    ("Session", 5),
    ("Transport", 4),
    ("Network", 3),
    ("Data link", 2),
    ("Physical", 1),
]

name_width = max(len(layer[0]) for layer in layers)
number_width = 3


def line(char):
    print("+" + char * number_width + "+" + char * (name_width + 2) + "+")


def draw_layers():
    for layer in layers:
        name = layer[0]
        number = layer[1]
        line("-")
        print(f"| {number} | {name.ljust(name_width)} |")
    line("-")


def draw_selected_layer(layer_number):
    for layer in layers:
        name = layer[0]
        number = layer[1]
        if number == layer_number:
            line("=")
            print(f"| {number} | {name.ljust(name_width)} |  <-- Selected Layer")
        elif number == layer_number - 1:
            line("=")
            print(f"| {number} | {name.ljust(name_width)} |")
        else:
            line("-")
            print(f"| {number} | {name.ljust(name_width)} |")
    if layer_number == 1:
        line("=")
    else:
        line("-")