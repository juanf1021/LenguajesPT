import networkx as nx
import matplotlib.pyplot as plt

# Función para leer el archivo de gramática y analizar las reglas
def leer_gramatica(archivo):
    reglas = {}
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if '->' in linea:
                izquierda, derecha = linea.split('->')
                izquierda = izquierda.strip()
                # Guardar todas las producciones en una lista
                if izquierda not in reglas:
                    reglas[izquierda] = []
                derecha_partes = [parte.strip() for parte in derecha.split()]
                reglas[izquierda].append(derecha_partes)
    return reglas

# Función para generar el árbol gramatical usando las reglas según una cadena
def generar_arbol_cadena(gramatica, cadena, simbolo_inicial='E'):
    G = nx.DiGraph()  # Grafo dirigido
    if verificar(gramatica, cadena.split(), simbolo_inicial, G, simbolo_inicial):
        return G
    else:
        raise ValueError("La cadena no es aceptada por la gramática.")

# Función auxiliar para verificar y agregar reglas al grafo de árbol
def verificar(gramatica, cadena, simbolo, G, padre):
    if not cadena and simbolo not in gramatica:  # Cadena vacía y no hay más producciones
        return True
    if simbolo in gramatica:
        for produccion in gramatica[simbolo]:
            if verificar_produccion(gramatica, produccion, cadena, G, padre):
                return True
    return False

def verificar_produccion(gramatica, produccion, cadena, G, padre):
    if len(produccion) > len(cadena):
        return False  # Más símbolos en la producción que en la cadena
    for i, simbolo in enumerate(produccion):
        if simbolo in gramatica:  # Es un no terminal
            G.add_edge(padre, simbolo)  # Agregar arista al grafo
            if not verificar(gramatica, cadena[i:], simbolo, G, simbolo):
                return False
        elif simbolo != cadena[i]:  # Es un terminal y no coincide
            return False
        else:  # Coincidencia de terminal
            G.add_edge(padre, simbolo)  # Agregar arista al grafo
    return True

# Función para dibujar el árbol
def dibujar_arbol(G):
    plt.figure(figsize=(10, 8))
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot')  # Disposición del gráfico de arriba hacia abajo
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
    plt.show()

# Programa principal
if __name__ == '__main__':
    archivo_gramatica = 'gramatica.txt'  # Especificar el archivo de gramática
    gramatica = leer_gramatica(archivo_gramatica)  # Leer y analizar la gramática
    print("Gramática:", gramatica)

    # Pedir al usuario que ingrese una cadena
    cadena_usuario = input("Ingrese una cadena para verificar si es aceptada por la gramática: ")
    
    try:
        arbol = generar_arbol_cadena(gramatica, cadena_usuario)  # Generar el árbol a partir de la cadena
        dibujar_arbol(arbol)  # Dibujar el árbol
        print("La cadena es aceptada y se ha generado el árbol.")
    except ValueError as e:
        print(e)





