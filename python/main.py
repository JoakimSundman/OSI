import json


def read(info):
    with open(info, "r") as file:  
        data = json.load(file)
    return data

def main():
    pass

if __name__ == "__main__":
    main()