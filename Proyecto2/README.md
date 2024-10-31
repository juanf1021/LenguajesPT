## Andres Castro, Juan Hurtado, Miguel Flechas, Juan Trujillo
# Analizador Sintáctico en Python

Este repositorio contiene un analizador sintáctico en Python diseñado para procesar y verificar un subconjunto de gramática del lenguaje Python. El analizador utiliza una **tabla de predicción** para decidir qué producciones de la gramática aplicar, permitiendo analizar de manera eficiente sin retrocesos.

## Funcionalidad General del Código

Este analizador sintáctico sigue una gramática específica que soporta construcciones básicas como:

1. Declaraciones de variables.
2. Expresiones aritméticas.
3. Bucles `for`.
4. Expresiones con paréntesis y palabras reservadas.

El analizador recibe un código fuente en formato de texto y verifica si este cumple con las reglas de la gramática establecida. Para esto, utiliza una serie de funciones que implementan cada regla de la gramática y que, en conjunto, siguen las estructuras especificadas en la **tabla de predicción**.

## Gramática Aceptada

La gramática que el analizador puede interpretar incluye las siguientes reglas:

1. **Inicio del programa** (`programa`):
   - `programa → declaraciones`

2. **Declaraciones**:
   - `declaraciones → declaracion declaraciones | ε`

3. **Declaración**:
   - `declaracion → tipo id = expresion`
   - `declaracion → for ( id in rango ) { declaraciones }`

4. **Expresión**:
   - `expresion → termino expresion'`

5. **Término y Factor**:
   - `termino → factor termino'`
   - `termino' → * factor termino' | ε`
   - `factor → ( expresion ) | id`

Estas reglas permiten construir expresiones básicas, manejar bucles `for` y asignar variables.

## Requisitos

Para ejecutar este código, necesitarás:
- **Python 3.x**

## Uso del Código

Sigue estos pasos para ejecutar el analizador sintáctico y verificar código fuente:

1. **Clona o descarga este repositorio** y asegúrate de estar en el directorio del proyecto.
2. **Prepara el código fuente** que deseas analizar en formato de texto.
3. **Ejecuta el analizador** pasándole el archivo de código fuente como entrada.

### Ejecución Básica

Asumiendo que tienes un archivo de código fuente en un archivo `codigo_fuente.txt`, puedes ejecutar el analizador de la siguiente manera:

```bash
python analizador_sintactico.py codigo_fuente.txt
```

Al ejecutar el comando, el analizador leerá el contenido de `codigo_fuente.txt` y mostrará mensajes indicando si el código cumple con la gramática establecida o si se encuentran errores.

## Funcionalidad de las Principales Clases y Funciones

### Clase `AnalizadorSintactico`
- **Propósito**: Gestiona el análisis sintáctico y contiene las reglas de la gramática.
- **Métodos Principales**:
  - `analizar()`: Inicia el proceso de análisis sintáctico.
  - `coincidir(token)`: Verifica si el token actual coincide con el token esperado y avanza al siguiente.
  - `programa()`, `declaraciones()`, `declaracion()`, `expresion()`: Cada método representa una producción de la gramática y se encarga de analizar un aspecto específico del código fuente.

### Ejemplo de Código Fuente Compatible

Este es un ejemplo de código que el analizador podría procesar sin errores:

```python
int x = 5
for (i in rango) {
    x = x * 2
}
```

En este ejemplo:
- Se declara una variable entera `x` y se le asigna el valor `5`.
- Se usa un bucle `for` para iterar en un rango, en cada iteración multiplicando `x` por `2`.

## Manejo de Errores

Si el analizador encuentra un error, el método `error(mensaje)` generará un mensaje detallado, indicando el tipo de error y el contexto en el que ocurrió.

## Tabla de Predicción

El analizador usa una tabla de predicción para decidir qué regla aplicar en función del símbolo actual y el próximo token en el código. Esta tabla se construye usando los conjuntos FIRST y FOLLOW de la gramática, optimizando el proceso de análisis.

## Contribuciones

Si deseas mejorar o extender la funcionalidad de este analizador sintáctico, puedes contribuir al proyecto de la siguiente manera:

1. **Forkea** este repositorio y crea una nueva rama para tus cambios.
2. **Desarrolla** las mejoras que desees.
3. **Realiza un Pull Request** con una breve descripción de los cambios realizados.
