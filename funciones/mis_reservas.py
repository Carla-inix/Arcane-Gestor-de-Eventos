from datetime import datetime
from reservas import reservas_activas, cancelar_reserva
import suscripcion


def reservas_usuario():
   
    while True:
        print('\n\tMis Reservas\n')

        if suscripcion.user_actual is None:
            print('No hay ningún usuario activo')
            input('\nPresiona Enter para volver...')
            return
        
        # Obtener reservas del usuario
        mis_reservas = [
            r for r in reservas_activas
            if r['usuario'] == suscripcion.user_actual
        ]

        if not mis_reservas:
            print('No tienes reservas activas')
            input('\nPresiona Enter para volver...')
            return

        # Mostrar reservas
        for i, reserva in enumerate(mis_reservas, 1):
            inicio = reserva['inicio'].strftime('%d-%m-%Y | %H:%M')
            fin = reserva['fin'].strftime('%H:%M')

            print(f'{i}. {reserva['sala']['nombre']}')
            print(f'   Horario: {inicio} - {fin}')
            print(f'   Duración: {reserva['horas']} horas')
            print(f'   Personas: {reserva['personas']}')
            
            if reserva.get('recursos'):
                equipos = ', '.join(
                    f'{r.replace('_', ' ')} {c}'
                    for r, c in reserva['recursos'].items()
                )
                print(f'   Equipos: {equipos}')

            if reserva['juegos']:
                print(f'   Juegos: {', '.join(reserva['juegos'])}')

            if reserva.get('descuento'):
                print('   Descuento aplicado: 20%')

            print('-' * 35)

        # Menú de opciones
        print('\nOpciones:')
        print('1. Cancelar una reserva')
        print('2. Cancelar todas las reservas')
        print('3. Atrás')

        selecc = input('\nElige una opción: ').strip()

        # Cancelar una reserva
        if selecc == '1':
            try:
                num = int(input('Número de reserva a cancelar: '))
                if num < 1 or num > len(mis_reservas):
                    print('\nOpción inválida')
                    continue

                cancelar_reserva(mis_reservas[num - 1])
                print('\nReserva cancelada con éxito\n')

            except ValueError:
                print('\nIngresa un número válido')

        # Cancelar todas
        elif selecc == '2':
            for r in reservas_activas[:]:
                if r['usuario'] == suscripcion.user_actual:
                   cancelar_reserva(r)
                   
            print('\nTodas las reservas han sido canceladas')
            input('\nPresiona Enter para volver...')
            return

        # Volver
        elif selecc == '3':
            return

        else:
            print('\nOpción inválida')