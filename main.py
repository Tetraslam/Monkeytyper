import pyautogui


def type_file(file_path):
    with open(file_path, 'r') as f:
        for char in f.read():
            pyautogui.typewrite(char)

file_path = "typetext.txt" # Add the text shown on screen here
type_file(file_path)
