# Controle de Estoque

Este arquivo contém a lógica central para o controle de estoque do sistema de gestão de produtos. Ele é utilizado como módulo de backend para manipulação dos dados de estoque, sendo integrado por outros arquivos Python.

## Metodologia

A metodologia adotada seria de um trabalho de maior transparência aos colaboradores envolvidos e a criação de um paínel liberal, o **Kanban** foi a metodologia escolhida pela sua facilidade e transparência necessária ao projeto.

## Requisitos

### Funcionais
- **Autenticação de usuário:** Deve permitir um login por meio de um campo de usuário e senha;
- **Cadastro de Produtos:** Permissão de criar novos produtos dentro da base de dados do sistema;
- **Consulta de Produtos:** Deve permitir consultas dos cadastros a partir de um arquivo externo exportado automaticamente.
  
### Não Funcionais
- **Interface Gráfica:** O sistema deve ter uma interface gráfica amigável construída com a biblioteca `tkinter`;
- **Exportação de Dados:** O sistema deve realizar a exportação de dados para análise externa;
- **Segurança Básica:** A senha digitada deve ser mascarada `show="*"`, mesmo que a validação de senha seja simples (sem criptografia).

## Modelagem UML

### Diagrama de uso
![image](https://github.com/user-attachments/assets/71833baa-b7bc-462a-865b-995603533946)

### Diagrama de classes


## Estrutura do Estoque

O estoque é representado por um dicionário Python chamado `estoque_id`, onde cada chave é o nome de um produto e o valor é outro dicionário com as informações de preço e quantidade:

```python
estoque_id = {
    "Manga": {"preco": 3.50, "quantidade": 10},
    "Laranja": {"preco": 10.00, "quantidade": 20},
    ...
}
```
## Utilização de CRUD

Para realização de um trabalho mais fluído dentro do código, foi determinado a criação de um CRUD, tendo em vista as seguintes ações:

### 1. cadastrar_produto(nome, quantidade, preco)
Cadastra um novo produto no estoque.
Se o produto já existir, exibe uma mensagem informando.
Caso contrário, adiciona o produto ao dicionário estoque_id.

### 2. atualizar_produto(nome, quantidade, preco)
Atualiza as informações de um produto já existente.
Se o produto não existir, exibe uma mensagem de erro.
Caso contrário, atualiza o preço e a quantidade.

### 3. consultar_produto(nome)
Consulta as informações de um produto específico.
Retorna uma string com o nome, preço e quantidade do produto.
Se o produto não existir, retorna uma mensagem de erro.

### 4. visualizar_estoque()
Retorna o dicionário completo do estoque, permitindo visualizar todos os produtos cadastrados.

## Tkinter - Criação de Interface
Para realização externa do trabalho de consulta e suas integrações, foi pensado a criação de uma Interface. Visando algo mais intuitivo e de melhor utilização do usuário final, o cliente

- Consulta de produtos vinculadas a uma criação de Arquivo CSV externamente do Vscode.
  ```python
   # Método para consultar produtos
    def consultar_produtos(self):
        # Converte o dicionário estoque_id em um DataFrame
        estoque = pd.DataFrame.from_dict(estoque_id, orient="index")
        estoque.reset_index(inplace=True)
        estoque.rename(columns={"index": "Produto", "preco": "Preço", "quantidade": "Quantidade"}, inplace=True)

        # Salva o DataFrame em um arquivo CSV
        estoque.to_csv("estoque.csv", index=False)
        print("Exportando base de consulta de produtos para 'estoque.csv'...")
  ```
- Cadastro de produtos internamente, solicitando as seguintes informações:
  -  Produto;
  -  Preço;
  -  Quantidade.
```python
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
```
 
 A sintaxe utilizada é a mesma que foi utilizada para criação na base.py, a única coisa que se diferencia é que Tkinter e ela se complementam dentro do processo para que não haja barreiras. 
```python
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
```
  
