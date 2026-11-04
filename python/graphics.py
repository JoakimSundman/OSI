layers = [("Application", 7),
          ("Presentation", 6), 
          ("Session", 5), 
          ("Transport", 4), 
          ("Network", 3), 
          ("Data link", 2), 
          ("Physical", 1)]

name_width = max(len(layer[0]) for layer in layers) + 2 
number_width = 3

def draw_layers():
    for layer in layers:
       name = layer[0]
       number = layer[1]
       print("+" + "-" * number_width + "+" + "-" * (name_width + 2) + "+")
       print(f"| {number} | {name.ljust(name_width)} |")
    print("+" + "-" * number_width + "+" + "-" * (name_width + 2) + "+")