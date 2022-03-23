from Random import RandomValue


def generateKeys():
    keys = open('chaves_plicas.txt', 'w')

    option = int(input('1 - Gerar Chaves Manualmente\n2 - Gerar Chaves Automaticamente\n'))
    if option == 1:
        p = int(input('digite a chave p: '))
        q = int(input('digite a chave q: '))
        e = int(input('digite a chave e: '))

    elif option == 2:
        random = RandomValue()
        p = random.randomPrime()
        q = random.randomPrime()
        e = random.randomExp(p, q)

    else:
        print('entrada inválida')
        return

    print('p:: ', p)
    print('q:: ', q)
    print('Não revele essa chave a ninguém')
    keys.write(f'{p * q}\n{e}')
    keys.close()
