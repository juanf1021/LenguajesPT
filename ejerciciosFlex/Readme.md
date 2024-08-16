#Trabajo de Juan Hurtado, Andres Castro, Miguel Flechas, Juan Trujillo

# Programas en LEX

Este repositorio contiene cinco programas escritos en LEX, implementados y probados en Kali Linux. Los programas son:

1. **Contar líneas, palabras y caracteres**: Cuenta el número de líneas, palabras y caracteres en un archivo de texto.
2. **Traductor de inglés a español**: Traduce palabras clave del inglés al español.
3. **Reconocimiento de símbolos y caracteres de la calculadora**: Reconoce números, símbolos y caracteres utilizados en una calculadora.
4. **Reconocimiento de tokens**: Reconoce tokens específicos como `NUMBER`, `ADD`, `SUB`, `MUL`, `DIV`, `ABS` y `EOL`.
5. **Clasificación de números complejos**: Clasifica números como reales, imaginarios o complejos.

## Requisitos Previos

Para ejecutar estos programas, necesitas tener LEX instalado en tu sistema. Aquí te mostramos cómo instalarlo y utilizarlo en Kali Linux.

### Instalación de LEX en Kali Linux

Si aún no tienes LEX instalado, puedes hacerlo con el siguiente comando:

```bash
sudo apt-get install flex
```

### Compilación y Ejecución de un Archivo LEX

Para compilar y ejecutar un archivo LEX, sigue estos pasos:

1. **Compila el archivo LEX**:  
   Supongamos que tienes un archivo llamado `programa1.l`, compílalo con:

   ```bash
   lex programa1.l
   ```

2. **Compila el código generado**:  
   Flex generará un archivo `lex.yy.c`. Compílalo con:

   ```bash
   gcc lex.yy.c -lfl
   ```

   Esto generará un archivo ejecutable llamado `a.out`.

3. **Ejecuta el programa**:  
   Para ejecutar el programa, asegúrate de estar en la carpeta donde se encuentra `a.out` y utiliza el siguiente comando:

   ```bash
   ./a.out
   ```

### Ejecución de los Programas

A continuación, se muestra cómo ejecutar cada uno de los programas mencionados:

1. **Programa 1: Contar líneas, palabras y caracteres**:

   ```bash
   ./a.out
   ```

2. **Programa 2: Traductor de inglés a español**:

   ```bash
   ./a.out
   ```

3. **Programa 3: Reconocimiento de símbolos y caracteres de la calculadora**:

   ```bash
   ./a.out
   ```

4. **Programa 4: Reconocimiento de tokens**:

   ```bash
   ./a.out
   ```

5. **Programa 5: Clasificación de números complejos**:

   ```bash
   ./a.out
   ```
