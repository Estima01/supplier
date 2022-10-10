import PySimpleGUI as sg
codigo = []
produto = []
quantidade = []
preco = []

contact_information = []

def estoque():
    layout = [[sg.Text('Estoque')],
    [sg.Table(values=contact_information, 
    headings=['Código','Produto','Quantidade','Preço'],
    max_col_width=25, 
    auto_size_columns=False,
    justification='center', 
    num_rows=20,
    key='-TABLE-',
    tooltip='This is a table')],
    [sg.Button('Cadastrar'), sg.Button('Editar'), sg.Button('Excluir'), sg.Button('Sair')]]
                
    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def cadastro_produto():
    layout = [[sg.Text('Cadastro de produtos')],
    [sg.Text('Código', size=(15,1)), sg.InputText()],
    [sg.Text('Nome do produto', size=(15,1)), sg.InputText()],
    [sg.Text('Quantidade', size=(15,1)),sg.InputText()],
    [sg.Text('Preço', size=(15,1)), sg.InputText()],
    [sg.Button('Cadastra'), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def excluir():
    layout = [[sg.Text('Excluir')],
    [sg.Text('Código do produto', size=(15,1)), sg.InputText()],
    [sg.Button('Excluir'), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values


while True:
    event, values = estoque()
    if event == 'Cadastrar':
        event, values = cadastro_produto()
        if event == 'Cadastra':
            codigo.append(values[0])
            produto.append(values[1])
            quantidade.append(values[2])
            preco.append(values[3])
            contact_information.append([codigo[0],produto[0],quantidade[0],preco[0]])
            produto.pop(0)
            quantidade.pop(0)
            preco.pop(0)
            codigo.pop(0)
    elif event == 'Editar':
        sg.popup('Em desenvolvimento')
    elif event == 'Excluir':
        event, values = excluir()
        if event == 'Excluir':
            for i in range(len(contact_information)):
                if values[0] == contact_information[i][0]:
                    contact_information.pop(i)
                    sg.popup('Produto excluido com sucesso')
        elif event == 'Sair':
            break
    elif event == 'Sair' or event == sg.WIN_CLOSED:
        break
