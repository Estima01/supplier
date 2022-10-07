from turtle import heading
import PySimpleGUI as sg

contact_information = []
#gestor de estoque


layout = [[sg.Text('Estoque')], [sg.Table(values=contact_information, 
headings=['Produto','Quantidade','Preço'],
justification='center',
num_rows=20,
alternating_row_color='lightblue',
key='-TABLE-', tooltip='This is a table')],
[sg.Button('Cadastrar'), sg.Button('Editar'), sg.Button('Excluir'), sg.Button('Sair')]]
              
window = sg.Window('+Supplier', layout)
event, values = window.read()
window.close()

def cadastrar():
    layout = [[sg.Text('Cadastro de Produto')],
              [sg.Text('Produto', size=(15, 1)), sg.InputText()],
              [sg.Text('Quantidade', size=(15, 1)), sg.InputText()],
              [sg.Text('Preço', size=(15, 1)), sg.InputText()],
              [sg.Submit('Cadastrar'), sg.Cancel('Cancelar')]]
    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values
while True:
    if event == "Cadastrar Produto":
        cadastrar()
        print(contact_information)
        
    elif event == sg.WIN_CLOSED or event == 'Voltar':
        break
