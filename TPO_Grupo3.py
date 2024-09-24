diccionario_de_estudiantes = {}

def agregar_nuevoestudiante():
    DNI = input("Ingrese su número de DNI (8 dígitos): ")

    while not (DNI.isdigit() and len(DNI) == 8):
        print("Datos inválidos. El DNI debe contener exactamente 8 dígitos.")
        DNI = input("Ingrese su número de DNI (8 dígitos): ")
    
    if DNI in diccionario_de_estudiantes:
        return "DNI duplicado, ingrese uno nuevo"
    else:
        nombre = input("Ingrese su nombre: ").strip()
        while not nombre.isalpha():
            print("Datos inválidos. Por favor revisar e ingresar nuevamente")
            nombre = input("Ingrese su nombre: ").strip()
        
        apellido = input("Ingrese su apellido: ").strip()
        while not apellido.isalpha():
            print("Datos inválidos. Por favor revisar e ingresar nuevamente")
            apellido = input("Ingrese su apellido: ").strip()
        
        validarNombre = input("¿Está seguro que desea cargar estos datos? (S/N): ")
        while validarNombre not in ("S", "s", "N", "n"):
            print("Comando desconocido")
            validarNombre = input("¿Está seguro que desea cargar estos datos? (S/N): ")
        
        if validarNombre in ("S", "s"):
            diccionario_de_estudiantes[DNI] = (nombre, apellido)
            return "Estudiante agregado exitosamente"
        if validarNombre in ("N", "n"):
            return agregar_nuevoestudiante()


def mostrar_estudiantes():
    if not diccionario_de_estudiantes:
        return "No hay estudiantes registrados"
    else:
        estudiantes = [f"DNI: {DNI}, Nombre: {nombre}, Apellido: {apellido}"
                       for DNI, (nombre, apellido) in diccionario_de_estudiantes.items()]
        return "\n".join(estudiantes)


def buscar_estudiante():
    while True:
        DNI = input("Ingrese su número de DNI o escriba 'salir' para volver al menú: ").strip()
        
        if DNI.lower() == 'salir':
            return "Saliendo de la búsqueda de estudiantes..."

        if not DNI.isdigit():
            print("El DNI debe ser un número. Por favor, intente nuevamente.")
            continue

        if DNI in diccionario_de_estudiantes:
            nombre, apellido = diccionario_de_estudiantes[DNI]
            return f"Nombre: {nombre}, Apellido: {apellido}"
        else:
            print("Estudiante no encontrado. Intente nuevamente.")



# Gestión de materias
lista_materias = []

def agregar_materia():
    while True:
        materia = input("Ingrese el nombre de la materia (o 'salir' para cancelar): ").strip()
        
        if materia.lower() == 'salir':
            return "Operación cancelada por el usuario."
        
        if not materia.isalpha():
            print("Nombre de materia inválido. No debe contener números ni caracteres especiales.")
        elif materia in lista_materias:
            print("Materia ya registrada")
        else:
            lista_materias.append(materia)
            return "Materia agregada exitosamente"

def mostrar_materias():
    if not lista_materias:
        return "No hay materias registradas"
    else:
        return "\n".join(lista_materias)



# Relación entre estudiantes y materias
diccionario_estudiantes_materias = {}

def asignar_materia_a_estudiante():
    while True:
        DNI = input("Ingrese el DNI del estudiante: ")
        
        if not DNI.isdigit():
            print("DNI inválido. Debe ser un número.")
            continue
        
        if DNI in diccionario_de_estudiantes:
            if not lista_materias:
                return "No hay materias registradas"
            
            print("Materias disponibles:")
            for materia in lista_materias:
                print(materia)
            
            while True:
                materia_asignada = input("Ingrese el nombre de la materia a asignar: ").strip()
                
                if not materia_asignada.isalpha():
                    print("Nombre de materia inválido. No debe contener números ni caracteres especiales.")
                    continue
                
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
                    print("Materia no registrada. Intente nuevamente.")
        else:
            print("Estudiante no encontrado. Intente nuevamente.")


def mostrar_materias_estudiante():
    while True:
        DNI = input("Ingrese el DNI del estudiante: ")
        
        if not DNI.isdigit():
            print("El DNI ingresado no es válido. Debe ser un número. Intente nuevamente.")
            continue
        
        if DNI in diccionario_estudiantes_materias:
            materias = diccionario_estudiantes_materias[DNI]
            if materias:
                return f"Materias asignadas al estudiante con DNI {DNI}:\n" + "\n".join(materias)
            else:
                return "El estudiante no tiene materias asignadas"
        else:
            print("Estudiante no registrado o no tiene materias asignadas. Intente nuevamente.")


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
        print(mostrar_estudiantes())
    elif opcion == '3':
        print(buscar_estudiante())
    elif opcion == '4':
        print(agregar_materia())
    elif opcion == '5':
        print(mostrar_materias())
    elif opcion == '6':
        print(asignar_materia_a_estudiante())
    elif opcion == '7':
        print(mostrar_materias_estudiante())
    elif opcion == '8':
        break
    else:
        print("Opción no válida")
