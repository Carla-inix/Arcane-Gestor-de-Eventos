from reservas import reservas_activas

usuarios = {}
suscrito = False
user_actual = None
cupon_disponible = False
cupon_usado = False

def suscrip ():
    global suscrito, user_actual
    
    while True:
        print('\nVamos a registrarte..')
        nombre = input('Nombre: ').strip()
        if not nombre:
            print('Tu nombre no puede estar vacio')
            continue
        
        while True:
            carnet_str = input('Ingrese su carnet de identidad: ')
            try:
                id_user = int(carnet_str)
                break
            except ValueError:
                print('Deben ser números enteros .Prueba otra vez')
            
        if id_user in usuarios:
            print('Ese ID ya existe, ingrese otro')
            continue
        
            #Guarda los datos en el diccionario
        usuarios[id_user] = nombre
        suscrito = True
        user_actual = id_user
        print('\nYa estás suscrito!!')
        
        return True
        
#Cancelar Suscripcion
def canc_suscrip():
    from reservas import reservas_activas, cancelar_reserva
    global suscrito, user_actual
    
    while True:
        try:
            print('Al cancelar tu suscripción se eliminarán las reservas que tengas')
            id_cancel = int(input('Ingresa tu carnet para cancelar: '))
            
            # Cancelar reservas activas del usuario y liberar juegos
            for r in reservas_activas[:]:
                if r['usuario'] == id_cancel:
                    cancelar_reserva(r)
            
            if id_cancel in usuarios:
                nombre = usuarios.pop(id_cancel)
                suscrito = False
                user_actual = None
                print('Suscripción Cancelada')
                return True
            else:
                print('ID no encontrado')
        except ValueError:
            print('Ingresa un número válido')
            

def menu_suscrip():
    if suscrito:
        
        while True:
            nombre = usuarios.get(user_actual, 'Desconocido')
            
            print('\n\tSuscrito\n')
            print(f'Usuario: {nombre}')
            print(f'ID: {user_actual}')
            print('-\n'*30)
            
            print('1. Cancelar Suscripción')
            print('2. Atrás')
            selecc = input('Elige una opción: ').strip()
            
            if selecc == '1':
                if canc_suscrip():
                    return
                else:
                    print('\nNo se pudo cancelar')
                    
            elif selecc == '2':
                return
            
            else:
                print('Opción inválida. Elige 1 o 2')