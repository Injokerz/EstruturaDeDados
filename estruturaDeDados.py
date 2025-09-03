import Les

l = Les.Les(5)

l.inserir_fim('A')
l.inserir_fim('B')
l.inserir_fim('C')

l.show()
print('esperado A B C')

l.remover_fim()

l.show()
print('esperado A B ')

l.inserir_fim('D')

l.show()
print('esperado A B D')

l.remover('B')

l.show()
print('esperado A D')