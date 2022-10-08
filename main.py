import PySimpleGUI as sg

produto = []
quantidade = []
preco = []
contact_information = []

def estoque():
    layout = [[sg.Text('Estoque')],
    [sg.Table(values=contact_information, 
    headings=['Produto','Quantidade','Preço'],
    max_col_width=25, 
    auto_size_columns=False,
    justification='center', 
    num_rows=20,
    alternating_row_color='lightblue',
    key='-TABLE-',
    tooltip='This is a table')],
    [sg.Button('Cadastrar'), sg.Button('Editar'), sg.Button('Excluir'), sg.Button('Sair')]]
                
    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def cadastro_produto():
    layout = [[sg.Text('Cadastro de produtos')],
    [sg.Text('Nome do produto', size=(15,1)), sg.InputText()],
    [sg.Text('Quantidade', size=(15,1)),sg.InputText()],
    [sg.Text('Código', size=(15,1)), sg.InputText()],
    [sg.Button('Cadastra'), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values



while True:
    event, values = estoque()
    if event == 'Cadastrar':
        event, values = cadastro_produto()
        if event == 'Cadastra':
            produto.append(values[0])
            quantidade.append(values[1])
            preco.append(values[2])
            contact_information.append([produto[0],quantidade[0],preco[0]])
            produto.pop(0)
            quantidade.pop(0)
            preco.pop(0)
    elif event == 'Editar':
        sg.popup('Em construção')
    elif event == 'Excluir':
        sg.popup('Em construção')
    elif event == 'Sair' or event == sg.WIN_CLOSED:
        break
