import tkinter as tk
import model
import size as s

add_root: tk.Tk
add_entry: list
contact: list

def start(person: list):
    global add_root
    global add_entry
    global contact
    contact = person
    add_root = tk.Toplevel()
    add_root.wm_attributes("-topmost", 1)
    add_root.geometry(s.get_dialog_window_size())
    add_root.resizable(width=False, height=False)

    add_root.columnconfigure(index=0, weight=1)
    add_root.columnconfigure(index=1, weight=3)

    name_label = tk.Label(add_root, text='Имя')
    phone_label = tk.Label(add_root, text='Телефон')
    comment_label = tk.Label(add_root, text = 'Комментарий')
    name_label.grid(column=0, row=0, sticky='e')
    phone_label.grid(column=0, row=1, sticky='e')
    comment_label.grid(column=0, row=2, sticky='e')

    add_entry = [tk.Entry(add_root, width=30)for _ in range(3)]
    for i, Entry in enumerate(add_entry):
        add_entry[i].grid(column=1, row=i)
    if contact != None:
        add_entry[0].insert(0, contact[1])
        add_entry[1].insert(0, contact[2])
        add_entry[2].insert(0, contact[3])
        title = 'Добавить контакт' if contact == None else 'Контакт'
        add_root.title(title)
        delete_button = tk.Button(add_root, text='Удалить', command=lambda: delete_contact())
        delete_button.grid(column=0, row=3)
        save_button = tk.Button(add_root, text='Сохранить', command=lambda: save_contact(add_entry))
        save_button.grid(column=2, row=3)
    else:
        add_button = tk.Button(add_root, text='Добавить', command=lambda: add_contacts(add_entry))
        add_button.grid(columnspan=2, row=3)
    add_root.mainloop()

def add_contacts(add_entry: list):
    global add_root
    new_id = str(int(model.last_id) + 1) 
    model.contacts.append([new_id, add_entry[0].get(), add_entry[1].get(), add_entry[2].get()])
    model.last_id = new_id
    model.refresh_table()
    model.save_file()
    add_root.destroy()

def delete_contact():
    global contact
    global add_root
    model.delete_contact(contact[0])
    add_root.destroy()

def save_contact(add_entry: list):
    global contact
    global add_root
    contact[1] = add_entry[0].get()
    contact[2] = add_entry[1].get()
    contact[3] = add_entry[2].get()
    model.save_contact(contact)
    add_root.destroy()
