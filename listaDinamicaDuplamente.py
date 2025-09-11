import Ldde
l = Ldde.Ldde()

l.inserir_inicio('A')
l.inserir_inicio('B')
l.inserir_inicio('C')
l.inserir_inicio('D')

# l.show()
# print('Esperado D C B A')

# l.remover_fim()
# print('Esperado D C B')
# l.show()

# print('Esperado B C D')
# l.show_reverso()

print('-----------')
l.remover('D')
l.show()
print('Esperado C B A')

l.remover('C')
l.show()
print('Esperado B A')

l.remover('B')
l.show()
print('Esperado A')

l.remover('A')
l.show()
print('Esperado ')