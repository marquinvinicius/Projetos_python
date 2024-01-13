from time import sleep
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS 
[ 5 ] SAIR DO PROGRAMA''')
    op = int(input('>>>>> Qual sua opção? '))
    if op == 1:
        s = p1 + p2
        print(f'A soma entre {p1} + {p2} é {s}')
    elif op == 2:
        s = p1* p2
        print(f'O resultado entre {p1} X {p2} foi {s}')
    elif op == 3:
        if p1 > p2:
            maior = p1
        else:
            maior = p2
        print(f'Entre {p1} e {p2} o maior foi {maior}')
    elif op == 4:
        print('informe os números novamente: ')
        p1 = int(input('Primeiro valor: '))
        p2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finlaizando...')
        break
    else:
        print('Opção inválida. Tente novamente.')
    print('=-='*10)
    sleep(1)
print('Fim do programa! Volte sempre!')
