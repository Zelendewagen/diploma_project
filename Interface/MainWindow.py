import tkinter as tk
from tkinter import ttk

from Interface import TopWindow
import Controller
import Model
from Interface import Config

main_window: tk.Tk
main_label: tk.Label
main_table: ttk.Treeview


def start():
    global main_window
    global main_table
    global string_bar

    # Создание окна
    main_window = tk.Tk()
    main_window.title('Телефонный справочник')
    main_window.geometry(Config.window_geometry
                         (main_window, Config.main_window_width,
                          Config.main_window_height))

    RESIZABLE = False

    main_window.resizable(RESIZABLE, RESIZABLE)
    main_window.wm_attributes("-topmost", 1)

    # Меню бар
    menu_bar = tk.Menu(main_window, tearoff=0)
    main_window.config(menu=menu_bar)
    clear = 'Очистить справочник'
    menu_bar.add_command(label=clear, command=Controller.new_file)
    menu_bar.add_separator()
    menu_bar.add_command(label='Открыть', command=Controller.open_file)
    menu_bar.add_separator()
    menu_bar.add_command(label='Сохранить', command=Controller.save_file)

    # Таблица с контактами
    heads = ['id', 'Имя', 'Телефон', 'Комментарий']
    main_table = ttk.Treeview(main_window, columns=heads, show='headings')
    for header in heads:
        main_table.heading(header, text=header, anchor='w')

    main_table.column('id', minwidth=30, width=30)
    main_table.column('Имя', stretch=True, width=110, minwidth=100)
    main_table.column('Телефон', stretch=True, width=150, minwidth=110)
    main_table.column('Комментарий', stretch=True, width=208, minwidth=110)

    main_table.bind('<Button-3>', right_button_menu)
    main_table.pack(anchor='w')

    # Кнопка добавления контакта
    dbv = 'Добавить контакт'
    add_button = tk.Button(text=dbv,
                           command=lambda: TopWindow.create_add_window())
    add_button.pack(padx=25, pady=4, ipadx=20, anchor='w')

    # Строка поиска
    string_bar = tk.StringVar()
    search_bar = ttk.Entry(main_window, width=40, textvariable=string_bar)
    string_bar.trace('w', search_str)
    search_label = tk.Label(text='Поиск : ')
    search_label.place(x=200, y=253, anchor='sw')
    search_bar.place(x=250, y=253, anchor='sw')

    # Запуск
    Controller.open_file(temp=True)
    main_window.mainloop()


# Открывает меню с командами изменения или удаления контакта
def right_button_menu(event):
    global main_window
    global main_table
    popup_menu = tk.Menu(main_window, tearoff=0)
    row_id = event.widget.identify('item', event.x, event.y)
    event.widget.focus()
    file_menu = tk.Menu(popup_menu, tearoff=0)
    file_menu.add_command(label='Изменить контакт',
                          command=lambda: TopWindow.create_change_window(
                              main_table.item(row_id).get('values')))
    file_menu.add_separator()
    file_menu.add_command(label='Удалить контакт',
                          command=lambda: Controller.delete_contact(row_id))
    file_menu.post(event.x_root, event.y_root)


def search_str(*args):
    search_contact(string_bar.get())
    if not string_bar.get():
        Controller.refresh_table()


def search_contact(text):
    search_list = []
    if text:
        for contact in Model.my_phonebook.contacts:
            for item in contact.items():
                if text.lower() in item.lower():
                    search_list.append(contact.items())
                    break
    Controller.show_search_result(search_list)



