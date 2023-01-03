import tkinter as tk
import model, contact_window

find_window: tk.Tk
find_entry: tk.Entry

def start():
    global find_window
    global find_entry
    find_window = tk.Toplevel()
    find_window.title('Поиск')
    find_window.wm_attributes("-topmost", 1)
    find_window.geometry('250x100')
    find_window.resizable(width=False, height=False)

    find_window.columnconfigure(index=0, weight=50)
    find_window.columnconfigure(index=1, weight=250)

    name_label = tk.Label(find_window, text='Имя')
    name_label.grid(column=0, row=0, sticky='e')
    name_label.pack()

    find_entry = tk.Entry(find_window, width=30)
    find_entry.pack()
    
    find_button = tk.Button(find_window, text='Поиск', command=lambda: find_contact(find_entry.get()))
    find_button.pack()

    find_window.mainloop()

def find_contact(name: str):
    global find_window
    global find_entry
    person = model.find_by_name(name)
    if person == None:
        find_entry.delete(0,tk.END)
        find_entry.insert(0, 'Ничего не найдено')
    else:
        find_window.destroy()
        contact_window.start(person) # Отобразить контакт
