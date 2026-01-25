import suscripcion
from reservas import reservar, avanzar_tiempo, tiempo_actual, reservas_activas, juegos_reservados, reset_tiempo
import mis_reservas
import tienda_arcane
import ofertas


MODO_DEBUG = True

def mostrar_hora_actual():
    print(f'\nFecha y hora: {tiempo_actual.strftime('%d-%m-%Y | %H:%M')}')
    
def mostrar_encabezado():
    print('\n' + '=' * 40)
    print('         Arcane Gaming Lounge')
    print('=' * 40)
    print('Horario: 09:00 AM - 11:00 PM')
    print('Contacto: arcane@gaming.com | Tel: +53 53529701')
    print('-' * 40)
 
def menu_principal():
    
    while True:
        mostrar_encabezado()
        mostrar_hora_actual()
        print('-' * 40)
        
        print('\n1. Reservar')
        print('2. Mis Reservas')
        print('3. Comprar Juegos')
        print('4. Suscripción')
        print('5. Ofertas')
        print('6. Salir')
        
        if MODO_DEBUG:
            print('7. Avanzar Tiempo (Modo Prueba)')

        selecc = input('\nElige una opción: ')
        if selecc == '1':
            if suscripcion.suscrito:
                reservar()
            else:
                print('\nPara poder reservar necesitas estar suscrito')
    
                if suscripcion.suscrip():
                    print('\nYa puedes reservar')
                    reservar()
                    
        elif selecc == '2':
            mis_reservas.reservas_usuario()
                    
        elif selecc == '3':
            if suscripcion.suscrito:
                tienda_arcane.menu_tienda()
            else:
                print('\nPara poder comprar necesitas estar suscrito')
    
                if suscripcion.suscrip():
                    print('\nYa puedes comprar')
                    tienda_arcane.menu_tienda()
        
        elif selecc == '4':
            if suscripcion.suscrito:
                suscripcion.menu_suscrip()
                
            else:
                suscripcion.suscrip()
                    
        elif selecc == '5':
            ofertas.mostrar_ofertas()
            
        elif selecc == '6':
           print('Hasta pronto')
           break
        
        elif selecc == '7' and MODO_DEBUG:
            while True:
                print('\nMODO PRUEBA / SIMULACIÓN')
                print('1. Avanzar tiempo')
                print('2. Resetear tiempo y reservas')
                print('3. Atrás')

                opcion_test = input('Elige una opción: ').strip()

                if opcion_test == '1':
                    try:
                        horas = int(input('Cuántas horas deseas avanzar?: '))
                        if horas <= 0:
                            print('Debes ingresar un número positivo')
                        else:
                            avanzar_tiempo(horas)
                    except ValueError:
                        print('Ingresa un número válido')

                elif opcion_test == '2':
                    confirmar = input(
                        '\nEsto eliminará reservas y reiniciará el tiempo\n'
                        'Estás seguro? si/no: '
                    ).lower().strip()

                    if confirmar == 'si':
                        reset_tiempo()

                elif opcion_test == '3':
                    break

                else:
                    print('Opción inválida')
                      
        else:
            print('Opción inválida. Elige 1-7')
    
menu_principal()