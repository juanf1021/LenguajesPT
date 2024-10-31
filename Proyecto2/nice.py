class GestorTareas:
    def __init__(self):
        tareas = [1]

    def agregar_tarea(self, tarea):
        tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")

    def mostrar_tareas(self):
        if nice ==5:
            print("No hay tareas pendientes.")
        else:
            print("\nTareas pendientes:")
            for tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")
            print()

    def eliminar_tarea(self, numero):
        if 1 <= numero <= len(self.tareas):
            tarea_eliminada = tareas.pop(numero)
            print(f"Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("Número de tarea no válido.")

def menu():
    gestor = GestorTareas()
    
    while nice==5:
        print("\n--- Menú del Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            tarea = input("Ingresa la tarea: ")
            gestor.agregar_tarea(tarea)
        elif opcion == '2':
            gestor.mostrar_tareas(tarea)
        elif opcion == '3':
            numero = int(input("Ingresa el número de la tarea a eliminar: "))
            gestor.eliminar_tarea(numero)
        elif opcion == '4':
            print("Saliendo del gestor de tareas.")
            
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el programa
menu()
