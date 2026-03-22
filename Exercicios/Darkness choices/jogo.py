print('-------------------------------------------------------------> Darkness choices 💀 ------------------------------------------------------------------------>')
print('Você acorda em uma cama de ferro antiga está coberta por um lençol amarelado. Ele parece ter sido mexido recentemente, mas ninguém deveria estar ali. ')
print('Ao levantar se depara com duas portas velhas e acabadas, respectivamente 1 e 2.')
print('Qual voce esccolhe?')
porta = input('> ')

if porta == "1":
    print('Voce abre a porta e se depara com duas taças:')
    print('1. Líquido de textura densa, com cor vermelho sangue 🔴')
    print('2. Líquido de textura leve, com cor esbranquiçada ⚪')
    print('Qual voce escolhe?')

    taca = input("> ")

    if taca == "1":
        print('Voce se sente fraco e aos poucos desmaia, acorda novamente na cama que iniciou..')
        print('Não foi dessa vez!')
        proposta = input("Tente novamente!")
        
    elif taca == "2":
        print('você toma não sente nada diferente no momento a parede a frente se abre e se depara com dois espelhos e uma pedra no chão:   ')
        print('1. O espelho reflete um vulto preto atrás de voce, com a mão em seu ombro')
        print('2. O outro reflete voce, morto. ')
        print('Voce pega a pedra do chão, qual espelho decide quebrar?')
        decisaotaca2 = input('')

        if decisaotaca2 == "1":
            print(' ')
            print(' ')
            print(' ')
        elif decisaotaca2 == "2":
            print(' ')
            print(' ')
        else:
            print('Escolha um número válido')
    else:
        print('Digite uma opção válida...')
        print('Tente novamente...')
elif porta == "2":
    print('Voce abre a poorta e se depara com dois espelhos pendurados na parede, não há janelas apenas uma pedra no chão, sem mais nada a sua volta:')
    print('1. O espelho refete a sua imagem, porém ao seu lado pelana um vulto preto ao seu lado, que apoia uma mão em seu ombro')
    print('2. O segundo espelho refelere sua imagem, porém nela voce está... morto.')
    print('Voce pega a pedra em uma de suas mãos e quebra um dos espelhos, qual deles voce escolhe?')
    espelho = input('> ')

    if espelho == '1':
        print('Ao quebrar o espelho se depara com uma passagem atrás dela, ao travessa-la, encontra uma criatura magra sentada no canto da sala, a mesma parte para cima de voce e sem chances de reagir, ela te come vivo!')
        print('Não foi dessa vez')
        print('Tente novamente!')
    elif espelho == '2':
        print('Imediatamente após quebrar, sente um aperto no peito, e su visão escureçe...')
        print('Voce está morto 💀')
        print('Tente novamente!!')
else:
    print('Tente um número válido!')