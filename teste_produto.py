# teste_produto.py
from produto import Produto

# daqui para baixo, a classe
# ja pode ser usada

p1 = Produto()
p1.nome = "Macarrão parafuso"
p1.quantidade = 5

p2 = Produto()
p2.nome = "Molho de tomate"
p2.quantidade = 3

print(f"{p1.nome}: {p1.quantidade} un")
print(f"{p2.nome}: {p2.quantidade} un")
