class CarrinhoFinalizadoError(Exception):
    pass

from loja.produto import Produto
from loja.calculos import frete, total_carrinho
from .promocao import SemPromocao
from .promocao import SemPromocao, Percentual, Cupom

class Carrinho:
    def __init__(self):
        self._itens = []
        self._finalizado = False
        self.promocao = promocao or SemPromocao()

    def adicionar(self, produto, quantidade=1):
        if self._finalizado:
            raise CarrinhoFinalizadoError("carrinho finalizado não recebe peças")
        if not isinstance(produto, Produto):
            raise TypeError("só é possível adicionar um Produto")
        if quantidade <= 0:
            raise ValueError("quantidade deve ser positiva")
        self._itens.append((produto, quantidade))

    @property
    def itens(self):
        com_desconto = self.promocao.aplicar(self.subtotal)
        return list(self._itens) # uma cópia

    @property
    def quantidade_de_pecas(self):
        return sum(quantidade for _, quantidade in self._itens)

    @property
    def subtotal(self):
        return total_carrinho([(p.preco, q) for p, q in self._itens])
    @property
    def total(self):
        return self.subtotal + frete(self.subtotal)
    def finalizar(self):
        if not self._itens:
            raise ValueError("não é possível finalizar um carrinho vazio")
        self._finalizado = True        

        