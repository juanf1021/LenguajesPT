OPERADORES = {
    '+': 'tk_suma',
    '-': 'tk_resta',
    '*': 'tk_mult',
    '/': 'tk_div',
    '**': 'tk_potencia',
    '%': 'tk_modulo',
    '//': 'tk_div_entero',
    '=': 'tk_asig',
    '==': 'tk_eq',
    '!': 'tk_negacion',
    '!=': 'tk_distinto',
    '<': 'tk_menor',
    '<=': 'tk_menor_igual',
    '>': 'tk_mayor',
    '>=': 'tk_mayor_igual',
    'and': 'tk_and',
    'or': 'tk_or',
    'not': 'tk_not',
    'is': 'tk_is',
    'in': 'tk_in',
    '~': 'tk_negacion_bitwise',
    '<<': 'tk_shift_izq',
    '>>': 'tk_shift_der',
    '&': 'tk_and_bitwise',
    '^': 'tk_xor_bitwise',
    '|': 'tk_or_bitwise',
    '.': 'tk_punto',
    ':=': 'tk_asig_rapida'
}

PALABRAS_RESERVADAS = {
    'False': 'False',
    'None': 'None',
    'True': 'True',
    'and': 'and',
    'as': 'as',
    'assert': 'assert',
    'async': 'async',
    'await': 'await',
    'break': 'break',
    'class': 'class',
    'continue': 'continue',
    'def': 'def',
    'del': 'del',
    'elif': 'elif',
    'else': 'else',
    'except': 'except',
    'finally': 'finally',
    'for': 'for',
    'from': 'from',
    'global': 'global',
    'if': 'if',
    'import': 'import',
    'in': 'in',
    'is': 'is',
    'lambda': 'lambda',
    'nonlocal': 'nonlocal',
    'not': 'not',
    'or': 'or',
    'pass': 'pass',
    'mft' : 'mft',
    'raise': 'raise',
    'return': 'return',
    'try': 'try',
    'while': 'while',
    'with': 'with',
    'yield': 'yield',
    'print': 'print',
    'range': 'range',
    'match':'match',
    'case':'case',
    'type':'type',
    '_':'_'
}

SIMBOLOS_ESPECIALES = {
    '(': 'tk_par_izq',
    ')': 'tk_par_der',
    ':': 'tk_dos_puntos',
    ',': 'tk_coma',
    '.': 'tk_punto',
    '"': 'tk_comilla_doble',
    "'": 'tk_comilla_simple',
    ';': 'tk_punto_coma',
    '{': 'tk_llave_izq',
    '}': 'tk_llave_der',
    '[': 'tk_corchete_izq',
    ']': 'tk_corchete_der',
    '!': 'tk_exclamacion',
    '@': 'tk_arroba',
    '=': 'tk_igual',
    '->': 'tk_flecha',
    '+=': 'tk_suma_asignacion',
    '-=': 'tk_resta_asignacion',
    '*=': 'tk_mult_asignacion',
    '/=': 'tk_div_asignacion',
    '//=': 'tk_div_entera_asignacion',
    '%=': 'tk_mod_asignacion',
    '@=': 'tk_arroba_asignacion',
    '&=': 'tk_and_asignacion',
    '|=': 'tk_or_asignacion',
    '^=': 'tk_xor_asignacion',
    '>>=': 'tk_shift_der_asignacion',
    '<<=': 'tk_shift_izq_asignacion',
    '**=': 'tk_potencia_asignacion',
    '#': 'tk_comentario',
    '\\': 'tk_barra_invertida',
}

def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z' or caracter == '_'

def es_digito(caracter):
    return '0' <= caracter <= '9'

def es_espacio(caracter):
    return caracter in ' \t\n'

def manejar_error_lexico(linea, columna):
    print(f">>> Error léxico(linea:{linea},posicion:{columna})")
    return None

