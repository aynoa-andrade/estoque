#almoxarifado.py

class Almoxarifado:
# Construtor: o almoxarifado nasce com o nome da unidade e sem produtos
    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []

# Guarda um objeto Produto no fim da lista
    def adicionar(self, produto):
        self.produtos.append(produto)

 # Busca um produto pelo código informado
    def buscar(self, codigo):
     for p in self.produtos:     # Percorre todos os produtos da lista
        if p.codigo == codigo:   # Verifica se o código do produto é igual ao código procurado
            return p

     return None

# Adiciona uma quantidade ao estoque de um produto
    def entrada(self, codigo, qtd):
     p = self.buscar(codigo)   # Busca o produto pelo código informado
     if p is None:       # Verifica se o produto não foi encontrado
      return False
    
     p.entrada(qtd)    # Se encontrou, chama o método entrada() da classe Produto
     return True   # Informa que a operação deu certo

# Retira uma quantidade do estoque de um produto
    def saida(self, codigo, qtd):

        # Busca o produto pelo código informado
        p = self.buscar(codigo)

        # Verifica se o produto não foi encontrado
        if p is None:
            return False
        return p.saida(qtd)

    # Lista todos os produtos do almoxarifado
    def listar(self):
       lista = []

       for p in self.produtos:
          lista.append(p.listar_produtos())
          return lista

    # Monta a solicitação de compra
    def solicitacao_compra(self):
       pedido = []

       for p in self.produtos:
          if p.situacao()  != "OK":
             item = {
                "codigo": p.codigo,
                "nome": p.listar_produtos()["nome"],
                "situacao": p.situacao()
             }

             pedido.append(item)
             return pedido

    # Calcula o valor total do estoque
    def valor_estoque(self):
       total = 0

       for p in self.produtos:
          total += p.quantidade * p.preco
          return total

    # Devolve os dados completos do almoxarifado em um dicionário
    def para_dicionario(self):
       d = {
          "unidade": self.unidade,
          "total_produtos": self.produtos,
          "produtos": self.listar()
       }

       return d