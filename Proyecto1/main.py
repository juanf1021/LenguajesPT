import sys
from afd import afd_analizador_lexico

def leer_archivo(archivo_entrada):
    with open(archivo_entrada, 'r') as archivo:
        contenido = archivo.read()
    return contenido

def escribir_salida(tokens, archivo_salida):
    with open(archivo_salida, 'w') as archivo:
        for token in tokens:
            if len(token) == 3:  # Para tokens sin lexema
                archivo.write(f"<{token[0]},{token[1]},{token[2]}>\n")
            else:  # Para tokens con lexema
                archivo.write(f"<{token[0]},{token[1]},{token[2]},{token[3]}>\n")

def analizador_lexico(archivo_entrada, archivo_salida):
    contenido = leer_archivo(archivo_entrada)
    tokens = afd_analizador_lexico(contenido)
    if tokens is None:
        return  # Abortar si se encontró un error léxico
    escribir_salida(tokens, archivo_salida)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    analizador_lexico(archivo_entrada, archivo_salida)
