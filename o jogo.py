import random
fichas=100
come_out=True
continuar=True
while continuar and come_out and fichas>0:
    print('Você está na fase “Come Out”')
    print('Você tem {} fichas'.format (fichas))
    dados= random.randint(1,6) + random.randint(1,6)
    print('Opções de aposta: Pass Line Bet, Field, Any Craps, Twelve')
    aposta=input('Escolha um tipo de aposta:')
    if aposta== 'Pass Line Bet':
        valor= int(input('Quanto você deseja apostar?'))
        if dados== 11 or dados== 7:
            fichas= fichas + valor
            come_out=True
            print('Você ganhou mais {} fichas'.format(valor))
            sair=input('Você deseja continuar? [S/N]')
            if sair == 'N':
                print('Você está fora!')
                print('Você saiu com {} fichas'.format(fichas))
                continuar=False
        elif dados== 2 or dados== 3 or dados== 12:
            fichas= fichas-valor
            come_out=True
            print('Você perdeu {} fichas'.format(valor))
            sair=input('Você deseja continuar? [S/N]')
            if sair == 'N':
                print('Você está fora!')
                print('Você saiu com {} fichas'.format(fichas))
                continuar=False
        else:
            print('Voce passou para a fase de Point')
            dados2= random.randint(1,6) + random.randint(1,6)
            if dados2 == dados:
                fichas= fichas + valor
                print('Você ganhou mais {} fichas e voltou para o "Come out"'.format(valor))
            elif dados2 == 7:
                print('Você perdeu!')
                come_out=False
            else:
                while dados2 != dados or dados2 != 7:
                    dados2= random.randint(1,6) + random.randint(1,6)
                    if dados2 == dados:
                        fichas= fichas + valor
                        print('Você ganhou mais {} fichas e voltou para o "Come out"'.format(valor))
                        come_out=True
                        break
                    elif dados2 == 7:
                        print('Você perdeu!')
                        come_out=False
                        continuar=False
                        break
  