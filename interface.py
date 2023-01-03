from ctypes import resize
import tkinter as tk
from tkinter import NO, VERTICAL, ttk
import model, contact_window, find_window
import size as s

main_table: ttk.Treeview
message_to_user: tk.Text
user_print: tk.Entry
add_entry: list
change_entry: list

def start():
    global main_table
    global message_to_user
    global btn_do_it
    global user_print
    global root
    root = tk.Tk()
    root.geometry(s.get_screen_size(root))
    root['bg'] = '#000000'
    root.title('Phone Book')
    root.wm_attributes('-alpha', 1.0)
    
    root.resizable(width=False, height=False)

    columns = ("name", "phone", "comments")
    main_table = ttk.Treeview(columns=columns, show="headings")
    main_table.place(x=s.get_point(5), y=s.get_point(5))

    heads = ['Имя', 'Телефон', 'Комментарий']
    main_table['columns'] = heads
    for header in heads:
        main_table.heading(header, text=header, anchor='w')
    size = s.get_int_size(130)
    main_table.column("#1", stretch=NO, width=size)
    main_table.column("#2", stretch=NO, width=size)
    main_table.column("#3", stretch=NO, width=size)

    scrollbar = ttk.Scrollbar(orient=VERTICAL, command=main_table.yview)
    main_table.configure(yscroll=scrollbar.set)
    scrollbar.place(x=s.get_point(380), y=s.get_point(5))

    btn_search = tk.Button(root, text='Поиск', font='3', width=s.get_size(12), height = '1', border='0', command=lambda: open_find_window()) 
    btn_search.place(x=s.get_int_size(30), y=s.get_int_size(340))

    btn_do_it = tk.Button(root, text='Добавить', font='3', width=s.get_size(12), height='1', border='1', command=lambda: open_add_window()) 
    btn_do_it.place(x=1, y=s.get_point(340))
    btn_do_it.update()
    btn_do_it.place(x=s.get_point(s.MWW - 30) - btn_do_it.winfo_width())

    bs = s.get_button_size()
    bc1 = s.get_point(30)
    bc2 = s.get_point(160)
    bc3 = s.get_point(290)

    bl1 = s.get_point(420)
    image1 = tk.PhotoImage(file="./images/button.png")
    image2 = tk.PhotoImage(file="./images/button2.png")
    image3 = tk.PhotoImage(file="./images/button3.png")
    btn1 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image1)
    btn2 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image2) 
    btn3 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image3) 
    btn1.place(x=bc1, y=bl1) 
    btn2.place(x=bc2, y=bl1)
    btn3.place(x=bc3, y=bl1)
 
    bl2 = s.get_point(520)
    image4 = tk.PhotoImage(file="./images/button4.png")
    image5 = tk.PhotoImage(file="./images/button5.png")
    image6 = tk.PhotoImage(file="./images/button6.png")
    btn4 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image4) 
    btn5 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image5) 
    btn6 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image6) 
    btn4.place(x=bc1, y=bl2)
    btn5.place(x=bc2, y=bl2)
    btn6.place(x=bc3, y=bl2) 
 
    bl3 = s.get_point(620)
    image7 = tk.PhotoImage(file="./images/button7.png")
    image8 = tk.PhotoImage(file="./images/button8.png")
    image9 = tk.PhotoImage(file="./images/button9.png")
    btn7 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image7) 
    btn8 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image8) 
    btn9 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image9) 
    btn7.place(x=bc1, y=bl3)
    btn8.place(x=bc2, y=bl3) 
    btn9.place(x=bc3, y=bl3) 
 
    bl4 = s.get_point(720)
    imageX = tk.PhotoImage(file="./images/buttonX.png")
    image0 = tk.PhotoImage(file="./images/button0.png")
    imageM = tk.PhotoImage(file="./images/buttonM.png")
    btnX = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=imageX) 
    btn0 = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=image0) 
    btnM = tk.Button(root, width=bs, height=bs, border='0', bg='#000000', image=imageM) 
    btnX.place(x=bc1, y=bl4) 
    btn0.place(x=bc2, y=bl4) 
    btnM.place(x=bc3, y=bl4)
    model.read_file()
    root.mainloop()

def open_add_window():
    contact_window.start(None)

def open_find_window():
    find_window.start()
