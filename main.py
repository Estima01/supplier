import PySimpleGUI as sg
import sqlite3 as sql
from barcode import EAN13
from barcode.writer import ImageWriter

def create_table(): #criação da tabela de estoque
    conn = sql.connect('estoque.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS estoque(codigo INTEGER, produto TEXT, quantidade INTEGER, preco_unitario REAL, preco_total REAL)')
    conn.commit()
    conn.close()


def view(): #visualização da tabela de estoque
    conn = sql.connect('estoque.db')
    c = conn.cursor()
    c.execute('SELECT * FROM estoque')
    rows = c.fetchall()
    conn.close()
    return rows

def valor():
    conn = sql.connect('estoque.db')
    c = conn.cursor()
    c.execute('SELECT SUM(preco_total) FROM estoque')
    rows = c.fetchall()
    conn.close()
    for i in rows:
        if i[0] == None:
            return '0,00'
        return i[0]


#--------------------------------------------------------------#

def estoque(): #tela do estoque
    layout = [[sg.Text('Estoque')],
    [sg.Table(values=view(), 
    headings=['Código','Produto','Quantidade','Preço Unitário','Preço Total'],
    max_col_width=25, 
    auto_size_columns=False,
    justification='center', 
    num_rows=20,
    key='-TABLE-',
    tooltip='This is a table')],
    [sg.Text('Total em mercadoria: R$') ,sg.Text(valor(), size=(15,1), key='-TOTAL-')],
    [sg.Button('Cadastrar'), sg.Button('Editar'), sg.Button('Excluir'), sg.Button('Gerar código de barras'),sg.Button('Gerar QR Code'),sg.Button('Sair')]]
                
    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def cadastro_produto(): #tela de cadastro de itens no estoque
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

def excluir(): #tela de exclusão de itens no estoque
    layout = [[sg.Text('Excluir')],
    [sg.Text('Código do produto', size=(15,1)), sg.InputText()],
    [sg.Button('Excluir'), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def editar(): #tela de edição de itens no estoque
    layout = [[sg.Text('Editar')],
    [sg.Text('Código do produto', size=(15,1)), sg.InputText()],
    [sg.Text('Nome do produto', size=(15,1)), sg.InputText()],
    [sg.Text('Quantidade', size=(15,1)), sg.InputText()],
    [sg.Text('Preço', size=(15,1)), sg.InputText()],
    [sg.Button('Editar'), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def gerar_codigo(): #tela de geração de código de barras
    layout = [[sg.Text('Gerar código de barras')],
    [sg.Text('Código do produto', size=(15,1)), sg.InputText()],
    [sg.Button('Gerar um codigo'),sg.Button("Gerar todos códigos"), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

#Menu principal

while True:
    create_table()
    event, values = estoque()
    if event == 'Cadastrar':
        event, values = cadastro_produto()
        if event == 'Cadastra':
            conn = sql.connect('estoque.db')
            c = conn.cursor()
            c.execute('INSERT INTO estoque VALUES (:codigo, :produto, :quantidade, :preco_unitario, :preco_total)', {'codigo': values[0], 'produto': values[1], 'quantidade': values[2], 'preco_unitario': values[3], 'preco_total': float(values[2]) * float(values[3])})
            conn.commit()
            conn.close()
            sg.popup('Produto cadastrado com sucesso')
    elif event == 'Editar':
        event, values = editar()
        if event == 'Editar':
            conn = sql.connect('estoque.db')
            c = conn.cursor()
            c.execute('UPDATE estoque SET produto = :produto, quantidade = :quantidade, preco_unitario = :preco WHERE codigo = :codigo', {'codigo': values[0], 'produto': values[1], 'quantidade': values[2], 'preco': values[3], 'preco_total': float(values[2]) * float(values[3])})
            conn.commit()
            conn.close()
            sg.popup('Produto editado com sucesso')    
    elif event == 'Excluir':
        event, values = excluir()
        if event == 'Excluir':
            conn = sql.connect('estoque.db')
            c = conn.cursor()
            c.execute('DELETE FROM estoque WHERE codigo = :codigo', {'codigo': values[0]})
            conn.commit()
            conn.close()
            sg.popup('Produto excluído com sucesso')
    elif event == 'Gerar código de barras':
        event, values = gerar_codigo()
        if event == 'Gerar um codigo':
            codigo_barras = EAN13(values[0], writer=ImageWriter())
            codigo_barrastransformado = codigo_barras.save("codigo")
            sg.popup('Código gerado com sucesso')
        elif event == 'Gerar todos códigos':
            conn = sql.connect('estoque.db')
            c = conn.cursor()
            c.execute('SELECT codigo FROM estoque')
            codigos = c.fetchall()
            for i in codigos:
                codigo_barras = EAN13(str(i[0]), writer=ImageWriter())
                codigo_barrastransformado = codigo_barras.save("{} - codigo".format(i[0]))
            sg.popup('Códigos gerados com sucesso')
    elif event == 'Gerar QR Code':
        sg.poup('Em desenvolvimento')

    elif event == 'Sair' or event == sg.WIN_CLOSED:
        from login import *
        break