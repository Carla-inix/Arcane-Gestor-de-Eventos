import suscripcion
from datetime import datetime


juegos_disponibles = {
    1: {'nombre': 'FIFA 24', 'precio': 350, 'stock': 2},
    2: {'nombre': 'Assassins Creed: Black Flag', 'precio': 500, 'stock': 4},
    3: {'nombre': 'Spider-Man 2', 'precio': 500, 'stock': 4},
    4: {'nombre': 'Mario Kart 8', 'precio': 400, 'stock': 3},
    5: {'nombre': 'Bramble', 'precio': 500, 'stock': 2},
    6: {'nombre': 'Resident Evil 4 Remake', 'precio': 600, 'stock': 1}
}

# Compras realizadas por el usuario
compras_usuarios = {}


def menu_tienda():
    if suscripcion.user_actual is None:
        print('Debes estar suscrito para comprar')
        input('\nPresiona Enter para volver...')
        return

    while True:
        print('\nTienda de Juegos\n')
        print('1. Comprar juegos')
        print('2. Ver mis compras')
        print('3. Atras')

        selecc = input('Elige una opción: ').strip()

        if selecc == '1':
            comprar_juegos()
            
        elif selecc == '2':
            mostrar_mis_compras()
            
        elif selecc == '3':
            return
        
        else:
            print('Opción inválida')


def comprar_juegos():
    while True:
        print('\n   Juegos Disponibles\n')

        for num, juego in juegos_disponibles.items():
            if juego['stock'] > 0:
                print(f'{num}. {juego['nombre']} - {juego['precio']}$ | Stock: {juego['stock']}')
            else:
                print(f'{num}. {juego['nombre']} - AGOTADO⭕')

        print('\n0. Atrás')
        selecc = input('Selecciona un juego: ').strip()

        if selecc == '0':
            return

        if not selecc.isdigit():
            print('Opcion invalida')
            continue

        selecc = int(selecc)

        if selecc not in juegos_disponibles:
            print('Juego inválido')
            continue

        juego = juegos_disponibles[selecc]

        if juego['stock'] == 0:
            print('Este juego está agotado')
            continue

        cantidad = input('Cantidad a comprar: ').strip()

        if not cantidad.isdigit():
            print('Cantidad inválida')
            continue

        cantidad = int(cantidad)

        if cantidad <= 0:
            print('Cantidad inválida')
            continue

        if cantidad > juego['stock']:
            print('No hay suficiente stock')
            continue

        total = cantidad * juego['precio']
        
        if copias_compradas(user, juego['nombre']) + cantidad > 3:
            print('No puedes comprar más de 3 copias del mismo juego')
            continue

        confirmar = input(
            f'Total: {total}$\nConfirmar compra? si/no: '
        ).lower().strip()

        if confirmar == 'si':

            # Descontar stock
            juego['stock'] -= cantidad

            # Registrar compra
            user = suscripcion.user_actual
            compras_usuarios.setdefault(user, []).append({
                'fecha': datetime.now()strftime('%d-%m-%Y | %H:%M'),
                'juego': juego['nombre'],
                'cantidad': cantidad,
                'total': total
            })

            print('Compra realizada con éxito!')
            return
        
        elif confirmar == 'no':
            print('Compra cancelada')
            return
        
        else:
            print('Respuesta inválida')


def mostrar_mis_compras():
    user = suscripcion.user_actual

    print('\n   Mis Compras\n')

    if user not in compras_usuarios or not compras_usuarios[user]:
        print('No has realizado compras')
        input('\nPresiona Enter para volver...')
        return

    for compra in compras_usuarios[user]:
        print(f'{compra['fecha']}\n{compra['juego']} x{compra['cantidad']} \n{compra['total']}$')
        print('-' * 30)

    input('\nPresiona Enter para volver...')
    
    
def copias_compradas(user, nombre_juego):
    total = 0
    for compra in compras_usuarios.get(user, []):
        if compra['juego'] == nombre_juego:
            total += compra['cantidad']
    return total