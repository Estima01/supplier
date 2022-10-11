import PySimpleGUI as sg
import json

def save_user(login, password):
    with open('login.json', 'w') as f:
        json.dump({'login': login, 'password': password}, f)


def load_user():
    with open('login.json', 'r') as f:
        return json.load(f)


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
    event, values = login()

    if event == 'Login':
        try:
            user = load_user()
            if user['login'] == values[0] and user['password'] == values[1]:
                sg.popup('Login efetuado com sucesso!')
                from main import *
                estoque()
                break
            else:
                sg.popup('Login ou senha inválidos')
        except FileNotFoundError:
            sg.popup('Usuário não cadastrado')
    elif event == 'Cadastrar':
        event, values = cadastro()
        if event == 'Cadastrar':
            save_user(values[0], values[1])
            sg.popup('Usuário cadastrado com sucesso')
        elif event == 'Cancelar':
            break
    elif event == 'Cancelar' or event == sg.WIN_CLOSED:
        break

