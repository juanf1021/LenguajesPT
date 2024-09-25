#Juan Hurtado, Andres Castro, Miguel Flechas, Juan Trujillo
# Generador de Árbol Gramatical en Python

## Descripción
Este programa, almacenado en el archivo `arbol.py`, toma una gramática formal desde el archivo `gramatica.txt`, la lee y genera un árbol gramatical en función de las reglas especificadas. Verifica si una cadena proporcionada por el usuario es aceptada por la gramática y, en caso afirmativo, dibuja el árbol correspondiente utilizando la librería `NetworkX` y `Matplotlib`.

## Requisitos

Asegúrate de tener instaladas las siguientes librerías de Python antes de ejecutar el código:

```bash
pip install networkx matplotlib pygraphviz
```

Además, necesitarás tener Graphviz instalado para generar y visualizar el árbol. Puedes descargarlo desde [Graphviz](https://graphviz.gitlab.io/download/).

## Uso

1. **Archivo de Gramática:** El archivo `gramatica.txt` debe contener las reglas gramaticales en el siguiente formato:

    ```
    E -> E + T
    E -> T
    T -> T * F
    T -> F
    F -> ( E )
    F -> id
    ```

2. **Ejecutar el programa:** Asegúrate de que los archivos `arbol.py` y `gramatica.txt` estén en el mismo directorio. Luego, ejecuta el programa:

    ```bash
    python arbol.py
    ```

3. **Ingresar la cadena:** El programa te pedirá ingresar una cadena de entrada, que será evaluada según la gramática proporcionada.

4. **Ver el árbol gramatical:** Si la cadena es aceptada, el programa generará y mostrará el árbol gramatical en una ventana de `Matplotlib`.

## Archivos

- **`arbol.py`**: Código principal del programa.
- **`gramatica.txt`**: Archivo de texto con las reglas gramaticales que serán usadas por el programa.

