import random 

# El juego
juego = []
while True:
    print('Bienvenidos a mi casino  !!!!!!!!!')
    jugador = random.randint(2, 26)
    dealer = random.randint(2, 26)

    # La partida
    while True:
        print('El jugador saco: ', jugador, 'El dealer tiene esto: ', dealer)
        quiere_mas_cartas = input('Quiere mas cartas? S/N ')
        if quiere_mas_cartas == 'S':
            jugador = jugador * random.randint(1, 13)
        else:
            if jugador == dealer:
                print('Gano el dealer')
                juego.append('dealer')
                break
            elif jugador == 21 or (jugador > dealer and jugador < 21):
                print('Gano el jugador')