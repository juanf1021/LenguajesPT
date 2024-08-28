```markdown
## Andres Castro, Miguel Flechas, Juan Trujillo, Juan Hurtado

A continuación, se detallan los pasos necesarios para instalar ANTLR, configurar el entorno y ejecutar el programa.

### Instalación de ANTLR

#### Descargar ANTLR

Primero, necesitas descargar el archivo JAR de ANTLR. Puedes hacerlo usando curl o directamente desde el sitio web de ANTLR.
```

```bash
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

Alternativamente, descarga el archivo desde la página de descargas de ANTLR.

#### Configurar el Alias para ANTLR

Para facilitar el uso de ANTLR desde la línea de comandos, puedes configurar un alias en tu terminal. Esto te permitirá usar el comando `antlr4` en lugar de tener que especificar la ruta completa al archivo JAR.

Abre o crea el archivo `~/.bashrc` (o `~/.zshrc` si usas Zsh) y añade la siguiente línea:

```bash
alias antlr4='java -jar /ruta/al/archivo/antlr-4.13.2-complete.jar'
```

Asegúrate de reemplazar `/ruta/al/archivo` con la ruta donde has guardado el archivo `antlr-4.13.2-complete.jar`.

Después de añadir el alias, recarga tu archivo de configuración:

```bash
source ~/.bashrc  # O ~/.zshrc si usas Zsh
```

#### Verificar la Instalación

Para verificar que ANTLR está correctamente instalado y el alias funciona, ejecuta:

```bash
antlr4 -version
```

Deberías ver la versión de ANTLR.

### Configuración y Ejecución del Programa

#### Generar el Código de Análisis

Con el archivo de gramática `Expr.g4` o `LabeledExpr.g4`, utiliza ANTLR para generar el código Java necesario. Asegúrate de estar en el directorio donde se encuentra tu archivo `.g4`.

```bash
antlr4 -no-listener -visitor Expr.g4
```

Esto generará los archivos `ExprLexer.java`, `ExprParser.java`, `ExprBaseVisitor.java`, y otros archivos necesarios.

#### Compilar el Código

Compila el código generado y cualquier otro archivo Java que necesites. Asegúrate de incluir el archivo JAR de ANTLR en el classpath.

```bash
javac -cp .:/ruta/al/archivo/antlr-4.13.2-complete.jar *.java
```

Reemplaza `/ruta/al/archivo` con la ruta donde se encuentra `antlr-4.13.2-complete.jar`.

#### Ejecutar el Programa

Una vez compilado, puedes ejecutar el programa usando el siguiente comando:

```bash
java -cp .:/ruta/al/archivo/antlr-4.13.2-complete.jar NombreDeLaClase
```

Asegúrate de reemplazar `NombreDeLaClase` con el nombre de tu clase principal (por ejemplo, `Calc` o `ExprJoyRide`).

### Ejemplo

Para ejecutar un ejemplo simple de cálculo con el archivo `Calc.java`, asegúrate de haber generado y compilado los archivos Java necesarios.

Ejecuta el programa:

```bash
java -cp .:/ruta/al/archivo/antlr-4.13.2-complete.jar Calc
```

```bash
3 + 3
```

Y el resultado debería ser:

```
6
```
```
