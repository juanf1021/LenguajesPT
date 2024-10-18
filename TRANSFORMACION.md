```markdown
# Transformación de Gramáticas a LL(1)

Este repositorio contiene un script de Python que realiza la transformación de gramáticas libres de contexto (CFG) en gramáticas LL(1). El proceso incluye la **eliminación de recursión por la izquierda** y el **factoring**, que son pasos fundamentales para convertir una gramática en una forma adecuada para análisis sintáctico predictivo.

## Archivos Principales

- **`gramatica.txt`**: Este archivo contiene las producciones de la gramática en un formato estándar. Cada línea debe tener el siguiente formato:  
  ```
  NoTerminal -> producción1 | producción2 | ...
  ```
  Ejemplo:
  ```
  E -> T E'
  E' -> + T E' | ε
  ```

- **`transformacion_LL1.py`**: Este script realiza los siguientes pasos sobre la gramática:
  - **Eliminación de recursión por la izquierda**: Identifica las producciones recursivas y las transforma para eliminar la recursión directa.
  - **Factoring**: Agrupa las producciones con prefijos comunes, eliminando ambigüedades y facilitando su uso en analizadores sintácticos descendentes.

## Cómo usar este código

### 1. Cargar la gramática

El archivo `gramatica.txt` se carga usando la función `cargar_gramatica(archivo)`. El archivo de gramática debe estar en el mismo directorio que el script de Python o se puede especificar la ruta completa.

```python
producciones = cargar_gramatica('gramatica.txt')
```

### 2. Eliminar la recursión por la izquierda

La recursión por la izquierda es un problema común en las gramáticas que impide su uso en análisis predictivos. Usa la función `eliminar_recursion_izquierda` para transformar producciones con recursión por la izquierda directa.

```python
producciones_sin_recursion = eliminar_recursion_izquierda(producciones)
```

### 3. Factorizar las producciones

El factor común en las producciones se elimina usando la técnica de **factoring**, que reorganiza las reglas con prefijos comunes. La función `factorizar` implementa esta técnica para simplificar la gramática.

```python
producciones_factorizadas = factorizar(producciones_sin_recursion)
```

### 4. Ejecución Completa

El script transforma una gramática cargada desde un archivo, primero eliminando la recursión por la izquierda y luego realizando el factoring. Ejecuta el script de la siguiente manera para ver las producciones transformadas:

```bash
python transformacion_LL1.py
```

### Ejemplo de ejecución:

Después de cargar la gramática y aplicar las transformaciones, el script imprimirá la gramática resultante, con las producciones libres de recursión por la izquierda y factorizadas.

```python
# Paso 1: Cargar la gramática
producciones = cargar_gramatica('gramatica.txt')

# Paso 2: Eliminar la recursión por la izquierda
producciones_sin_recursion = eliminar_recursion_izquierda(producciones)

# Paso 3: Factorizar las producciones
producciones_factorizadas = factorizar(producciones_sin_recursion)

# Mostrar el resultado
for no_terminal, reglas in producciones_factorizadas.items():
    print(f"{no_terminal} -> {' | '.join([' '.join(r) for r in reglas])}")
```

### Salida esperada:

El script mostrará una salida similar a la siguiente:

```
Después de eliminar la recursión izquierda:
E -> T E'
E' -> + T E' | ε
T -> F T'
T' -> * F T' | ε
F -> ( E ) | id

Después de factorizar:
E -> T E'
E' -> + T E' | ε
T -> F T'
T' -> * F T' | ε
F -> ( E ) | id
```

## Detalles Técnicos

- **Eliminación de recursión por la izquierda**: 
  - Cuando se detecta una producción de la forma `A -> Aα | β`, la producción es transformada en:
    ```
    A -> βA'
    A' -> αA' | ε
    ```

- **Factoring**: 
  - Agrupa producciones que comparten un prefijo común en una nueva producción con un nuevo no terminal.
    Ejemplo:
    ```
    A -> ab | ac
    ```
    Se transforma en:
    ```
    A -> aA'
    A' -> b | c
    ```

## Requisitos

- **Python 3.x**: Asegúrate de tener instalada la versión 3.x de Python para ejecutar los scripts.
- **Archivo de gramática (`gramatica.txt`)**: Debe contener las reglas de la gramática que se desea transformar.
