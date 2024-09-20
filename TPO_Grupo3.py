diccionario_de_estudiantes = {}

def agregar_nuevoestudiante():
    DNI = input("Ingrese su número de DNI: ")
    if DNI in diccionario_de_estudiantes:
        return "DNI duplicado, ingrese uno nuevo"
    else:
        nombre = input("Ingrese su nombre: ").strip()
        apellido = input("Ingrese su apellido: ").strip()
        if not DNI.isdigit() or not nombre or not apellido:
            return "Datos inválidos, por favor revisar e ingresar nuevamente"
        else:
            diccionario_de_estudiantes[DNI] = (nombre, apellido)
            return "Estudiante agregado exitosamente"

def mostrar_estudiantes():
    if not diccionario_de_estudiantes:
        return "No hay estudiantes registrados"
    else:
        for DNI, (nombre, apellido) in diccionario_de_estudiantes.items():
            print(f"DNI: {DNI}, Nombre: {nombre}, Apellido: {apellido}")

def buscar_estudiante():
    DNI = input("Ingrese su número de DNI: ")
    if DNI in diccionario_de_estudiantes:
        nombre, apellido = diccionario_de_estudiantes[DNI]
        return f"Nombre: {nombre}, Apellido: {apellido}"
    else:
        return "Estudiante no encontrado"

# Gestión de materias
lista_materias = []

def agregar_materia():
    materia = input("Ingrese el nombre de la materia: ").strip()
    if materia in lista_materias:
        return "Materia ya registrada"
    elif not materia:
        return "Nombre de materia inválido"
    else:
        lista_materias.append(materia)
        return "Materia agregada exitosamente"

def mostrar_materias():
    if not lista_materias:
        return "No hay materias registradas"
    else:
        for materia in lista_materias:
            print(materia)

# Relación entre estudiantes y materias
diccionario_estudiantes_materias = {}

def asignar_materia_a_estudiante():
    DNI = input("Ingrese el DNI del estudiante: ")
    
    if DNI in diccionario_de_estudiantes:
        if not lista_materias:
            return "No hay materias registradas"
    
        print("Materias disponibles:")
        for materia in lista_materias:
            print(materia)

        materia_asignada = input("Ingrese el nombre de la materia a asignar: ").strip()
        
        if materia_asignada in lista_materias:
            if DNI in diccionario_estudiantes_materias:
                if materia_asignada not in diccionario_estudiantes_materias[DNI]:
                    diccionario_estudiantes_materias[DNI].append(materia_asignada)
                    return f"Materia '{materia_asignada}' asignada al estudiante con DNI {DNI}"
                else:
                    return "El estudiante ya tiene esta materia asignada"
            else:
                diccionario_estudiantes_materias[DNI] = [materia_asignada]
                return f"Materia '{materia_asignada}' asignada al estudiante con DNI {DNI}"
        else:
            return "Materia no registrada"
    else:
        return "Estudiante no encontrado"

def mostrar_materias_estudiante():
    DNI = input("Ingrese el DNI del estudiante: ")
    
    if DNI in diccionario_estudiantes_materias:
        materias = diccionario_estudiantes_materias[DNI]
        if materias:
            print(f"Materias asignadas al estudiante con DNI {DNI}:")
            for materia in materias:
                # print(materia)
                return materia
        else:
            return "El estudiante no tiene materias asignadas"
    else:
        return "Estudiante no tiene materias asignadas o no está registrado"

# Programa principal
while True:
    print("\nMenú:")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Agregar materia")
    print("5. Mostrar materias")
    print("6. Asignar materia a estudiante")
    print("7. Mostrar materias de un estudiante")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print(agregar_nuevoestudiante())
    elif opcion == '2':
        mostrar_estudiantes()
    elif opcion == '3':
        print(buscar_estudiante())
    elif opcion == '4':
        print(agregar_materia())
    elif opcion == '5':
        mostrar_materias()
    elif opcion == '6':
        print(asignar_materia_a_estudiante())
    elif opcion == '7':
        print(mostrar_materias_estudiante())
    elif opcion == '8':
        break
    else:
        print("Opción no válida")
