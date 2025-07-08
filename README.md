# Controle de Estoque

Este arquivo contém a lógica central para o controle de estoque do sistema de gestão de produtos. Ele é utilizado como módulo de backend para manipulação dos dados de estoque, sendo integrado por outros arquivos Python.

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
Para realização externa do trabalho de consulta e suas integrações, foi pensado a criação de uma Interface.

- Consulta de Ativos vinculadas a uma criação de Arquivo CSV externamente do Vscode.
  
- Cadastro de produtos internamente, solicitando as seguintes informações:
  -  Produto;
  -  Preço;
  -  Quantidade.

  
