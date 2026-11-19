#produtos.py

class Produto:
    # Construtor
    def __init__(self, codigo=None, nome=None, quantidade=0, preco=0.0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    # Situação do produto
    def situacao(self):
        if self.quantidade == 0:
            return "Em falta"
        elif self.quantidade <= 4:
            return "Repor"
        else:
            return "OK"

    # Devolve os dados em um dicionário
    def listar_produtos(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "situacao": self.situacao()
        }

    # Entrada de produtos
    def entrada(self, qtd):
        self.quantidade = self.quantidade + qtd

    # Saída de produtos
    def saida(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade = self.quantidade - qtd
            return True
        else:
            return False
