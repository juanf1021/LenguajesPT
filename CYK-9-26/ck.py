import time
import matplotlib.pyplot as plt

# Función para leer la gramática desde un archivo de texto
def read_gramatica_from_file(file_path):
    grammar = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()  # Eliminar espacios en blanco
            if not line:
                continue  # Saltar líneas vacías
            lhs, rhs = line.split("->")
            lhs = lhs.strip()
            productions = rhs.split("|")
            grammar[lhs] = [prod.strip() for prod in productions]
    return grammar

# Implementación del algoritmo CYK
def cyk_algorithm(string, grammar):
    n = len(string)
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Primera fase: Población de la tabla con producciones unitarias
    for i in range(n):
        for lhs, rhs in grammar.items():
            for production in rhs:
                if production == string[i]:
                    table[i][i].add(lhs)

    # Segunda fase: Población de la tabla con producciones compuestas
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            for split in range(start, end):
                for lhs, rhs in grammar.items():
                    for production in rhs:
                        if len(production) == 2:
                            A, B = production[0], production[1]
                            if A in table[start][split] and B in table[split + 1][end]:
                                table[start][end].add(lhs)

    return 'S' in table[0][n - 1]

# Función para medir y graficar tiempos de ejecución
def measure_and_plot_execution_times(grammar, max_length=20):
    lengths = range(1, max_length + 1)
    times = []

    # Crear o abrir archivo para guardar los tiempos
    with open("Tiempos.txt", "w") as f:
        f.write("Longitud de la cadena, Tiempo de ejecución (segundos)\n")
        f.write("==============================================\n")

        for length in lengths:
            test_string = "a" * length  # Generar una cadena de longitud 'length'
            start_time = time.time()
            cyk_algorithm(test_string, grammar)
            end_time = time.time()

            execution_time = end_time - start_time
            times.append(execution_time)
            f.write(f"Longitud de la cadena: {length}, Tiempo de ejecución: {execution_time:.6f} segundos\n")
            print(f"Longitud de la cadena: {length}, Tiempo de ejecución: {execution_time:.6f} segundos")

        f.write("==============================================\n")
        f.write("Tabla de tiempos de ejecución:\n")
        f.write("Longitud\tTiempo (segundos)\n")
        for length, time_ in zip(lengths, times):
            f.write(f"{length}\t\t{time_:.6f}\n")

    # Graficar los tiempos de ejecución
    plt.plot(lengths, times, marker='o')
    plt.xlabel('Longitud de la cadena')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución del algoritmo CYK')
    plt.grid(True)
    plt.savefig("Graficos.png")  # Guardar la figura como archivo PNG
    plt.close()

# Leer la gramática desde el archivo gramatica.txt y ejecutar la medición
grammar_file_path = "gramatica.txt"
grammar = read_gramatica_from_file(grammar_file_path)
measure_and_plot_execution_times(grammar, max_length=20)
