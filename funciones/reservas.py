from datetime import datetime, timedelta


tiempo_actual = datetime.now()

reservas_activas = []

juegos_reservados = set()


# FUNCIONES AUXILIARES
# ===============================


def obtener_horas_dispo(fecha):
    horas_disponibles = []

    for h in range(9, 23):  # 9:00 a 22:00
        inicio = fecha.replace(hour=h, minute=0)
        fin = inicio + timedelta(hours=1)


        ocupada = False
        for reserva in reservas_activas:
            if inicio < reserva['fin'] and fin > reserva['inicio']:
                ocupada = True
                break

        if not ocupada:
            horas_disponibles.append(h)

    return horas_disponibles


def pedir_numero(mensaje, minimo=1, maximo=None):
    while True:
        valor = input(mensaje).strip()

        if valor.lower() in ['atras']:
            return 'atras'

        if valor.startswith('0') and len(valor) > 1:
            print('No se permiten ceros al inicio')
            continue

        try:
            num = int(valor)


            if num < minimo:
                print(f'Mínimo {minimo}')
                continue


            if maximo is not None and num > maximo:
                print(f'Máximo {maximo}')
                continue

            return num

        except ValueError:
            print('Ingresa un número válido')



def pedir_duracion(hora_inicio, horas_disponibles):
    while True:
        horas = pedir_numero('Cuántas horas? (1–5): ', 1, 5)
        if horas == 'atras':
            return None


        if hora_inicio + horas > 23:
            print('El horario excede las 23:00')
            continue


        horas_necesarias = range(hora_inicio, hora_inicio + horas)
        if not all(h in horas_disponibles for h in horas_necesarias):
            print('Esa duración invade un horario no disponible')
            continue


        return horas



def selecc_juegos(juegos_consola):
    while True:
        print('\nElije hasta 5 juegos:')
        disponibles = [
            juego for i, juego in enumerate(juegos_consola)
            if i not in juegos_reservados
        ]


        if not disponibles:
            print('No quedan juegos disponibles')
            return []


        for i, juego in enumerate(disponibles, 1):
            print(f'{i}. {juego}')


        selecc_j = input('Escribe los números separados por coma o atras para volver: ').strip()
        if selecc_j.lower() == 'atras':
            return None


        partes = [x.strip() for x in selecc_j.split(',')]
        if any(not x.isdigit() for x in partes):
            print('Entrada inválida')
            continue


        idxs = [int(x) - 1 for x in partes]
        if any(i < 0 or i >= len(disponibles) for i in idxs):
            print('Número fuera de rango')
            continue


        if len(set(idxs)) != len(idxs):
            print('No repitas juegos')
            continue


        if len(idxs) > 5:
            print('Máximo 5 juegos')
            continue


        seleccionados = []
        for i in idxs:
            idx_global = juegos_consola.index(disponibles[i])
            seleccionados.append(idx_global)


        juegos_reservados.update(seleccionados)
        return [juegos_consola[i] for i in seleccionados]


# DATOS
# ===============================

salas = [
    {'nombre': 'Sala 1: Consolas', 'descripcion': 'Esta sala cuenta con dos PlayStation 5 y está condicionada para que tengas una excelente partida.', 'max_personas': 8, 'max_sillas': 8, 'max_sofas': 2, 'max_mandos': 4},
    {'nombre': 'Sala 2: Consolas', 'descripcion': 'Esta sala cuenta con dos PlayStation 5 y está condicionada para que tengas una excelente partida.', 'max_personas': 8, 'max_sillas': 8, 'max_sofas': 2, 'max_mandos': 4},
    {'nombre': 'Sala 3: PCs', 'descripcion': 'Esta sala cuenta con tres computadoras listas para su disfrute. Tienen servicio a internet ilimitado y una gran variedad de videojuegos',  'max_personas': 6, 'max_sillas': 6, 'max_audifonos': 6},
    {'nombre': 'Sala 4: Realidad Virtual', 'descripcion': 'Esta sala cuenta con cuatro equipos de realidad virtual de gran inmersión para que la pases en grande.\nEstos son:\n- Dos RV Cooperativo de exploración y combate\n- RV de carreras\n- RV simulador de atracciones', 'max_personas': 6, 'max_mandos_rv': 6, 'max_visores_rv': 5, 'max_caminadora_rv': 3}
]


juegos_consola = [
    'Hollow Knight', 'Stardew Valley', 'Clair Obscur: Expedition 33', 'Call of Duty',
    'Undertale', 'It Takes Two', 'Mortal Kombat 11', 'Overcooked', 'The Quarry', 'The Last of Us'
]


# FUNCIÓN PRINCIPAL
# ===============================


