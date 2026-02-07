import suscripcion
from datetime import datetime

#DATOS
#=======================

juegos_disponibles = [
    {'nombre': 'FIFA 24', 'precio': 350, 'stock': 2, 'descripcion': 'ss'},
    {'nombre': 'Assassins Creed: Black Flag', 'precio': 500, 'stock': 4, 'descripcion': 'aa'},
    {'nombre': 'Spider-Man 2', 'precio': 500, 'stock': 4, 'descripcion': 'vv'},
    {'nombre': 'Mario Kart 8', 'precio': 400, 'stock': 3, 'descripcion': 'nn'},
    {'nombre': 'Bramble', 'precio': 500, 'stock': 2, 'descripcion': 'dd'},
    {'nombre': 'Resident Evil 4 Remake', 'precio': 600, 'stock': 1, 'descripcion': 'bb'},
]

compras_usuarios = {}

def pedir_numero(mensaje, minimo=None, maximo=None, atras=False):

    while True:
        selecc = input(mensaje).strip().lower()

        if atras and selecc == 'atras':
            return 'atras'

        if selecc == '':
            print('\nDebes ingresar un número')
            continue

        if not selecc.isdigit():
            print('\nIngresa un número válido\n')
            continue

        if selecc != str(int(selecc)):
            print('\nNo se permiten ceros al inicio\n')
            continue

        numero = int(selecc)

        if minimo is not None and numero < minimo:
            print(f'\nMínimo {minimo}')
            continue

        if maximo is not None and numero > maximo:
            print(f'\nMáximo {maximo}')
            continue

        return numero

#FUNCIONES
#========================

def comprar_juegos():
    while True:
        user = suscripcion.user_actual

        if compras_hoy(user, compras_usuarios) >= 2:
            print('\nSolo puedes hacer 2 compras por día\n')
            input('Presiona Enter para volver...')
            return
        
        
        print('\n' + '=' *40)
        print('            Juegos Disponibles')

        for i, juego in enumerate(juegos_disponibles, 1):
            print('=' * 40)
            print(f'{i}. {juego['nombre']}')
            
            if juego['stock'] > 0:
                print(f'Precio: {juego['precio']}$')
                print(f'Stock: {juego['stock']}')
                print(f'Descripción: {juego['descripcion']}')
            else:
                print('AGOTADO⭕')
        
        print('\n0. Atrás')
        selecc = input('Selecciona un juego: ').strip()

        if selecc == '0':
            return

        if not selecc.isdigit():
            print('\nIngresa un número válido')
            continue

        selecc = int(selecc)

        if selecc < 1 or selecc > len(juegos_disponibles):
            print('\nJuego inválido')
            continue

        juego = juegos_disponibles[selecc - 1]

        if juego['stock'] == 0:
            print('\nEste juego está agotado')
            continue

        cantidad = input('\nCantidad a comprar: ').strip()

        if not cantidad.isdigit():
            print('\nCantidad inválida')
            continue

        cantidad = int(cantidad)

        if cantidad <= 0:
            print('\nCantidad inválida')
            continue

        if cantidad > juego['stock']:
            print('\nNo hay suficiente stock')
            continue

        costo = cantidad * juego['precio']
        
        
        if copias_compradas(user, juego['nombre']) + cantidad > 3:
            print('\nNo puedes comprar más de 3 copias del mismo juego')
            continue

        confirmar = input(
            f'\nCosto: {costo}$\nConfirmar compra? si/no: '
        ).lower().strip()

        if confirmar == 'si':

            # Descontar stock
            juego['stock'] -= cantidad

            # Registrar compra
            compras_usuarios.setdefault(user, []).append({
                'fecha': datetime.now(),
                'juego': juego['nombre'],
                'precio': juego['precio'],
                'cantidad': cantidad,
                'costo': costo,
                
            })

            print('Compra realizada con éxito!')
            return
        
        elif confirmar == 'no':
            print('\nCompra cancelada')
            return
        
        else:
            print('\nRespuesta inválida\n')


def compras_hoy(usuario, compras_usuarios):
    hoy = datetime.now().date()
    return sum(
        1 for compra in compras_usuarios.get(usuario, [])
        if compra['fecha'].date() == hoy
    )


def mostrar_mis_compras():
    user = suscripcion.user_actual

    print('\n'+'='*30)
    print('          Mis Compras')
    print('='*30)
    
    if user not in compras_usuarios or not compras_usuarios[user]:
        print('No has realizado compras')
        input('\nPresiona Enter para volver...')
        return

    for compra in compras_usuarios[user]:
        print(f'Fecha: {compra['fecha'].strftime('%d-%m-%Y | %H:%M')}')
        print(f'Juego: {compra['juego']} {compra['precio']}$')
        print(f'Cantidad: {compra['cantidad']}')
        print(f'Costo: {compra['costo']}$')
        print('-' * 30)

    input('\nPresiona Enter para volver...')
    
    
def copias_compradas(user, nombre_juego):
    total = 0
    for compra in compras_usuarios.get(user, []):
        if compra['juego'] == nombre_juego:
            total += compra['cantidad']
    return total


#MENÚ
#========================

def menu_tienda():
    if suscripcion.user_actual is None:
        print('Debes estar suscrito para comprar')
        input('\nPresiona Enter para volver...')
        return

    while True:
        print('\n'+'='*40)
        print('             Tienda Arcane')
        print('='*40)
        print('\n1. Comprar juegos')
        print('2. Ver mis compras')
        print('3. Atrás')

        opcion = input('Elige una opción: ').strip()

        if opcion == '1':
            comprar_juegos()
        elif opcion == '2':
            mostrar_mis_compras()
        elif opcion == '3':
            return
        else:
            print('\nOpción inválida\n')