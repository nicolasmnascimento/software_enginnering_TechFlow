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
