import tkinter as tk

from Interface import Config
import Controller

add_contact_window: tk.Tk
change_window: tk.Tk
add_entry = []
change_entry = []


def create_add_window():
    global add_contact_window
    global add_entry

    RESIZABLE = False

    add_contact_window = tk.Toplevel()
    add_contact_window.grab_set()
    add_contact_window.title('Добавить контакт')
    add_contact_window.geometry(Config.window_geometry(
        add_contact_window, Config.top_window_width, Config.top_window_height))
    add_contact_window.resizable(RESIZABLE, RESIZABLE)
    add_contact_window.attributes("-topmost", True)

    add_contact_window.columnconfigure(index=0, weight=50)
    add_contact_window.columnconfigure(index=1, weight=250)

    name_lable = tk.Label(add_contact_window, text='Имя')
    phone_lable = tk.Label(add_contact_window, text='Телефон')
    comment_lable = tk.Label(add_contact_window, text='Комментарий\n(Не обязательно)')
    name_lable.grid(column=0, row=0, pady=3, sticky='e')
    phone_lable.grid(column=0, row=1, sticky='e')
    comment_lable.grid(column=0, row=2, sticky='e')

    add_entry = [tk.Entry(add_contact_window, width=30) for _ in range(3)]
    for i, entry in enumerate(add_entry):
        add_entry[i].grid(column=1, row=i)

    add_button = tk.Button(add_contact_window, text='Добавить',
                           command=lambda: Controller.add_contact(add_entry))
    add_button.grid(columnspan=2, pady=2, row=3)


def create_change_window(contact: list):
    global change_window
    global change_entry

    RESIZABLE = False

    change_window = tk.Toplevel()
    change_window.grab_set()
    change_window.title('Изменить контакт')
    change_window.geometry(Config.window_geometry(change_window, Config.top_window_width, Config.top_window_height))
    change_window.resizable(RESIZABLE, RESIZABLE)
    change_window.attributes("-topmost", 1)

    change_window.columnconfigure(index=0, weight=50)
    change_window.columnconfigure(index=1, weight=250)

    name_lable = tk.Label(change_window, text='Имя')
    phone_lable = tk.Label(change_window, text='Телефон')
    comment_lable = tk.Label(change_window, text='Комментарий')
    name_lable.grid(column=0, row=0, pady=3, sticky='e')
    phone_lable.grid(column=0, row=1, sticky='e')
    comment_lable.grid(column=0, row=2, sticky='e')

    change_entry = [tk.Entry(change_window, width=30) for _ in range(3)]
    for i, entry in enumerate(change_entry):
        change_entry[i].insert(0, contact[i + 1])
        change_entry[i].grid(column=1, row=i)

    change_button = tk.Button(change_window, text='Изменить',
                              command=lambda: Controller.change_contact(change_entry, contact))
    change_button.grid(columnspan=2, pady=2, row=3)

    change_window.mainloop()
