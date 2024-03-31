from main_functions import *


def main():
    os.system("cls")
    print("Welcome to an unofficial command-line Github repositories searching application")
    print_main_message({"space": "activates search system.", "esc": "exits program."})
    keyboard.on_press(search)
    keyboard.wait('esc')


if __name__ == "__main__":
    main()











