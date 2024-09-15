Juan Hurtado, Miguel Flechas, Andrés Castro, Juan Trujillo
```markdown
# Analizador Léxico en Python

Este proyecto es un analizador léxico escrito en Python, diseñado para procesar código fuente en Python y generar una lista de tokens según un conjunto de reglas predefinidas. Analiza el código de entrada, identifica componentes como operadores, identificadores, palabras reservadas y literales, y proporciona los tokens correspondientes.

## Características

- **Reconocimiento de palabras reservadas, operadores y símbolos**: El analizador identifica las palabras reservadas de Python, operadores aritméticos, lógicos y otros símbolos especiales.
- **Generación de tokens**: El resultado es una lista de tokens que incluye el tipo de token, número de línea y número de columna.
- **Detección de errores**: Si se encuentra un error léxico, el programa detiene su ejecución y muestra un mensaje con la línea y columna donde se produjo el error.

## Archivos

- `main.py`: Script principal que lee el archivo de entrada, ejecuta el análisis léxico y escribe los tokens en un archivo de salida.
- `afd.py`: Contiene la lógica principal del analizador léxico, incluyendo el reconocimiento de tokens y las transiciones de estado.
- `pruebaError.py`: Ejemplo de archivo Python utilizado para probar el análisis léxico.
- `tokens_salida.txt`: Archivo de salida donde se escriben los tokens generados.

## Cómo Funciona

El analizador léxico lee un archivo fuente en Python, procesa cada carácter y utiliza un autómata finito para identificar los tokens. Los tokens reconocidos incluyen:

- **Palabras reservadas**: Palabras clave de Python como `if`, `else`, `while`, etc.
- **Operadores**: Operadores aritméticos y lógicos como `+`, `-`, `==`, `!=`, etc.
- **Símbolos**: Símbolos especiales como paréntesis `(`, `)`, comas `,`, dos puntos `:`, etc.
- **Identificadores**: Nombres de variables, funciones, etc.
- **Literales**: Números enteros, flotantes, cadenas de texto, etc.
- **Comentarios**: Se ignoran los comentarios de una línea.
- **Errores**: Si se detecta un carácter inválido o una secuencia no reconocida, el programa reporta el error y su ubicación.

### Ejemplo de Entrada

```python
class Animal:
    makes_noise = False

    def sound(self):
        return "??"

cow = Animal()
cow.sound()
```

### Ejemplo de Salida

```
<class,1,1>
<id,Animal,1,7>
<tk_dos_puntos,1,13>
<id,makes_noise,2,5>
<tk_asig,2,17>
<False,2,19>
<def,4,5>
<id,sound,4,9>
<tk_par_izq,4,14>
<id,self,4,15>
<tk_par_der,4,19>
<tk_dos_puntos,4,20>
<return,5,9>
<tk_cadena,"??",5,16>
<id,cow,7,1>
<tk_asig,7,5>
<id,Animal,7,7>
<tk_par_izq,7,13>
<tk_par_der,7,14>
<id,cow,8,1>
<tk_punto,8,4>
<id,sound,8,5>
<tk_par_izq,8,10>
<tk_par_der,8,11>
```

## Cómo Usar

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-repo/analizador-lexico-python.git
   cd analizador-lexico-python
   ```

2. Prepara tu archivo de entrada en Python (por ejemplo, `pruebaError.py`) que contiene el código Python que deseas analizar.

3. Ejecuta el analizador léxico con el siguiente comando:

   ```bash
   python main.py <archivo_entrada.py> <archivo_salida.txt>
   ```

   Reemplaza `<archivo_entrada.py>` con la ruta a tu archivo fuente en Python, y `<archivo_salida.txt>` con el archivo de salida donde se escribirán los tokens.

   Ejemplo:

   ```bash
   python main.py pruebaError.py tokens_salida.txt
   ```

4. Revisa el archivo `tokens_salida.txt` para ver la lista de tokens generados por el análisis léxico.

## Manejo de Errores

Si el analizador léxico detecta un carácter o secuencia inválida, mostrará un mensaje de error y detendrá el procesamiento. El formato del mensaje de error es el siguiente:

```
>>> Error léxico(linea:X,posicion:Y)
```

Donde `X` es el número de línea y `Y` es la columna donde ocurrió el error.
