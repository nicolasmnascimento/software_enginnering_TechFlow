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
