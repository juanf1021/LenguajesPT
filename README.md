# LenguajesPT
Trabajo de : Juan Hurtado, Miguel Flechas, Andres Castro

AFD (Autómata Finito Determinista) en C
Este proyecto implementa un Autómata Finito Determinista (AFD) en lenguaje C. El programa es capaz de leer la configuración de un AFD desde un archivo de texto y procesar cadenas de entrada para determinar si son aceptadas o rechazadas por el autómata.

Contenido del Proyecto
proyect.c: Archivo principal que contiene la implementación del AFD.
config.txt: Archivo de configuración de ejemplo para probar el programa.
Requisitos
Compilador de C (por ejemplo, GCC).
Instrucciones de Uso
Paso 1: Compilación
Primero, debes compilar el programa. Si estás en un entorno Unix/Linux o en una terminal compatible con GCC, puedes hacerlo con el siguiente comando:

```txt
gcc -o proyect proyect.c
```
Este comando generará un ejecutable llamado proyect.

Paso 2: Ejecutar el Programa
Una vez compilado, puedes ejecutar el programa desde la terminal con el siguiente comando:
```txt
./proyect
```
Paso 3: Probar con un Archivo de Configuración
Cuando ejecutes el programa, se te pedirá que ingreses el nombre del archivo de configuración. Para probar el programa con el archivo de configuración incluido en este repositorio, ingresa el siguiente nombre cuando se te solicite:

Ingrese el nombre del archivo de configuración: config.txt
Paso 4: Ingresar una Cadena de Entrada
Luego, se te pedirá que ingreses la cadena de entrada que deseas procesar con el AFD. Por ejemplo, podrías ingresar:


Ingrese la cadena de entrada: abba  (rechazada en ejemplo inicial)
Ingrese la cadena de entrada: ab (aceptada en el ejemplo)
El programa procesará la cadena de entrada y te dirá si fue aceptada o rechazada por el AFD.

Formato del Archivo de Configuración
El archivo de configuración debe seguir un formato específico:

Lista de estados: Una línea con los nombres de los estados separados por comas.
Alfabeto: Una línea con los símbolos del alfabeto separados por comas.
Estado inicial: Una línea con el nombre del estado inicial.
Estados de aceptación: Una línea con los nombres de los estados de aceptación separados por comas.
Transiciones: Cada línea subsiguiente representa una transición en el formato estado_actual,símbolo,estado_siguiente.
Ejemplo del contenido de config.txt:

```txt
q0,q1,q2
a,b
q0
q2
q0,a,q1
q1,b,q2
q2,a,q1
q2,b,q0
