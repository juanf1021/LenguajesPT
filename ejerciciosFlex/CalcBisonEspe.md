####Andres Castro, Miguel Flechas, Juan Hurtado, Juan Trujillo
Este programa implementa una calculadora simple utilizando herramientas de generación de analizadores léxicos y sintácticos: **Flex** y **Bison**. La calculadora permite realizar operaciones básicas como suma, resta, multiplicación, división y cálculo del valor absoluto sobre números enteros. Además, el programa maneja errores como la división por cero.

#### Archivos del Proyecto
1. **lex.l**: Contiene las reglas léxicas que definen los tokens reconocidos por el analizador léxico. Estos tokens incluyen números, operadores matemáticos y el fin de línea.
2. **calculadora.y**: Define las reglas gramaticales para analizar expresiones matemáticas y generar el código correspondiente. Aquí se manejan las operaciones aritméticas y se controla el flujo del programa.
3. **calculadora.tab.h**: Archivo de encabezado generado por Bison que declara los tokens y el tipo de valor utilizado por el parser.
4. **calculadora.tab.c**: Código fuente generado por Bison a partir del archivo `calculadora.y`. Contiene la implementación del parser.
5. **lex.yy.c**: Código fuente generado por Flex a partir del archivo `lex.l`. Contiene la implementación del analizador léxico.

#### Compilación y Ejecución en Kali Linux
Para compilar y ejecutar este programa en Kali Linux, sigue los siguientes pasos:

1. **Instalación de Bison y Flex**:
   Asegúrate de tener Bison y Flex instalados en tu sistema. Si no están instalados, puedes hacerlo ejecutando:
   ```
   sudo apt-get update
   sudo apt-get install bison flex
   ```

2. **Generación de los Archivos de Código**:
   Primero, usa Flex para generar el código C del analizador léxico y Bison para el parser:
   ```
   flex lex.l
   bison -d calculadora.y
   ```
   Esto generará dos archivos: `lex.yy.c` para el analizador léxico y `calculadora.tab.c` junto con `calculadora.tab.h` para el parser.

3. **Compilación del Programa**:
   Compila los archivos generados junto con cualquier otro archivo adicional que utilices (como la librería estándar de C):
   ```
   gcc lex.yy.c calculadora.tab.c -o calculadora
   ```

4. **Ejecución del Programa**:
   Ejecuta la calculadora desde la terminal:
   ```
   ./calculadora
   ```
   La calculadora estará lista para recibir expresiones matemáticas. Escribe la operación que deseas realizar y presiona `Enter`. La calculadora te devolverá el resultado de la operación.

#### Ejemplo de Uso
```plaintext
> 3 + 4
= 7
> 10 * 5
= 50
> 10 / 0
error: division by zero
```

#### Notas Adicionales
- **Operadores Reconocidos**:
  - `+`: Suma
  - `-`: Resta
  - `*`: Multiplicación
  - `/`: División
  - `|`: Valor absoluto
- **Errores**:
  - El programa maneja la división por cero y cualquier carácter desconocido como errores.
