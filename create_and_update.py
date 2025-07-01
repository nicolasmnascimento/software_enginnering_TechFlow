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
