


import os

# Archivo donde se almacenarán los contactos
archivo_contactos = "agenda_contactos.txt"

# Función para cargar contactos desde el archivo
def cargar_contactos():
    contactos = []
    if os.path.exists(archivo_contactos):
        with open(archivo_contactos, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:  # Asegurarse de que hay tres elementos
                    contactos.append({"nombre": datos[0], "teléfono": datos[1], "email": datos[2]})
    return contactos

# Función para guardar contactos en el archivo
def guardar_contactos(contactos):
    with open(archivo_contactos, "w") as archivo:
        for contacto in contactos:
            archivo.write(f"{contacto['nombre']},{contacto['teléfono']},{contacto['email']}\n")

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- MENÚ DE AGENDA ---")
    print("1. Registrar un nuevo contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar un contacto")
    print("4. Modificar un contacto")
    print("5. Eliminar un contacto")
    print("6. Salir")

# Función principal
def main():
    contactos = cargar_contactos()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            # Registrar un nuevo contacto
            nombre = input("Ingrese el nombre: ").strip()
            teléfono = input("Ingrese el teléfono: ").strip()
            email = input("Ingrese el email: ").strip()
            if nombre and teléfono and email:
                contactos.append({"nombre": nombre, "teléfono": teléfono, "email": email})
                guardar_contactos(contactos)
                print("Contacto registrado con éxito.")
            else:
                print("Todos los campos son obligatorios.")
        
        elif opcion == "2":
            # Ver todos los contactos
            if not contactos:
                print("No hay contactos registrados.")
            else:
                print("\n--- LISTA DE CONTACTOS ---")
                for i, contacto in enumerate(contactos, start=1):
                    print(f"{i}. {contacto['nombre']} - {contacto['teléfono']} - {contacto['email']}")
        
        elif opcion == "3":
            # Buscar un contacto
            buscar = input("Ingrese el nombre del contacto a buscar: ").strip()
            encontrados = [c for c in contactos if buscar.lower() in c["nombre"].lower()]
            if encontrados:
                print("\n--- CONTACTOS ENCONTRADOS ---")
                for contacto in encontrados:
                    print(f"{contacto['nombre']} - {contacto['teléfono']} - {contacto['email']}")
            else:
                print("No se encontraron contactos con ese nombre.")
        
        elif opcion == "4":
            # Modificar un contacto
            buscar = input("Ingrese el nombre del contacto a modificar: ").strip()
            for i, contacto in enumerate(contactos):
                if buscar.lower() == contacto["nombre"].lower():
                    print(f"Modificando el contacto: {contacto['nombre']} - {contacto['teléfono']} - {contacto['email']}")
                    contacto["nombre"] = input("Nuevo nombre (dejar vacío para no cambiar): ").strip() or contacto["nombre"]
                    contacto["teléfono"] = input("Nuevo teléfono (dejar vacío para no cambiar): ").strip() or contacto["teléfono"]
                    contacto["email"] = input("Nuevo email (dejar vacío para no cambiar): ").strip() or contacto["email"]
                    contactos[i] = contacto
                    guardar_contactos(contactos)
                    print("Contacto modificado con éxito.")
                    break
            else:
                print("No se encontró un contacto con ese nombre.")
        
        elif opcion == "5":
            # Eliminar un contacto
            buscar = input("Ingrese el nombre del contacto a eliminar: ").strip()
            confirmacion = input(f"¿Está seguro de eliminar a {buscar}? (s/n): ").strip().lower()
            if confirmacion == "s":
                contactos = [c for c in contactos if buscar.lower() != c["nombre"].lower()]
                guardar_contactos(contactos)
                print("Contacto eliminado con éxito.")
            else:
                print("Eliminación cancelada.")
        
        elif opcion == "6":
            # Salir
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
