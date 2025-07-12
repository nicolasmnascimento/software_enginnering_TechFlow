from tkinter import *
import pandas as pd
import sqlite3
from base import estoque_id, cadastrar_produto  # Importa as funções e o estoque do base.py


class aplicacao:
    # Chamando a criação da interface
    def __init__(self):    
        self.layout = Tk()
        # Adicionando Título à interface
        self.layout.title("Controle de Estoque do Nicolas")
        # Adicionando tamanho da interface
        self.layout.geometry("200x500")
        # Referenciando a tela para adição de informações
        self.tela = Frame(self.layout)

        # Criação do texto que vai aparecer
        self.login = Label(self.tela, text="Login: ")
        self.login.place(x=0, y=10)
        self.campo_login = Entry(self.tela)
        self.campo_login.place(x=55, y=10)

        self.senha = Label(self.tela, text="Senha: ")
        self.senha.place(x=45, y=50)
        self.campo_senha = Entry(self.tela, show="*")
        self.campo_senha.place(x=55, y=50)

        # Botão Confirmar com comando para chamar o método bloqueio
        self.confirma = Button(self.tela, text="Confirmar", command=self.bloqueio)
        self.confirma.place(x=0, y=90)

        # Colocando na tela tudo que irá aparecer
        self.tela.pack()
        self.login.pack()
        self.campo_login.pack()
        self.senha.pack()
        self.campo_senha.pack()
        self.confirma.pack()

        mainloop()

    # Método que chama os dois bloqueios
    def bloqueio(self):
        login = self.campo_login.get()
        senha = self.campo_senha.get()

        if login == "76312" and senha == "12345":
            self.abrir_tela_admin()
        elif login == "13052003" and senha == "12345":
            self.abrir_tela_usuario()
        else:
            print("Login ou senha incorretos.")

    # Método para abrir a tela de administrador
    def abrir_tela_admin(self):
        admin_tela = Toplevel(self.layout)
        admin_tela.title("Administrador")
        admin_tela.geometry("300x200")
        Label(admin_tela, text="Bem-vindo, Administrador!").pack()
        Button(admin_tela, text="Cadastrar Produto", command=self.cadastrar_produto).pack()
        Button(admin_tela, text="Consultar Produtos", command=self.consultar_produtos).pack()

    # Método para abrir a tela de usuário
    def abrir_tela_usuario(self):
        usuario_tela = Toplevel(self.layout)
        usuario_tela.title("Usuário Comum")
        usuario_tela.geometry("300x200")
        Label(usuario_tela, text="Bem-vindo, Usuário!").pack()
        Button(usuario_tela, text="Consultar Produtos", command=self.consultar_produtos).pack()

    # Método para cadastrar produto
    def cadastrar_produto(self):
        cadastro_tela = Toplevel(self.layout)
        cadastro_tela.title("Cadastrar Produto")
        cadastro_tela.geometry("300x300")

        Label(cadastro_tela, text="Nome do Produto:").pack()
        nome_produto = Entry(cadastro_tela)
        nome_produto.pack()

        Label(cadastro_tela, text="Quantidade:").pack()
        quantidade_produto = Entry(cadastro_tela)
        quantidade_produto.pack()

        Label(cadastro_tela, text="Preço:").pack()
        preco_produto = Entry(cadastro_tela)
        preco_produto.pack()

        def salvar_produto():
            nome = nome_produto.get()
            quantidade = quantidade_produto.get()
            preco = preco_produto.get()

            if not nome:
                print("Erro: O nome do produto não pode estar vazio.")
            elif not quantidade.isdigit():
                print("Erro: A quantidade deve ser um número inteiro.")
            elif not preco.replace('.', '', 1).isdigit():
                print("Erro: O preço deve ser um número válido.")
            else:
                cadastrar_produto(nome, int(quantidade), float(preco))  # Chama a função do base.py
                print(f"Produto '{nome}' cadastrado com sucesso!")
                cadastro_tela.destroy()

        Button(cadastro_tela, text="Salvar", command=salvar_produto).pack()

    # Método para consultar produtos
    def consultar_produtos(self):
        # Converte o dicionário estoque_id em um DataFrame
        estoque = pd.DataFrame.from_dict(estoque_id, orient="index")
        estoque.reset_index(inplace=True)
        estoque.rename(columns={"index": "Produto", "preco": "Preço", "quantidade": "Quantidade"}, inplace=True)

        # Salva o DataFrame em um arquivo CSV
        estoque.to_csv("estoque.csv", index=False)
        print("Exportando base de consulta de produtos para 'estoque.csv'...")

        # Adiciona os dados ao banco de dados SQLite
        conn = sqlite3.connect("estoque.db")
        estoque.to_sql("estoque", conn, if_exists="replace", index=False)
        conn.close()
        print("Dados exportados para o banco de dados SQLite 'estoque.db'.")


# Instanciando a aplicação
tl = aplicacao()