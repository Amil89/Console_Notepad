from pathlib import Path
import os


def head_text(app_name: str, separate: str):
    app_name = 'Note'
    separate = '*'
    print(f'\n\n{separate*31}\n\t{app_name}\t')
    print(f'{separate*31}\n\n [1] New file\n [2] Open file\n [3] New folder\n [4] About\n [5] Quit Note\n')


def new_folder(folder_path: str, folder_name: str):
    folder_name = input('Enter folder name: ')
    folder_path = input('Enter the full path of folder: ')
    os.mkdir(f'{folder_path}/{folder_name}')


def new_file(text_in_file: str, file_name: str, path_file: str, contents: list):
    print('Enter your content. CTRL-D or CTRL-Z (windows) to save it: ')
    contents = []
    while True:
        try:
            text_in_file = input('')
            contents.append(text_in_file)
        except EOFError:
            question_for_save = input('Do you want to save your file [ Y ]yes or [ N ]no?: ')
            if question_for_save == 'Y':
                file_name = input('\nEnter name of file: ')
                path_file = input('Enter the full path to the folder where the file will be saved: ')
                for item in contents:
                    file = Path(f'/{path_file}/{file_name}').open('a+')
                    file.write(f'\n{item}')
                break
            elif question_for_save == 'N':
                break


def open_file(file_open: str, path_file: str):
    while True:
        try:
            path_file = input('Enter full path to the file. < Back [ b ]: ')
            if path_file == 'b':
                menu()
            else:
                file_open = Path(path_file).read_text()
                print(file_open)
            break
        except FileNotFoundError:
            print('Unable to open the file. The file is missing or the name of the file is invalid!')


def display_about(separate: str, about: str):
    separate = '_'*40
    about = """
    App name: Note | Build: 1.0
    By ChiefBR0 2023.
    All rights reserved.
    Only for Linux/Unix Systems.
    """
    print(f'\n\n{separate}\n{about}\n\n')


def menu(choise):
    head_text('Note', '*')
    choise = input('~ Select item: ')
    match choise:
        case '1':
            new_file('0', '0', '0', [0])
        case '2':
            open_file('0', '0')
        case '3':
            new_folder('0', '0')
        case '4':
            display_about('-', 'note')
        case '5':
            return


menu('0')
