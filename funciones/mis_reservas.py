from reservas import reservas_activas
import suscripcion
from datetime import datetime


def reservas_usuario():
    print('\nMis Reservas\n')
    
    if suscripcion.user_actual is None:
        print('No hay ningun usuario activo')
        print('\nPresiona Enter para volver..')
        return

    tiene_reservas = False

    for reserva in reservas_activas:
        if reserva['usuario'] == suscripcion.user_actual:
            tiene_reservas = True

            inicio = reserva['inicio'].strftime('%Y-%m-%d %H:%M')
            fin = reserva['fin'].strftime('%H:%M')

            print(f'Sala: {reserva['sala']['nombre']}')
            print(f'Horario: {inicio} - {fin}')
            if reserva.get('descuento'):
                print('Descuento aplicado: 20%')
            print(f'Duración: {reserva['horas']} horas')
            print(f'Personas: {reserva['personas']}')
            print(f'Juegos: {', '.join(reserva['juegos'])}')
            print('-' * 35)

    if not tiene_reservas:
        print('No tienes reservas activas')

    input('\nPresiona Enter para volver al menú...')