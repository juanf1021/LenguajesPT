# Función para leer el archivo y convertirlo en un diccionario de producciones
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


def calcular_primeros(producciones):
    primeros = {nt: set() for nt in producciones}

    def primeros_de_simbolo(simbolo):
        if simbolo not in producciones:
            return {simbolo}
        if simbolo in primeros and primeros[simbolo]:
            return primeros[simbolo]
        for produccion in producciones[simbolo]:
            for s in produccion:
                simbolos_primeros = primeros_de_simbolo(s)
                primeros[simbolo].update(simbolos_primeros - {'ε'})
                if 'ε' not in simbolos_primeros:
                    break
            else:
                primeros[simbolo].add('ε')
        return primeros[simbolo]

    for nt in producciones:
        primeros_de_simbolo(nt)
    return primeros

def calcular_siguientes(producciones, primeros):
    siguientes = {nt: set() for nt in producciones}
    siguientes['E'].add('$')

    while True:
        cambios = False
        for nt in producciones:
            for produccion in producciones[nt]:
                for i, simbolo in enumerate(produccion):
                    if simbolo not in producciones:
                        continue
                    restantes = produccion[i + 1:]
                    conjunto_primeros = calcular_primeros_para_cadena(restantes, primeros)
                    if 'ε' in conjunto_primeros:
                        conjunto_primeros.remove('ε')
                        conjunto_primeros.update(siguientes[nt])
                    if not conjunto_primeros <= siguientes[simbolo]:
                        siguientes[simbolo].update(conjunto_primeros)
                        cambios = True
        if not cambios:
            break
    return siguientes

def calcular_primeros_para_cadena(cadena, primeros):
    resultado = set()
    for simbolo in cadena:
        simbolos_primeros = primeros[simbolo] if simbolo in primeros else {simbolo}
        resultado.update(simbolos_primeros - {'ε'})
        if 'ε' not in simbolos_primeros:
            break
    else:
        resultado.add('ε')
    return resultado

def calcular_prediccion(producciones, primeros, siguientes):
    predicciones = {}
    for nt in producciones:
        for produccion in producciones[nt]:
            primeros_produccion = calcular_primeros_para_cadena(produccion, primeros)
            if 'ε' in primeros_produccion:
                primeros_produccion.remove('ε')
                primeros_produccion.update(siguientes[nt])
            predicciones[(nt, tuple(produccion))] = primeros_produccion
    return predicciones

# Ejecutar el cálculo
primeros = calcular_primeros(producciones)
siguientes = calcular_siguientes(producciones, primeros)
predicciones = calcular_prediccion(producciones, primeros, siguientes)

print("Conjunto Primeros:")
for nt, conjunto in primeros.items():
    print(f"{nt}: {conjunto}")

print("\nConjunto Siguientes:")
for nt, conjunto in siguientes.items():
    print(f"{nt}: {conjunto}")

print("\nConjunto Prediccion:")
for (nt, produccion), conjunto in predicciones.items():
    print(f"{nt} -> {' '.join(produccion)}: {conjunto}")