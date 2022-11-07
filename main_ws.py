import PySimpleGUIWx as sg
import sqlite3 as sql
import os
from barcode import EAN13
from barcode.writer import ImageWriter
import qrcode as qr


def create_table(): #criação da tabela de estoque
    conn = sql.connect('estoque.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS estoque(codigo int NOT NULL, produto TEXT, quantidade INTEGER, preco_unitario REAL, preco_total REAL, PRIMARY KEY(codigo))')
    conn.commit()
    conn.close()

def view(): #visualização da tabela de estoque
    conn = sql.connect('estoque.db')
    c = conn.cursor()
    c.execute('SELECT * FROM estoque')
    rows = c.fetchall()
    conn.close()
    return rows

def valor(): #exibição do valor na tela principal
    conn = sql.connect('estoque.db')
    c = conn.cursor()
    c.execute('SELECT SUM(preco_total) FROM estoque')
    rows = c.fetchall()
    conn.close()
    for i in rows:
        if i[0] == None:
            return '0,00'
        return i[0]

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
    [sg.Button('Cadastrar'), sg.Button('Editar'), sg.Button('Excluir'), sg.Button('Gerar código de barras ou QR code'),sg.Button('Sair')]]

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
    [sg.Text('Imagem do produto', size=(15,1)), sg.InputText(), sg.FileBrowse()],
    [sg.Button('Cadastrar'), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values


def editar_produto(): #tela de edição de itens no estoque
    layout = [[sg.Text('Editar produtos')],
    [sg.Text('Código', size=(15,1)), sg.InputText()],
    [sg.Text('Nome do produto', size=(15,1)), sg.InputText()],
    [sg.Text('Quantidade', size=(15,1)),sg.InputText()],
    [sg.Text('Preço', size=(15,1)), sg.InputText()],
    [sg.Text('Imagem do produto', size=(15,1)), sg.InputText(), sg.FileBrowse()],
    [sg.Button('Editar'), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def excluir_produto(): #tela de exclusão de itens no estoque
    layout = [[sg.Text('Excluir produtos')],
    [sg.Text('Código', size=(15,1)), sg.InputText()],
    [sg.Button('Excluir'), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values

def gerar_codigo(): #tela de geração de código de barras e QR code
    layout = [[sg.Text('Gerar código de barras ou QR code')],
    [sg.Text('Código', size=(15,1)), sg.InputText()],
    [sg.Button('Gerar código de barras'),sg.Button('Gerar QR Code'),sg.Button('Gerar todos códigos de barra'),sg.Button('Gerar todos QR Code'), sg.Button('Sair')]]

    window = sg.Window('+Supplier', layout)
    event, values = window.read()
    window.close()
    return event, values


while True:
    create_table()
    event, values = estoque()
    if event == 'Cadastra':
        event, values = cadastro_produto()
        if event == 'Cadastrar':
            conn = sql.connect('estoque.db')
            c = conn.cursor()
            c.execute('INSERT INTO estoque VALUES (:codigo, :produto, :quantidade, :preco_unitario, :preco_total)', {
                'codigo': values[0],
                'produto': values[1],
                'quantidade': values[2],
                'preco_unitario': values[3],
                'preco_total': float(values[2]) * float(values[3])
            })
            conn.commit()
            conn.close()
            sg.popup('Produto cadastrado com sucesso!')
    elif event == 'Editar':
        event, values = editar_produto()
        if event == 'Editar':
            conn = sql.connect('estoque.db')
            c = conn.cursor()
            c.execute('UPDATE estoque SET produto = :produto, quantidade = :quantidade, preco_unitario = :preco_unitario, preco_total = :preco_total WHERE codigo = :codigo', {
                'codigo': values[0],
                'produto': values[1],
                'quantidade': values[2],
                'preco_unitario': values[3],
                'preco_total': float(values[2]) * float(values[3])
            })
            conn.commit()
            conn.close()
            sg.popup('Produto editado com sucesso!')
    elif event == 'Excluir':
        event, values = excluir_produto()
        if event == 'Excluir':
            conn = sql.connect('estoque.db')
            c = conn.cursor()
            c.execute('DELETE FROM estoque WHERE codigo = :codigo', {
                'codigo': values[0]
            })
            conn.commit()
            conn.close()
            sg.popup('Produto excluído com sucesso!')
    elif event == 'Gerar código de barras ou QR code':
        event, values = gerar_codigo()
        if event == 'Gerar código de barras':
            codigo_barras = EAN13(values[0], writer=ImageWriter())
            codigo_barrastransformado = codigo_barras.save("codigo")
            sg.popup('Código gerado com sucesso')
        elif event == 'Gerar todos códigos de barra':
            conn = sql.connect('estoque.db')
            c = conn.cursor()
            c.execute('SELECT codigo FROM estoque')
            codigos = c.fetchall()
            for i in codigos:
                codigo_barras = EAN13(str(i[0]), writer=ImageWriter())
                codigo_barrastransformado = codigo_barras.save("{} - codigo".format(i[0]))
            sg.popup('Códigos gerados com sucesso')
        elif event == 'Gerar QR Code':
            gerar_qr = qr.make(values[0])
            gerar_qr.save("prod_{}_qr.png".format(values[0]))
            sg.popup('QR Code gerado com sucesso')
        elif event == 'Gerar todos QR Code':
            conn = sql.connect('estoque.db')
            c = conn.cursor()
            c.execute('SELECT codigo FROM estoque')
            codigos = c.fetchall()
            for i in codigos:
                gerar_qr = qr.make(str(i[0]))
                gerar_qr.save("prod_{}_qr.png".format(i[0]))
            sg.popup('QR Codes gerados com sucesso')
    elif event == 'Sair' or event == sg.WIN_CLOSED:
        break


