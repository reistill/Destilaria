import mysql.connector
from tkinter import *
from tkinter import ttk
from destilaria import nome_entry, email_entry 

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2006@Qwerty130469",
    database = "destilaria")
cursor = conexao.cursor()

#Funções que serão usadas nos botões da janela/interface
def ver_produtos():
    listar_produto = "SELECT * FROM Produto"
    cursor.execute(listar_produto)
    listagem1 = cursor.fetchall()
    return print(listagem1)

def ver_clientes():
    listar_cliente = "SELECT * FROM Cliente"
    cursor.execute(listar_cliente)
    listagem2 = cursor.fetchall()
    return print(listagem2)

def cadastrar_cliente():
    nome = nome_entry.get()
    email = email_entry.get()
    
    print(f"Usuário {nome} do respectivo email: {email} cadastrado!")

    comando = "INSERT INTO Cliente(nome_cliente, email) VALUES (%s, %s)"
    valor = (nome, email)
    cursor.execute(comando, valor)
    conexao.commit()

def excluir_cliente():
    nome = nome_entry.get()
    email = email_entry.get()

    print(f"Usuário {nome} do respectivo email: {email} excluído!")

    comando = "DELETE FROM Cliente WHERE nome_cliente = %s AND email = %s"
    valor = (nome, email)
    cursor.execute(comando, valor)
    conexao.commit()