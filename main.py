from funciones.persistencia import guardar_estado, cargar_estado
from funciones.menu import menu_principal

def main():
    try:
        cargar_estado()
    except FileNotFoundError:
        pass
    
    menu_principal()
    
    guardar_estado()
    
if __name__ == '__main__':
    main()