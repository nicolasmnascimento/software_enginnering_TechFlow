# Estrutura de controle de vendas

# Dicionário de estoque inicial
estoque_id = {
    "Manga": {"preco": 3.50, "quantidade": 10},
    "Laranja": {"preco": 10.00, "quantidade": 20},
    "Goiaba": {"preco": 5.60, "quantidade": 6},
    "Morango": {"preco": 7.00, "quantidade": 12},
    "Uva": {"preco": 15.00, "quantidade": 30},
    "Limão": {"preco": 3.50, "quantidade": 90}
}

# Função para cadastrar um novo produto
def cadastrar_produto(nome, quantidade, preco):
    if nome in estoque_id:
        print(f"Produto '{nome}' já existe no estoque!")
    else:
        estoque_id[nome] = {"preco": preco, "quantidade": quantidade}
        print(f"Produto '{nome}' cadastrado com sucesso!")

# Função para atualizar um produto existente
def atualizar_produto(nome, quantidade, preco):
    if nome not in estoque_id:
        print(f"Produto '{nome}' não encontrado no estoque!")
    else:
        estoque_id[nome] = {"preco": preco, "quantidade": quantidade}
        print(f"Produto '{nome}' atualizado com sucesso!")

# Função para consultar o estoque de um produto
def consultar_produto(nome):
    if nome in estoque_id:
        produto = estoque_id[nome]
        return f"Produto: {nome}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}"
    else:
        return f"Produto '{nome}' não encontrado no estoque!"

# Função para visualizar todo o estoque
def visualizar_estoque():
    return estoque_id




    