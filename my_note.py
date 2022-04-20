from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

def new_file():
    global file_name
    file_name = 'Новая заметка'
    text.delete('1.0', END)

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except EXCEPTION:
        messagebox.showerror('Нельзя сохранить')

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

note = Tk()
note.title('Мои заметки')
note.geometry('500x500')

text = Text(note, width=500, height=500)
text.pack()

menu_bar = Menu(note)
file = Menu(menu_bar)

file.add_command(label='Новый', command=new_file)
file.add_command(label='Открыть', command=open_file)
file.add_command(label='Сохранить как', command=save_as)

menu_bar.add_cascade(label='Файл', menu=file)

note.config(menu=menu_bar)
note.mainloop()
