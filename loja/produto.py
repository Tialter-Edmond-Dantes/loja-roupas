TAMANHOS = ("PP", "P", "M", "G", "GG")

vitrine = [
    {"nome": "Camiseta básica", "preco": 39.90, "tamanho": "M"},
    {"nome": "Calça jeans", "preco": 129.90, "tamanho": "G"},
    {"nome": "Moletom", "preco": 159.90, "tamanho": "P"},
]

carrinho = [("Camiseta básica", 3), ("Calça jeans", 1)]


class Produto:
    def __init__(self, nome, preco, tamanho):
        if not nome or not nome.strip():
            raise ValueError("nome do produto não pode ser vazio")

        if preco <= 0:
            raise ValueError("preço do produto deve ser maior que zero")

        if tamanho not in TAMANHOS:
            raise ValueError(f"tamanho inválido: {tamanho}")

        self.nome = nome.strip()
        self.preco = preco
        self.tamanho = tamanho

    def descricao(self):
        return f"{self.nome} {self.tamanho}: R$ {self.preco:.2f}"
