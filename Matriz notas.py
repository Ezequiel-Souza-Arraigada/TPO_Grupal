def dni_valido(dni):
    return dni.isdigit() and 10000000 <= int(dni) <= 70000000

def nota_valida(nota):
    nota_int= int(nota)
    if nota_int >= 0 and nota_int <= 10:
        return nota
    else:
        return False

def matriz(num_estudiantes):
    matriz_datos = []

    for f in range(num_estudiantes):
        
        nombre = input(f"Estudiante {f + 1} - Nombre: ").title()

        # Validación del DNI
        while True:
            dni = input(f"Estudiante {f + 1} - DNI: ")
            if dni_valido(dni):
                break
            else:
                print("Error: DNI inválido. Debe estar entre 10,000,000 y 70,000,000.")
        
        # Validación de la Nota1
        while True:
            nota1 = input(f"Estudiante {f + 1} - Nota 1 (entre 0 y 10): ")
            if nota_valida(nota1):
                nota1 = int(nota1)
                break
            else:
                print("Error: Nota inválida. Debe estar entre 0 y 10.")
        
        # Validación de la Nota2
        while True:
            nota2 = input(f"Estudiante {f + 1} - Nota 2 (entre 0 y 10): ")
            if nota_valida(nota2):
                nota2 = int(nota2)
                break
            else:
                print("Error: Nota inválida. Debe estar entre 0 y 10.")
        
        # Cálculo nota final 
        nota_final = (nota1 + nota2) // 2

        # Agregar los datos validados a la matriz
        matriz_datos.append([nombre, dni, nota1, nota2, nota_final])

    return matriz_datos


def imprimir_matriz_estudiantes(matriz_datos):

    print("-- Lista de estudiantes --")
    print("---------------------------------------------------------------------------------------")
    
    

    # Bucle para imprimir cada fila de la matriz
    for fila in matriz_datos:
        nombre = fila[0]  
        dni = fila[1]     
        nota1 = fila[2]   
        nota2 = fila[3]   
        nota_final = fila[4] 
        
        
        print(f"Nombre: {'%-15s' % nombre} | DNI: {'%-10s' % dni} | Nota 1: {nota1} | Nota 2: {nota2} | Nota Final: {nota_final}")
    
   
    print("---------------------------------------------------------------------------------------")


# Main
num_estudiantes = int(input("¿Cuántos estudiantes quieres ingresar?: "))
matriz_prueba = matriz(num_estudiantes)

# Imprimir
imprimir_matriz_estudiantes(matriz_prueba)