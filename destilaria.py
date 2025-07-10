import mysql.connector
from destilaria_func import *

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",                                          
    password = "2006@Qwerty130469",
    database = "destilaria")
cursor = conexao.cursor()

janela = Tk()
janela.title('Sistema da Destilaria')
janela.geometry("600x400")
#Componentes da interface de cadastro
ttk.Label(janela, text='Nome:').grid(row=0, column=0, padx=5, pady=5)
ttk.Label(janela, text='Email:').grid(row=1, column=0, padx=5, pady=5)
#para criar o espaço branco de digitar
nome_entry = ttk.Entry(janela)
email_entry = ttk.Entry(janela)
#Grid para formatar
nome_entry.grid(row=0, column=1, padx=5, pady=5)
email_entry.grid(row=1, column=1, padx=5, pady=5)
#texto entre o grid e os botões
ttk.Label(janela, text="Botão pra ver o estoque:").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(janela, text="Botão pra ver os clientes cadastrados:").grid(row=1, column=2, padx=5, pady=5)


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

    #cadastro = f"INSERT INTO Cliente(nome_cliente, email) VALUES (%s, %s)", (nome, email)
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
    
#Botões da interface
ttk.Button(janela, command=ver_produtos, text="Ver produtos").grid(row=0, column=3, padx=5, pady=5)
ttk.Button(janela, command=ver_clientes, text="Ver clientes").grid(row=1, column=3, padx=5, pady=5)
ttk.Button(janela, command=cadastrar_cliente, text="Cadastrar cliente").grid(row=2, column=0, padx=0, pady=5)
ttk.Button(janela, command=excluir_cliente, text="Excluir cliente").grid(row=2, column=1, padx=0, pady=5)

janela.mainloop()

cursor.close()
conexao.close()