import json

import graphics


def read(info):
    with open(info, "r") as file:  
        data = json.load(file)
    return data

def main():
    graphics.draw_layers()

if __name__ == "__main__":
    main()