def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point < 1 or point > 5:  # Verificar si está fuera del rango de 1 a 5
                print('Por favor, introduzca un valor entre el 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'Puntuación: {point} Comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                print("Puntuación y comentario guardados.")
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def comprobar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido:
                print(contenido)
            else:
                print("No hay resultados para mostrar.")
    except FileNotFoundError:
        print("No hay resultados para mostrar. El archivo no existe.")

def iniciar_programa():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprobar los resultados obtenidos hasta ahora')
        print('3: Finalizar')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Por favor, introduzca del 1 al 3')
        else:
            print('Por favor, introduzca del 1 al 3')

# Iniciar el programa
iniciar_programa()
