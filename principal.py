import moedas
while True:
    cont = ''
    # Criação do menu.
    moedas.format('Conversor de Moedas')
    m1 = moedas.moeda1('REAL(BRL)', 'DÓLAR(USD)', 'EURO(EUR)', 'IENE(JPY)')
    m2 = moedas.moeda2(m1, 'REAL(BRL)', 'DÓLAR(USD)', 'EURO(EUR)', 'IENE(JPY)')
    # Exibição das moedas escolhidas.
    moedas.format(f'CONVERSÃO DE {m1} para {m2}')
    # Recebe o cifrão da primeira moeda.
    cifra = moedas.cifrao(m1)
    n = moedas.leiaFloat(f'Digite um valor para conversão: {cifra}')
    # Recebe o resultado da cotação.
    res = moedas.calculo(n, m1, m2)
    # Resultado final
    print(f'{cifra}{n:.2F} convertendo pra {m2} equivale a {moedas.cifrao(m2)}{res:.2f}')
    # Pergunta se o usuário que continuar ou não. Se sim o programa continua, se não, o programa termina.
    while cont not in ('S', 'N'):
        print('-' * 50)
        cont = str(input('Quer continuar [S/N]? ').strip().upper())
        if cont not in ('S', 'N'):
            print('ERRO! Opção inválida')
    if cont in ('N'):
        break
    elif cont in 'S':
        print('OK! VAMOS CONTINUAR')
moedas.format('OBRIGADO POR USAR O CONVERSOR DE MOEDAS!')
