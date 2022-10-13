import PySimpleGUI as sg
import sqlite3 as sql

def create_table():
    conn = sql.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users(login TEXT, senha TEXT)')
    conn.commit()
    conn.close()

def create_user(login, senha):
    conn = sql.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users VALUES(?,?)', (login, senha))
    conn.commit()
    conn.close()

def login_user(login, senha):
    conn = sql.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE login=? AND senha=?', (login, senha))
    rows = c.fetchall()
    conn.close()
    return rows



def login():
    layout = [[sg.Text('Informação de login')],
              [sg.Text('Login', size=(15, 1)), sg.InputText()],
              [sg.Text('Senha', size=(15, 1)), sg.InputText(password_char='*')],
              [sg.Submit('Login'), sg.Cancel('Cancelar'), sg.Button('Cadastrar')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def cadastro():
    layout = [[sg.Text('Cadastro de Usuário')],
              [sg.Text('Login', size=(15, 1)), sg.InputText()],
              [sg.Text('Senha', size=(15, 1)), sg.InputText(password_char='*')],
              [sg.Submit('Cadastrar'), sg.Cancel('Cancelar')]]
    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

while True:
    create_table()
    event, values = login()
    if event == 'Login':
        if login_user(values[0], values[1]):
            sg.popup('Logado com sucesso')
            from main import *
            break
        else:
            sg.popup('Login ou senha incorretos')
    elif event == 'Cadastrar':
        event, values = cadastro()
        if event == 'Cadastrar':
            create_user(values[0], values[1])
            sg.popup('Usuário cadastrado com sucesso')
        elif event == 'Cancelar':
            break
    elif event == 'Cancelar' or event == sg.WIN_CLOSED:
        break

