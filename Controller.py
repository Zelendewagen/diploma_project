import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox as mb

import Model
from Interface import MainWindow
from Interface import TopWindow


def refresh_table():
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for row in Model.my_phonebook.get_contacts():
        MainWindow.main_table.insert('', 'end', values=row)
    save_file(temp=True)


def show_search_result(search_list):
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for row in search_list:
        MainWindow.main_table.insert('', 'end', values=row)


def add_contact(add_entry: list):
    if add_entry[0].get() and add_entry[1].get():
        Model.my_phonebook.add(
            add_entry[0].get(), add_entry[1].get(), add_entry[2].get())
    else:
        # добавляет 3 тестовых контакта, если при добавлении нового контакта не было заполнено ни одно поле
        if not add_entry[0].get() and not add_entry[1].get() and not add_entry[2].get():
            Model.my_phonebook.add('Егор', '+7-777-777-77-77', 'Домашний')
            Model.my_phonebook.add('Саня', '+7 777 777 77 77', 'Рабочий')
            Model.my_phonebook.add('Мария', '+77777777777', 'Личный')
    refresh_table()
    TopWindow.add_contact_window.destroy()


def change_contact(change_entry: list, contact: list):
    Model.my_phonebook.set(contact[0], change_entry[0].get(),
                           change_entry[1].get(), change_entry[2].get())
    refresh_table()
    TopWindow.change_window.destroy()


def delete_contact(id):
    contact = MainWindow.main_table.item(id).get('values')
    if mb.askyesno('Удалить', 'Точно?'):
        Model.my_phonebook.remove(contact[0])
        refresh_table()


def new_file():
    if mb.askyesno('Удалить все контакты', 'Точно?'):
        Model.my_phonebook.clear()
    refresh_table()


def open_file(temp: bool = False):
    if temp:
        full_file_name = "Saves/temp.spr"
        if not os.path.exists("Saves/temp.spr"):
            with open("Saves/temp.spr", "w", encoding='UTF-8') as file:
                file.close()
    else:
        full_file_name = askopenfilename(title='Открыть', filetypes=(("Файл справочника", "*.spr"),))
    try:
        with open(full_file_name, 'r', encoding='UTF-8') as file:
            Model.my_phonebook.clear()
            for index, line in enumerate(file.readlines()):
                contact = line.replace('\n', '').replace("'", "").replace('"', '').split(',')
                Model.my_phonebook.add(
                    contact[1], contact[2], contact[3], contact[0])
    except Exception as e:
        print(f'Файл не выбран\n{e}')
    refresh_table()


def save_file(temp: bool = False):
    if temp:
        full_file_name = "Saves/temp.spr"
    else:
        full_file_name = asksaveasfilename(
            title='Сохранить как...', filetypes=(("Файл справочника", ".spr"),), initialfile='Новый справочник.spr')

    try:
        with open(full_file_name, 'w', encoding='UTF-8') as file:
            data = ''
            for contact in Model.my_phonebook.get_contacts():
                for item in contact:
                    data += f"'{str(item)}',"
                data += '\n'
            file.write(data)
    except Exception as e:
        print(f'Файл не выбран\n{e}')
