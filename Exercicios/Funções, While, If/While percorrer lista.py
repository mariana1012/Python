print('Guardando os números na lista e perquisando na mesma depois -->')

l =  []

x = 0

while x < 5:
    numeros = int(input('Digite um número e adicione a lista'))
    l.append(numeros)
    x += 1


verificar = int(input(' Digite o número que deseja verificar na lista: '))

if verificar in l:
    print('Esse número está na lista!')
else:
    print('Esse número nãp está em sua lista, tente novamente!')
