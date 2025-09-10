import Ldse
l = Ldse.Ldse()
l.inserir_inicio('A')
l.show()
print('Esperado A')

l.inserir_inicio('B')
l.show()
print('Esperado B A')

l.inserir_inicio('C')
l.show()
print('Esperado C B A')

l.inserir_inicio('D')
l.show()
print('Esperado D C B A')

l.remover_inicio()
l.show()
print('Esperado C B A')

l.remover_inicio()
l.show()
print('Esperado B A')

l.inserir_fim('B')
l.show()
print('Esperado B A B')

print('Primeiro')
print(l.ver_primeiro())

print('Ultimo')
print(l.ver_ultimo())

print('Quantidade')
print(l.ver_quantidade())

print('Esta vazia')
print(l.esta_vazia())

l.remover_fim3()
l.show()
print('Esperado B A')

l.remover('A')
l.show()
print('Esperado B')

l.inserir_inicio('X')
l.show()
print('Esperado X B')

l.remover('B')
l.show()
print('Esperado X')

