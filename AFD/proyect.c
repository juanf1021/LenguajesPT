#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Juan Hurtado, Miguel Flechas, Andres Castro

#define MAX_ESTADOS 100          // Máximo número de estados que el AFD puede manejar
#define MAX_ALFABETO 26          // Máximo número de símbolos en el alfabeto
#define MAX_TRANSICIONES 1000    // Máximo número de transiciones que el AFD puede manejar

// Estructura para representar un Autómata Finito Determinista (AFD)
typedef struct {
    char *estados[MAX_ESTADOS];                   // Lista de nombres de los estados del AFD
    char alfabeto[MAX_ALFABETO];                  // Alfabeto del AFD
    char *estado_inicial;                         // Estado inicial del AFD
    char *estados_aceptacion[MAX_ESTADOS];        // Lista de estados de aceptación
    int num_estados;                              // Número de estados en el AFD
    int num_alfabeto;                             // Número de símbolos en el alfabeto
    int num_estados_aceptacion;                   // Número de estados de aceptación
} AFD;

// Estructura para representar una transición en el AFD
typedef struct {
    char *estado_actual;     // Estado actual antes de la transición
    char simbolo;            // Símbolo que desencadena la transición
    char *estado_siguiente;  // Estado siguiente después de la transición
} Transicion;

// Arreglo global de transiciones y un contador de transiciones
Transicion transiciones[MAX_TRANSICIONES];
int num_transiciones = 0;  // Número de transiciones registradas

/**
 * Función para leer la configuración del AFD desde un archivo.
 * @param nombre_archivo Nombre del archivo que contiene la configuración.
 * @param afd Puntero a la estructura AFD que será llenada con los datos leídos.
 */
void leer_configuracion(const char *nombre_archivo, AFD *afd) {
    // Abre el archivo para lectura
    FILE *archivo = fopen(nombre_archivo, "r");
    if (!archivo) {
        perror("Error al abrir el archivo");
        exit(EXIT_FAILURE);
    }

    char linea[256];
    char *token;
    
    // Leer estados del AFD desde el archivo
    fgets(linea, sizeof(linea), archivo);
    token = strtok(linea, ",\n");
    while (token) {
        afd->estados[afd->num_estados++] = strdup(token);  // Guardar el estado en la lista de estados
        token = strtok(NULL, ",\n");
    }

    // Leer el alfabeto del AFD desde el archivo
    fgets(linea, sizeof(linea), archivo);
    token = strtok(linea, ",\n");
    while (token) {
        afd->alfabeto[afd->num_alfabeto++] = token[0];  // Guardar el símbolo en el alfabeto
        token = strtok(NULL, ",\n");
    }

    // Leer el estado inicial del AFD desde el archivo
    fgets(linea, sizeof(linea), archivo);
    afd->estado_inicial = strdup(strtok(linea, "\n"));  // Guardar el estado inicial

    // Leer los estados de aceptación del AFD desde el archivo
    fgets(linea, sizeof(linea), archivo);
    token = strtok(linea, ",\n");
    while (token) {
        afd->estados_aceptacion[afd->num_estados_aceptacion++] = strdup(token);  // Guardar cada estado de aceptación
        token = strtok(NULL, ",\n");
    }

    // Leer las transiciones del AFD desde el archivo
    while (fgets(linea, sizeof(linea), archivo)) {
        token = strtok(linea, ",\n");
        transiciones[num_transiciones].estado_actual = strdup(token);  // Estado actual de la transición
        token = strtok(NULL, ",\n");
        transiciones[num_transiciones].simbolo = token[0];  // Símbolo que desencadena la transición
        token = strtok(NULL, ",\n");
        transiciones[num_transiciones].estado_siguiente = strdup(token);  // Estado siguiente de la transición
        num_transiciones++;  // Incrementa el contador de transiciones
    }

    fclose(archivo);  // Cierra el archivo
}

/**
 * Función que busca la transición válida desde un estado actual con un símbolo dado.
 * @param afd Puntero a la estructura AFD.
 * @param estado_actual El estado actual desde el que se busca la transición.
 * @param simbolo El símbolo que desencadena la transición.
 * @return El estado siguiente si la transición es válida, NULL si no hay transición válida.
 */
char* transicion(AFD *afd, char *estado_actual, char simbolo) {
    for (int i = 0; i < num_transiciones; i++) {
        // Comprueba si la transición es válida
        if (strcmp(transiciones[i].estado_actual, estado_actual) == 0 && transiciones[i].simbolo == simbolo) {
            return transiciones[i].estado_siguiente;  // Retorna el estado siguiente
        }
    }
    return NULL; // No se encontró transición válida
}

/**
 * Función para procesar una cadena de entrada y determinar si es aceptada por el AFD.
 * @param afd Puntero a la estructura AFD.
 * @param entrada Cadena de entrada que será procesada.
 * @return 1 si la cadena es aceptada, 0 si es rechazada.
 */
int procesar_entrada(AFD *afd, const char *entrada) {
    char *estado_actual = afd->estado_inicial;  // Comienza en el estado inicial
    for (int i = 0; entrada[i] != '\0'; i++) {
        // Aplica la transición para el símbolo actual
        estado_actual = transicion(afd, estado_actual, entrada[i]);
        if (!estado_actual) {
            return 0; // Cadena rechazada si no hay transición válida
        }
    }

    // Verifica si el estado final es un estado de aceptación
    for (int i = 0; i < afd->num_estados_aceptacion; i++) {
        if (strcmp(estado_actual, afd->estados_aceptacion[i]) == 0) {
            return 1; // Cadena aceptada
        }
    }

    return 0; // Cadena rechazada si no se llega a un estado de aceptación
}

/**
 * Función principal del programa.
 * Pide al usuario el nombre del archivo de configuración y la cadena de entrada, y luego procesa la entrada.
 */
int main() {
    char nombre_archivo_configuracion[256];
    char cadena_entrada[256];
    AFD afd = {0};  // Inicializa la estructura del AFD

    // Solicita al usuario el nombre del archivo de configuración
    printf("Ingrese el nombre del archivo de configuración: ");
    scanf("%s", nombre_archivo_configuracion);

    // Lee la configuración del archivo
    leer_configuracion(nombre_archivo_configuracion, &afd);

    // Solicita al usuario la cadena de entrada a procesar
    printf("Ingrese la cadena de entrada: ");
    scanf("%s", cadena_entrada);

    // Procesa la cadena de entrada y muestra si fue aceptada o rechazada
    if (procesar_entrada(&afd, cadena_entrada)) {
        printf("Resultado: La cadena fue aceptada.\n");
    } else {
        printf("Resultado: La cadena fue rechazada.\n");
    }

    // Liberar memoria alocada dinámicamente
    for (int i = 0; i < afd.num_estados; i++) free(afd.estados[i]);
    for (int i = 0; i < afd.num_estados_aceptacion; i++) free(afd.estados_aceptacion[i]);
    for (int i = 0; i < num_transiciones; i++) {
        free(transiciones[i].estado_actual);
        free(transiciones[i].estado_siguiente);
    }

    return 0;
}
