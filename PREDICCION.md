Juan Hurtado, Miguel Flechas, Andres Castro, Juan Trujillo

```markdown
# Procesador de Gramáticas Libre de Contexto

Este repositorio contiene implementaciones para el manejo de gramáticas libres de contexto, incluyendo funciones para:
- El cálculo de los conjuntos **Primeros**, **Siguientes** y **Predicción**.
- La **eliminación de recursión por la izquierda**.
- El **factorizado** de producciones para optimizar las gramáticas.

Estas herramientas permiten analizar y transformar gramáticas, facilitando su uso en compiladores y otros procesadores de lenguaje.

## Archivos Principales

- **`gramatica.txt`**: Archivo de entrada que contiene las producciones de la gramática en un formato específico. Cada línea sigue el formato:  
  ```
  NoTerminal -> producción1 | producción2 | ...
  ```
  Ejemplo:
  ```
  E -> T E'
  E' -> + T E' | ε
  ```

- **`calculo_gramatica.py`**: Este archivo incluye las funciones para:
  - **Cargar la gramática** desde un archivo de texto.
  - **Calcular los conjuntos Primeros, Siguientes y Predicción**.
  - **Eliminar la recursión por la izquierda**.
  - **Factorizar las producciones**.

## Cómo usar estos códigos

### 1. Cargar la gramática

El archivo `gramatica.txt` es cargado mediante la función `cargar_gramatica(archivo)`. Este archivo debe estar en el mismo directorio que el script de Python o especificar su ruta completa.

```python
producciones = cargar_gramatica('gramatica.txt')
```

### 2. Eliminar la recursión por la izquierda

La función `eliminar_recursion_izquierda` detecta y elimina la recursión izquierda directa de las producciones. Esto es importante para garantizar que las gramáticas puedan ser usadas en analizadores sintácticos que requieren gramáticas sin recursión izquierda.

```python
producciones_sin_recursion = eliminar_recursion_izquierda(producciones)
```

### 3. Factorizar las producciones

La función `factorizar` reorganiza las producciones, agrupando aquellas que tienen prefijos comunes, mejorando la legibilidad y facilitando el análisis descendente de las gramáticas.

```python
producciones_factorizadas = factorizar(producciones_sin_recursion)
```

### 4. Calcular conjuntos Primeros y Siguientes

- **Primeros**: Para un símbolo no terminal, este conjunto contiene los terminales que pueden aparecer al inicio de una cadena derivada.
- **Siguientes**: Para un símbolo no terminal, este conjunto contiene los terminales que pueden aparecer justo después de dicho símbolo en alguna derivación.
  
Usa la función `calcular_primeros` para obtener el conjunto de **Primeros**, y `calcular_siguientes` para el conjunto de **Siguientes**.

```python
primeros = calcular_primeros(producciones)
siguientes = calcular_siguientes(producciones, primeros)
```

### 5. Calcular el conjunto de Predicción

El conjunto de **Predicción** combina los resultados de **Primeros** y **Siguientes** para determinar cuáles terminales pueden iniciar una derivación en una producción específica.

```python
predicciones = calcular_prediccion(producciones, primeros, siguientes)
```

### Ejecución

Ejecuta el script `calculo_gramatica.py` para realizar las transformaciones y cálculos. El script imprimirá los conjuntos **Primeros**, **Siguientes**, y **Predicción**, además de las producciones transformadas después de la eliminación de la recursión por la izquierda y la factorización.

### Ejemplo de uso:

```bash
python calculo_gramatica.py
```

## Salida esperada

Al ejecutar el script, obtendrás:

1. **Conjunto Primeros** para cada no terminal.
2. **Conjunto Siguientes** para cada no terminal.
3. **Conjunto Predicción** para cada producción.


