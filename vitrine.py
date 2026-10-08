# Etapa 2: os dados da loja em tipos e coleções (aula 3)

# tupla: a lista de tamanhos não muda
TAMANHOS = ("PP", "P", "M", "G", "GG")

# lista de dicionários: um por produto
vitrine = [
    {"nome": "Camiseta básica", "preco": 39.90, "tamanhos": "M"},
    {"nome": "Calça jeans", "preco": 129.90, "tamanhos": "G"},
    {"nome": "Moletom", "preco": 159.90, "tamanhos": "P"},
] 

# lista de pares (nome,quatidades)
carrinho = [("Camiseta básica", 3), ("Calça jeans", 1)]

# dicionário: nome -> preço
precos = {}
for produto in vitrine:
    precos[produto["nome"]] = produto["preco"]

total = 0
for nome, quantidade in carrinho:
    total = total + precos[nome] * quantidade

print("peças na vitrine:",  len(vitrine))
print("Total do carrinho: R$", round(total, 2))

print(vitrine[1]["preco"])
print(TAMANHOS[-1])
print(len(carrinho))
print(precos["Moletom"] * 2)
