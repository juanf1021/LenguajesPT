def cargar_gramatica(archivo):
    producciones = {}
    with open(archivo, 'r') as archivo_gramatica:
        for linea in archivo_gramatica:
            linea = linea.strip()
            if not linea:
                continue
            no_terminal, producciones_str = linea.split('->')
            no_terminal = no_terminal.strip()
            producciones[no_terminal] = [p.strip().split() for p in producciones_str.split('|')]
    return producciones

# Gramática cargada desde un archivo
archivo_gramatica = 'gramatica.txt'  # Cambia este nombre por el archivo que desees cargar
producciones = cargar_gramatica(archivo_gramatica)

def eliminar_recursion_izquierda(producciones):
    nuevas_producciones = {}
    for no_terminal in producciones:
        reglas = producciones[no_terminal]
        directas = []
        indirectas = []
        
        for regla in reglas:
            if regla[0] == no_terminal:
                indirectas.append(regla[1:])  # Recursión izquierda directa
            else:
                directas.append(regla)  # Regla sin recursión izquierda

        # Si hay recursión izquierda, transformamos
        if indirectas:
            nuevo_no_terminal = f"{no_terminal}'"
            while nuevo_no_terminal in producciones or nuevo_no_terminal in nuevas_producciones:
                nuevo_no_terminal += "'"

            nuevas_producciones[no_terminal] = [regla + [nuevo_no_terminal] for regla in directas]
            nuevas_producciones[nuevo_no_terminal] = [regla + [nuevo_no_terminal] for regla in indirectas]
            nuevas_producciones[nuevo_no_terminal].append(['ε'])
        else:
            nuevas_producciones[no_terminal] = directas

    return nuevas_producciones

# Función para realizar el factoring de la gramática
def factorizar(producciones):
    nuevas_producciones = {}
    for no_terminal in producciones:
        reglas = producciones[no_terminal]
        prefijos = {}

        # Agrupar reglas por prefijos comunes
        for regla in reglas:
            primer_elemento = regla[0]
            if primer_elemento not in prefijos:
                prefijos[primer_elemento] = []
            prefijos[primer_elemento].append(regla)

        if len(prefijos) == 1:
            nuevas_producciones[no_terminal] = reglas
        else:
            nuevo_no_terminal = f"{no_terminal}'"
            while nuevo_no_terminal in producciones or nuevo_no_terminal in nuevas_producciones:
                nuevo_no_terminal += "'"

            nuevas_producciones[no_terminal] = []
            for prefijo in prefijos:
                grupo = prefijos[prefijo]
                if len(grupo) == 1:
                    nuevas_producciones[no_terminal].append(grupo[0])
                else:
                    nuevas_producciones[no_terminal].append([prefijo, nuevo_no_terminal])
                    nuevas_producciones[nuevo_no_terminal] = [[item for item in regla[1:]] if len(regla) > 1 else ['ε'] for regla in grupo]

    return nuevas_producciones

# Paso 1: Eliminar recursión izquierda
producciones = eliminar_recursion_izquierda(producciones)
print("Después de eliminar la recursión izquierda:")
for no_terminal, reglas in producciones.items():
    print(f"{no_terminal} -> {' | '.join([' '.join(r) for r in reglas])}")

# Paso 2: Factorizar
producciones = factorizar(producciones)
print("\nDespués de factorizar:")
for no_terminal, reglas in producciones.items():
    print(f"{no_terminal} -> {' | '.join([' '.join(r) for r in reglas])}")