def afd_analizador_lexico(texto):
    estado = 0
    tokens = []
    lexema = ''
    numero_linea = 1
    columna = 1
    i = 0

    while i < len(texto):
        caracter = texto[i]

        if estado == 0:  # Estado inicial
            if es_letra(caracter):
                estado = 1
                lexema += caracter
            elif es_digito(caracter):
                estado = 2
                lexema += caracter
            elif caracter == '#':
                estado = 5
            elif caracter == '"' or caracter == "'":
                estado = 6
                lexema += caracter
                columna_inicio = columna
            elif caracter in OPERADORES:
                op = caracter
                if i + 1 < len(texto) and op + texto[i + 1] in OPERADORES:
                    op += texto[i + 1]
                    i += 1
                tokens.append((OPERADORES[op], numero_linea, columna))
                columna += len(op)
                i += 1
                continue
            elif caracter in SIMBOLOS_ESPECIALES:
                tokens.append((SIMBOLOS_ESPECIALES[caracter], numero_linea, columna))
                columna += 1
                i += 1
                continue
            elif es_espacio(caracter):
                if caracter == '\n':
                    numero_linea += 1
                    columna = 1
                else:
                    columna += 1
                i += 1
                continue
            else:
                manejar_error_lexico(numero_linea, columna)
                tokens.append((f">>> Error léxico(linea:{numero_linea},posicion:{columna})", numero_linea, columna))
                return tokens

        elif estado == 1:  # Identificadores o palabras reservadas
            if es_letra(caracter) or es_digito(caracter):
                lexema += caracter
            else:
                if lexema in PALABRAS_RESERVADAS:
                    tokens.append((PALABRAS_RESERVADAS[lexema], numero_linea, columna - len(lexema)))
                else:
                    tokens.append(('id', lexema, numero_linea, columna - len(lexema)))
                lexema = ''
                estado = 0
                continue

        elif estado == 2:  # Números (enteros o flotantes)
            if es_digito(caracter):
                lexema += caracter
            elif caracter == '.' and '.' not in lexema:
                lexema += caracter
                estado = 3  # Parte decimal
            elif caracter == 'e' and 'e' not in lexema.lower():
                lexema += caracter
                estado = 4  # Notación científica
            elif caracter.lower() == 'j':
                lexema += caracter
                tokens.append(('tk_imaginario', lexema, numero_linea, columna - len(lexema)))
                lexema = ''
                estado = 0
            else:
                tokens.append(('tk_entero', lexema, numero_linea, columna - len(lexema)))
                lexema = ''
                estado = 0
                continue

        elif estado == 3:  # Parte decimal de un número flotante
            if es_digito(caracter):
                lexema += caracter
            elif caracter.lower() == 'e' and 'e' not in lexema.lower():
                lexema += caracter
                estado = 4  # Notación científica
            elif caracter.lower() == 'j':
                lexema += caracter
                tokens.append(('tk_imaginario', lexema, numero_linea, columna - len(lexema)))
                lexema = ''
                estado = 0
            else:
                tokens.append(('tk_flotante', lexema, numero_linea, columna - len(lexema)))
                lexema = ''
                estado = 0
                continue

        elif estado == 4:  # Notación científica
            if caracter in '+-' and lexema[-1].lower() == 'e':
                lexema += caracter
            elif es_digito(caracter):
                lexema += caracter
            elif caracter.lower() == 'j':
                lexema += caracter
                tokens.append(('tk_imaginario', lexema, numero_linea, columna - len(lexema)))
                lexema = ''
                estado = 0
            else:
                tokens.append(('tk_flotante', lexema, numero_linea, columna - len(lexema)))
                lexema = ''
                estado = 0
                continue

        elif estado == 5:  # Comentarios
            if caracter == '\n':
                estado = 0
                numero_linea += 1
                columna = 1
            else:
                i += 1
                columna += 1
                continue

        elif estado == 6:  # Cadenas
            if caracter == '\\':
                lexema += caracter
                if i + 1 < len(texto):
                    i += 1
                    columna += 1
                    lexema += texto[i]
            elif (caracter == '"' and lexema[0] == '"') or (caracter == "'" and lexema[0] == "'"):
                lexema += caracter
                tokens.append(('tk_cadena', lexema, numero_linea, columna_inicio))
                lexema = ''
                estado = 0
            elif caracter == '\n':
                manejar_error_lexico(numero_linea, columna)
                tokens.append((f">>> Error léxico(linea:{numero_linea},posicion:{columna})", numero_linea, columna))
                return tokens
            else:
                lexema += caracter

        i += 1
        columna += 1

    if lexema:
        if estado == 1:
            if lexema in PALABRAS_RESERVADAS:
                tokens.append((PALABRAS_RESERVADAS[lexema], numero_linea, columna - len(lexema)))
            else:
                tokens.append(('id', lexema, numero_linea, columna - len(lexema)))
        elif estado in [2, 3, 4]:
            tipo_token = 'tk_flotante' if '.' in lexema or 'e' in lexema.lower() else 'tk_entero'
            tokens.append((tipo_token, lexema, numero_linea, columna - len(lexema)))
        elif estado == 6:
            manejar_error_lexico(numero_linea, columna)
            tokens.append((f">>> Error léxico(linea:{numero_linea},posicion:{columna})", numero_linea, columna))
            return tokens

    return tokens
