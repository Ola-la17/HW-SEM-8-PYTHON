from tkinter import END
import interface

path = 'phonebook.txt'
contacts = []
last_id: str = '0'

def read_file():
    global contacts, last_id
    with open(path, 'r', encoding='utf_8') as f:
        contacts = [i.strip().split(';') for i in f.readlines()]
    last_id = '0' if len(contacts) == 0 else contacts[len(contacts) - 1][0]
    refresh_table()

def get_contacts():
    global contacts
    return contacts

def edit_contact(ID: int):
    global contacts
    contacts = interface.main_table.Item(ID).get('values')
    interface.changeContact(contacts)

def save_contact(contact: list):
    global contacts
    for i in range(len(contacts)):
        if contacts[i][0] == contact[0]:
            contacts[i] = contact
            break
    save_file()
    refresh_table()

def save_file():
    global contacts
    with open(path, 'w', encoding='utf_8') as f:
        for contact in contacts:
            f.write(';'.join(contact) + "\n")

def delete_contact(id: str):
    global contacts
    contacts.pop(get_index(id))
    save_file()
    refresh_table()

def get_index(id: str):
    global contacts
    for i in range(len(contacts)):
        if contacts[i][0] == id:
            return i
    return None

def find_by_name(name: str):
    global contacts, current_id
    current_id = ''
    for i in range(len(contacts)):
        if contacts[i][1] == name:
            current_id = contacts[i][0]
            return contacts[i]
    return None

def refresh_table():
    interface.main_table.delete(*interface.main_table.get_children())
    for person in contacts:
        data = [person[1], person[2], person[3]]
        interface.main_table.insert("", END, values=data)
