import os
import string

letters = list(string.ascii_uppercase)

current_dir = os.getcwd()

for letter in letters:
    folder_path = os.path.join(current_dir, letter)
    os.mkdir(folder_path)