def reservar():
    while True:
        print('\nSalas disponibles:')
        for i, sala in enumerate(salas, 1):
            estado = '(Reservada)' if not sala['disponible'] else ''
            print(f'{i}. {sala['nombre']} {estado}')
        print('Atras')


        selecc = input('Selecciona una sala: ').lower()
        if selecc == 'atras':
            return


        try:
            sala = salas[int(selecc) - 1]
        except:
            print('Opción inválida')
            continue


        if not sala['disponible']:
            print('Sala no disponible')
            continue


        #Personas
        personas = pedir_numero('Cuántas personas?: ', 1, sala['max_personas'])
        if personas == 'atras':
            continue

        # Mandos / audifonos / visores
        if 'Consolas' in sala['nombre']:
            mandos = pedir_numero(f'Cuantos mandos usaran? Maximo {sala['max_mandos']}: ', minimo=1, maximo=sala['max_mandos'])
            if mandos == 'atras':
                continue
            
        elif 'PCs' in sala['nombre']:
            audifonos = pedir_numero(f'Cuantos audífonos usaran? Maximo {sala['max_audifonos']}: ', minimo=1, maximo=sala['max_audifonos'])
            if audifonos == 'atras':
                continue
            
        elif 'Realidad Virtual' in sala['nombre']:
            mandos_rv = pedir_numero(f'Cuantos mandos RV usaran? Maximo {sala['max_mandos_rv']}: ', minimo=1, maximo=sala['max_mandos_rv'])
            if mandos_rv == 'atras':
                continue
            visores_rv = pedir_numero(f'Cuantos visores RV usaran? Maximo {sala['max_visores_rv']}: ', minimo=1, maximo=sala['max_visores_rv'])
            if visores_rv == 'atras':
                continue


        juegos = []
        if 'Consolas' in sala['nombre']:
            juegos = selecc_juegos(juegos_consola)
            if juegos is None:
                continue


        hoy = datetime.now()
        print('\nFechas disponibles:')
        for i in range(16):
            print(f'{i+1}. {(hoy + timedelta(days=i)).strftime('%Y-%m-%d')}')


        selecc_f = pedir_numero('Selecciona fecha: ', 1, 16)
        
        if selecc_f == 'atras':
            continue

        fecha = hoy + timedelta(days=selecc_f-1)
        horas_disp = obtener_horas_dispo(fecha)

        if not horas_disp:
            print('No hay horarios disponibles')
            continue


        print('\nHorarios disponibles:')
        for i, h in enumerate(horas_disp, 1):
            print(f'{i}. {h:02d}:00')


        selecc_h = pedir_numero('Hora de inicio: ', 1, len(horas_disp))
        if selecc_h == 'atras':
            continue

        hora_inicio = horas_disp[selecc_h - 1]
        inicio = fecha.replace(hour=hora_inicio, minute=0)

        horas = pedir_duracion(hora_inicio, horas_disp)
        if horas is None:
            continue

        fin = inicio + timedelta(hours=horas)
        costo = horas * 1000


        print(f'\nCosto total: {costo}$')
        
        while True:
            confirmar = input('\nConfirmar reserva? si/no: ').strip().lower()
            
            if confirmar in ['si']:
                print('\nReserva realizada con exito!')
                
                #Guardar la reserva
                reserva = {
                    'sala': sala,
                    'inicio': inicio,
                    'fin': fin,
                    'horas': horas,
                    'juegos': juegos,
                    'personas': personas,
                }
                reservas_activas.append(reserva)
                
                sala['disponible'] = False
                return
            
            elif confirmar in ['no']:
                print('Reserva cancelada. Volviendo al menu principal...')
                return
            
            else:
                print('\nRespuesta invalida. Escribe si o no')
                
                
#FUNCION DE SIMULACION
#=================================
                
def avanzar_tiempo (horas=1):
    global tiempo_actual
    tiempo_actual += timedelta(hours=horas)
    print(f'\nTiempo avanzado {horas} horas. Hora actual simulada: {tiempo_actual.strftime('%Y-%m-%d %H:%M')}')
    
    #Chequear reservas terminadas
    terminadas = []
    for reserva in reservas_activas[:]:
        if tiempo_actual >= reserva['hora_fin']:
            reserva['sala']['disponible'] = True
            
            #Liberar juegos de consolas
            if 'Consolas' in reserva['sala']['nombre']:
                for juego in reserva['juegos']:
                    idx = juegos_consola.index(juego)
                    if idx in juegos_reservados:
                        juegos_reservados.remove(idx)
            terminadas.append(reserva)
            
    #Quitar las terminadas de la lista activa
    for t in terminadas:
        reservas_activas.remove(t)
        
    if terminadas:
        print(f'Se liberaron {len(terminadas)} reservas automaticamente')
    else:
        print('No hay reservas que hayan terminado aun')
        
def reset_tiempo():
    global tiempo_actual, reservas_activas, juegos_reservados
    tiempo_actual = datetime.now()
    reservas_activas = []
    juegos_reservados.clear()
    for sala in salas:
        sala['disponible'] = True
    print('Tiempo y reservas reseteados')
