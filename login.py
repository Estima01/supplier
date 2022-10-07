import PySimpleGUI as sg

list = ['x','x']
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
        if values[0] == list[0] and values[1] == list[1]:
            sg.popup('Login efetuado com sucesso!')
            from main import estoque
            estoque()
            break
        else:
            sg.popup('Login ou senha incorretos')
    if event == 'Cadastrar':
        event, values = cadastro()
        if event == 'Cadastrar':
            list.append(values[0])
            list.append(values[1])
            list.pop(0)
            list.pop(0) 
            sg.popup('Cadastro efetuado com sucesso!')
            print(list)
    elif event == sg.WIN_CLOSED or event == 'Cancelar':
        break