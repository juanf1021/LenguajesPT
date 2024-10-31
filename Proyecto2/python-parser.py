from afd import afd_analizador_lexico, PALABRAS_RESERVADAS
import sys

# Clase AnalizadorSintactico con gramática mejorada para for y expresiones
class AnalizadorSintactico:
    def __init__(self):
        self.tokens = []
        self.posicion_actual = 0
        self.token_actual = None	
        self.linea_actual = 1
        self.columna_actual = 1
        self.variables_definidas = set()
        self.palabras_reservadas = PALABRAS_RESERVADAS.copy()
        self.built_ins = {
            'print', 'input', 'len', 'int', 'str', 'float', 'bool', 'list', 
            'dict', 'set', 'tuple', 'range', 'sum', 'max', 'min', 'abs',
            'round', 'sorted', 'enumerate', 'zip', 'map', 'filter', 'any',
            'all', 'chr', 'ord', 'pow', 'type', 'math'
        }
        
        # Gramática ajustada para aceptar comprensiones de listas, índices, y funciones en expresiones
        self.gramatica = {
            'programa': [['declaraciones']],
            'declaraciones': [['declaracion', 'declaraciones'], ['ε']],
            'declaracion': [
                ['clase'],
                ['def', 'id', 'tk_par_izq', 'parametros', 'tk_par_der', 'tk_dos_puntos', 'bloque'],
                ['if_stmt'], 
                ['while', 'expresion', 'tk_dos_puntos', 'bloque'],
                ['for', 'id', 'in', 'expresion', 'tk_dos_puntos', 'bloque'],
                ['print', 'print_args'],
                ['return', 'expresion'],
                ['expresion_stmt'],
                ['importacion']  
            ],
            'if_stmt': [  
                ['if', 'expresion', 'tk_dos_puntos', 'bloque', 'elif_stmt', 'else_parte']
            ],
            'elif_stmt': [
                ['elif', 'expresion', 'tk_dos_puntos', 'bloque', 'elif_stmt'],
                ['ε']
            ],
            'else_parte': [
                ['else', 'tk_dos_puntos', 'bloque'],
                ['ε']
            ],
            'clase': [
                ['class', 'id', 'herencia_opt', 'tk_dos_puntos', 'bloque']
            ],
            'herencia_opt': [
                ['tk_par_izq', 'id', 'herencia_lista', 'tk_par_der'],
                ['ε']
            ],
            'herencia_lista': [
                ['tk_coma', 'id', 'herencia_lista'],
                ['ε']
            ],
            'importacion': [
                ['import', 'id', 'import_lista'],
                ['from', 'id', 'import', 'id', 'import_lista']
            ],
            'import_lista': [
                ['tk_coma', 'id', 'import_lista'],
                ['ε']
            ],
            'print_args': [
                ['tk_par_izq', 'arg_lista', 'tk_par_der']
            ],
            'arg_lista': [
                ['expresion', 'arg_lista_prima'],
                ['ε']
            ],
            'arg_lista_prima': [
                ['tk_coma', 'expresion', 'arg_lista_prima'],
                ['ε']
            ],
            'expresion_stmt': [
                ['expresion']
            ],
            'parametros': [
                ['param', 'param_lista'],
                ['ε']
            ],
            'param_lista': [
                ['tk_coma', 'param', 'param_lista'],
                ['ε']
            ],
            'param': [
                ['id', 'tipo_opt']
            ],
            'tipo_opt': [
                ['tk_asig', 'tk_entero'],
                ['tk_dos_puntos', 'tipo'],
                ['ε']
            ],
            'tipo': [
                ['id'],
                ['tk_corchete_izq', 'tipo', 'tk_corchete_der']
            ],
            'bloque': [
                ['INDENT', 'declaraciones', 'DEDENT']
            ],
            'expresion': [
                ['termino', 'expresion_logica']
            ],
            'expresion_logica': [
                ['tk_igual', 'termino', 'expresion_logica'],
                ['tk_distinto', 'termino', 'expresion_logica'],
                ['tk_menor', 'termino', 'expresion_logica'],
                ['tk_menor_igual', 'termino', 'expresion_logica'],
                ['tk_mayor', 'termino', 'expresion_logica'],
                ['tk_mayor_igual', 'termino', 'expresion_logica'],
                ['tk_and', 'termino', 'expresion_logica'],
                ['tk_or', 'termino', 'expresion_logica'],
                ['tk_eq','termino', 'expresion_logica'],
                ['ε']
            ],
            'termino': [
                ['factor', 'termino_prima']
            ],
            'termino_prima': [
                ['tk_mult', 'factor', 'termino_prima'],
                ['tk_div', 'factor', 'termino_prima'],
                ['ε']
            ],
            'factor': [
                ['tk_par_izq', 'expresion', 'tk_par_der'],  # Agrupación con ()
                ['tk_corchete_izq', 'lista_contenido', 'tk_corchete_der'],  # Listas con múltiples elementos
                ['num_id', 'asig'],                                  
                ['tk_entero'],                                   
                ['tk_flotante'],                                 
                ['tk_cadena'],                                   
                ['range', 'tk_par_izq', 'arg_lista', 'tk_par_der']  
            ],
            'lista_contenido': [  # Regla para contenido de listas
                ['expresion', 'lista_contenido_prima'],
                ['ε']
            ],
            'lista_contenido_prima': [
                ['tk_coma', 'expresion', 'lista_contenido_prima'],
                ['ε']
            ],
            'indice_acceso': [  # Acceso por índice en listas y tuplas
                ['tk_corchete_izq', 'expresion', 'tk_corchete_der'],
                ['ε']
            ],
            'asig': [
                ['tk_coma', 'num_id', 'asig'],
                ['tk_asig', 'expresion'],
                ['tk_par_izq', 'arg_lista', 'tk_par_der'],
                ['tk_punto', 'id'],
                ['indice_acceso'],
                ['tk_entero'],
                ['tk_cadena'], 
                ['tk_resta', 'op'],
                ['tk_suma', 'op'],
                ['ε']
            ],
            'op': [
                ['tk_asig'],
                ['tk_suma'],
                ['tk_resta'],
                ['ε']
            ],
            'num_id': [
                ['id'],
                ['tk_entero']
            ]
        }

        # Cálculo de conjuntos PRIMEROS, SIGUIENTES, y tabla de predicción
        self.primeros = self.calcular_primeros()
        self.siguientes = self.calcular_siguientes()
        self.tabla_prediccion = self.construir_tabla_prediccion()







    def calcular_primeros(self):
        primeros = {}
        for no_terminal in self.gramatica:
            primeros[no_terminal] = set()
        cambio = True
        while cambio:
            cambio = False
            for no_terminal, producciones in self.gramatica.items():
                for produccion in producciones:
                    if not produccion or produccion[0] == 'ε':
                        if 'ε' not in primeros[no_terminal]:
                            primeros[no_terminal].add('ε')
                            cambio = True
                        continue
                    first_symbol = produccion[0]
                    if first_symbol not in self.gramatica:
                        if first_symbol not in primeros[no_terminal]:
                            primeros[no_terminal].add(first_symbol)
                            cambio = True
                    else:
                        for first in primeros[first_symbol]:
                            if first != 'ε' and first not in primeros[no_terminal]:
                                primeros[no_terminal].add(first)
                                cambio = True
        return primeros

    def calcular_siguientes(self):
        siguientes = {nt: set() for nt in self.gramatica}
        siguientes['programa'].add('$')
        cambio = True
        while cambio:
            cambio = False
            for no_terminal, producciones in self.gramatica.items():
                for produccion in producciones:
                    for i, simbolo in enumerate(produccion):
                        if simbolo in self.gramatica:
                            resto = produccion[i+1:]
                            if not resto:
                                for follow in siguientes[no_terminal]:
                                    if follow not in siguientes[simbolo]:
                                        siguientes[simbolo].add(follow)
                                        cambio = True
                            else:
                                primeros_resto = self.calcular_primeros_cadena(resto)
                                for first in primeros_resto - {'ε'}:
                                    if first not in siguientes[simbolo]:
                                        siguientes[simbolo].add(first)
                                        cambio = True
                                if 'ε' in primeros_resto:
                                    for follow in siguientes[no_terminal]:
                                        if follow not in siguientes[simbolo]:
                                            siguientes[simbolo].add(follow)
                                            cambio = True
        return siguientes

    def calcular_primeros_cadena(self, cadena):
        if not cadena:
            return {'ε'}
        resultado = set()
        todos_epsilon = True
        for simbolo in cadena:
            if simbolo in self.gramatica:
                primeros_simbolo = self.primeros[simbolo]
            else:
                primeros_simbolo = {simbolo}
            resultado.update(primeros_simbolo - {'ε'})
            if 'ε' not in primeros_simbolo:
                todos_epsilon = False
                break
        if todos_epsilon:
            resultado.add('ε')
        return resultado

    def construir_tabla_prediccion(self):
        tabla = {}
        for no_terminal, producciones in self.gramatica.items():
            tabla[no_terminal] = {}
            for i, produccion in enumerate(producciones):
                primeros_produccion = self.calcular_primeros_cadena(produccion)
                for terminal in primeros_produccion - {'ε'}:
                    tabla[no_terminal][terminal] = (produccion, i)
                if 'ε' in primeros_produccion:
                    for terminal in self.siguientes[no_terminal]:
                        if terminal not in tabla[no_terminal]:
                            tabla[no_terminal][terminal] = (produccion, i)
    
        return tabla

    def analizar(self, tokens):
        self.tokens = tokens
        self.posicion_actual = 0
        self.obtener_siguiente_token()
        try:
            self.programa()
            if self.token_actual[0] != '$':
                self.error(['$'])
            print("El analisis sintactico ha finalizado exitosamente.")
        except Exception as e:
            print(str(e))

    def obtener_siguiente_token(self):
        if self.posicion_actual < len(self.tokens):
            self.token_actual = self.tokens[self.posicion_actual]
            self.posicion_actual += 1
            if len(self.token_actual) >= 3:
                self.linea_actual = self.token_actual[1]
                self.columna_actual = self.token_actual[2]
        else:
            self.token_actual = ('$', self.linea_actual, self.columna_actual)

    def error(self, esperados):
        if isinstance(self.token_actual, tuple):
        # Si el token es un identificador ('id', nombre, línea, columna)
            if self.token_actual[0] == 'id':
                token = self.token_actual[1]  # Usar el lexema del identificador
            else:
            # Si es una palabra reservada o símbolo especial, usar el primer elemento
                token = self.token_actual[0]
        else:
            token = self.token_actual

        esperados_str = '", "'.join(esperados)
        raise Exception(f'<{self.linea_actual},{self.columna_actual}> Error sintactico: se encontro: "{token}"; se esperaba: "{esperados_str}"')

    def coincidir(self, token_esperado):
        if isinstance(self.token_actual, tuple) and len(self.token_actual) == 4:
            lexema = self.token_actual[1]
            if token_esperado == 'id':
                next_token = self.tokens[self.posicion_actual][0] if self.posicion_actual < len(self.tokens) else None
                if next_token == 'tk_igual':
                    self.variables_definidas.add(lexema)
            self.obtener_siguiente_token()
        elif self.token_actual[0] == token_esperado:
            self.obtener_siguiente_token()
        else:
            self.error([token_esperado])

    def programa(self):
        self._procesar_no_terminal('programa')

    def _procesar_no_terminal(self, no_terminal):
        token_actual = self.token_actual[0]
        if token_actual not in self.tabla_prediccion[no_terminal]:
            esperados = list(self.tabla_prediccion[no_terminal].keys())
            self.error(esperados)
        produccion, _ = self.tabla_prediccion[no_terminal][token_actual]
        for simbolo in produccion:
            if simbolo == 'ε':
                continue
            elif simbolo in self.gramatica:
                self._procesar_no_terminal(simbolo)
            else:
                self.coincidir(simbolo)

def main(archivo_entrada):
    with open(archivo_entrada, 'r') as f:
        contenido = f.read()
    tokens = afd_analizador_lexico(contenido)
    if not tokens:
        return
    parser = AnalizadorSintactico()
    parser.analizar(tokens)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo_entrada>")
        sys.exit(1)
    archivo_entrada = sys.argv[1]
    main(archivo_entrada)

