import sqlite3
import tkinter.messagebox as mb
from tkinter import *

# вход
def login_in():
    window.destroy()
    login_window = Tk()
    login_window.title('lab9')
    login_window.geometry('250x250')
    login_window.eval('tk::PlaceWindow . center')
    Label_login = Label(login_window, text='Введите логин:')
    entry_Login = Entry(login_window)
    Label_pass = Label(login_window, text='Введите пароль:')
    entry_pass = Entry(login_window)
    confirm = Button(login_window, text='Войти', command=lambda x=entry_Login, y=entry_pass, z=login_window: Check_login_in(x, y, z))
    Label_login.pack()
    entry_Login.pack()
    Label_pass.pack()
    entry_pass.pack()
    confirm.pack()
    login_window.mainloop()

# проверка
def Check_login_in(entyLogin, entypass, window):
    login = entyLogin.get()
    password = entypass.get()
    if login == '' or password == '':
        msg = 'Заполните все поля'
        mb.showerror("Ошибка", msg)
    else:
        con = sqlite3.connect('Databaze.sqlite')
        cur = con.cursor()
        cur.execute('create table if not exists Users(Login TEXT UNIQUE NOT NULL, Password TEXT NOT NULL) ')
        con.commit()
        cur.execute('SELECT * FROM Users')
        for i in cur.fetchall():
            if i[0] == login:
                if i[1] == password:
                    window.destroy()
                    finaly = Tk()
                    answer = Label(finaly, text='Вы успешно вошли!')
                    answer.pack()
                    finaly.geometry('250x250')
                    finaly.eval('tk::PlaceWindow . center')
                    finaly.mainloop()
                    exit()
                else:
                    msg = 'Пароли не совпадают'
                    mb.showerror("Ошибка", msg)
                    return
        msg = 'Такой пользователь не существует'
        mb.showerror("Ошибка", msg)

# регистрация
def Registr():
    window.destroy()
    reg_window = Tk()
    reg_window.title('lab9')
    reg_window.geometry('250x250')
    reg_window.eval('tk::PlaceWindow . center')
    Label_login = Label(reg_window, text='Введите логин:')
    entry_Login = Entry(reg_window)
    Label_pass = Label(reg_window, text='Введите пароль:')
    entry_pass = Entry(reg_window)
    confirm = Button(reg_window, text='Зарегистрироваться', command=lambda x=entry_Login, y=entry_pass, z=reg_window: Check_reg(x, y, z))
    Label_login.pack()
    entry_Login.pack()
    Label_pass.pack()
    entry_pass.pack()
    confirm.pack()
    reg_window.mainloop()

# проверка
def Check_reg(entyLogin, entypass, window):
    login = entyLogin.get()
    password = entypass.get()
    if login == '' or password == '':
        msg = 'Заполните все поля'
        mb.showerror("Ошибка", msg)
    else:
        con = sqlite3.connect('Databaze.sqlite')
        cur = con.cursor()
        cur.execute('create table if not exists Users(Login TEXT UNIQUE NOT NULL, Password TEXT NOT NULL) ')
        con.commit()
        cur.execute('SELECT * FROM Users')
        flag = 0
        for i in cur.fetchall():
            if i[0] == login:
                msg = 'Такой пользователь уже существует'
                mb.showerror("Ошибка", msg)
                flag = 1
        if flag == 0:
            window.destroy()
            finaly = Tk()
            answer = Label(finaly, text='Вы успешно зарегистрировались!')
            cur.execute("INSERT INTO Users(Login, Password) VALUES(?,?)", (login, password))
            con.commit()
            answer.pack()
            finaly.geometry('250x250')
            finaly.eval('tk::PlaceWindow . center')
            finaly.mainloop()
            exit()


window = Tk()
window.title('lab9')
window.geometry('250x250')
window.eval('tk::PlaceWindow . center')
Login = Button(window, text='Войти', command=login_in)
Reg = Button(window, text='Регистрация', command=Registr)
Login.pack()
Reg.pack()
window.mainloop()