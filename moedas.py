def format(msg):
    # Função que centralizar a msg e adiciona linhas tanto embaixo quanto emcima.
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)


def moeda1(* moedas):
    # Função que recebe uma lista de moedas e depois as orderna da 1 a última, e depois verifica se o input digitado está realmente correto. Se estiver o valor é retornado.
    for i, m in enumerate(moedas):
        print(f'{i + 1} - {m}')
    res1 = 0
    while res1 <= 0 or res1 > len(moedas):
        print('-' * 50)
        res1 = leiaInt('Digite a opção que deseja converter: ')
        if res1 <= 0 or res1 > len(moedas):
            print('ERRO! Valor selecionado inválido.')
    for i, m in enumerate(moedas):
        if res1 - 1 == i:
            print(f'Moeda {m} escolhida com sucesso!')
            print('-' * 50)
            return m


def moeda2(res1, * moedas):
    # Funcão igual a anterior mas com o porém que caso o usúario digite a mesma moeda, será exibido uma mensagem de erro.
    res2 = 0
    for i, m in enumerate(moedas):
        print(f'{i + 1} - {m}')
    while True:
        print('-' * 50)
        res2 = leiaInt('Digite a opcão para qual deseja converter: ')
        if res2 <= 0 or res2 > len(moedas):
            print('ERRO! Valor selecionado inválido.')
        for i, m in enumerate(moedas):
            if res2 - 1 == i:
                if m == res1:
                    print('ERRO! Tipos de moedas iguais.')
                else:
                    print(f'Moeda {m} escolhida com sucesso!')
                    return m


def leiaFloat(msg):
    # Função que irá ler um número de ponto flutuante, caso o número digitado não seja um número, tenha mais de 2 casa decimais ou não tenha nenhuma casa inteira exibirá um erro ao usuário.
    while True:
        num = str(input(msg).strip())
        num = num.replace(',', '.')
        try:
            casas_inteiras = len(num.split('.')[0])
            casas_decimais = len(num.split('.')[1])
        except:
            try:
                num = float(num)
            except:
                print('ERRO! Valor digitado inválido')
                print('-' * 50)
            else:
                return num
        else:
            try:
                num = float(num)
            except:
                print('ERRO! Valor digitado inválido')
                print('-' * 50)
            else:
                if casas_decimais <= 1 or casas_decimais > 2 or casas_inteiras == 0:
                    print('ERRO! Valor digitado inválido')
                    print('-' * 50)
                elif casas_decimais == 2:
                    return num


def leiaInt(msg):
    # Função irá tentar ler um número inteiro e caso resulte em um erro retornará 0, que normalmente significa erro no programa.
    try:
        num = int(input(msg))
    except:
        return 0
    else:
        return num


def cifrao(moeda):
    # A função irá pegar o parâmetro moeda e verificar qual foi a escolhida, retornado o seu cifrão.
    if moeda in 'REAL(BRL)':
        c = 'R$'
    elif moeda in 'DÓLAR(USD)':
        c = '$'
    elif moeda in 'EURO(EUR)':
        c = '€'
    elif moeda in 'IENE(JPY)':
        c = '¥'
    return c


def calculo(valor, escolha1, escolha2):
    # Função principal, primeiro ela irá pegar as moedas selecionadas, depois irá acessar uma api das cotações das moedas, logo em seguida irá pegar a cotação da moeda escolhida. Depois desse processo ele irá fazer o cálculo do valor e retorná-lo ao usúario.
    import requests
    escolha1 = escolha1[-4:-1]
    escolha2 = escolha2[-4:-1]
    requisicao = requests.get(
        f'https://economia.awesomeapi.com.br/last/{escolha1}-{escolha2}')
    info = requisicao.json()
    chave = f'{escolha1}{escolha2}'
    cotacao = float(info[chave]['bid'])
    resultado = valor * cotacao
    return resultado
