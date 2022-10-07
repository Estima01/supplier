#login.py
import PySimpleGUI as sg
import main

list = []
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
    layout = [[sg.Text('Cadastro')],
              [sg.Text('Login', size=(15, 1)), sg.InputText()],
              [sg.Text('Senha', size=(15, 1)), sg.InputText(password_char='*')],
              [sg.Submit('Cadastrar'), sg.Cancel('Cancelar')]]
    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def main():
    while True:
        event, values = login()
        if event in (None, 'Cancelar'):
            break
        elif event == 'Cadastrar':
            event, values = cadastro()
            if event in (None, 'Cancelar'):
                break
            else:
                list.append(values)
                print(list)
        else:
            print(values)
        if event == 'Login':
            if values in list:
                print('Login efetuado com sucesso!')
                import main
            else:
                print('Login ou senha incorretos!')


if __name__ == '__main__':
    main()
