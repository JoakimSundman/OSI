import graphics


def read_layer_data(layer_number):
    file_path = f"data/layers/osi-{layer_number}.md"
    with open(file_path, "r") as f:
        return f.read()

def main():
    graphics.draw_layers()
    while True:
        user_input = input("Pick a layer to learn more about it (or type 'exit' to quit): ")  # noqa: E501
        if user_input == "exit":
            break
        if user_input.isdigit():
            layer_number = int(user_input)
            if 1 <= layer_number <= 7:
                graphics.draw_selected_layer(layer_number)
        else:
            print("Invalid input. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()