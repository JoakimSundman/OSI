import json

import graphics


def read(path):
    with open(path, "r", encoding="utf-8") as file:  
        data = json.load(file)
    return data

def main():
    graphics.draw_layers()

if __name__ == "__main__":
    main()