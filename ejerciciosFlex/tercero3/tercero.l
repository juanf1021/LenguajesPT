%{
#include <stdio.h>
%}

%%
[0-9]+(\.[0-9]+)?        { printf("Número: %s\n", yytext); }
\+                        { printf("Operador Suma: +\n"); }
\-                        { printf("Operador Resta: -\n"); }
\*                        { printf("Operador Multiplicación: *\n"); }
\/                        { printf("Operador División: /\n"); }
\^                        { printf("Operador Potencia: ^\n"); }
\%                        { printf("Operador Módulo: %%\n"); }
\=                        { printf("Símbolo Igual: =\n"); }
\(                        { printf("Paréntesis Izquierdo: (\n"); }
\)                        { printf("Paréntesis Derecho: )\n"); }
\[                        { printf("Corchete Izquierdo: [\n"); }
\]                        { printf("Corchete Derecho: ]\n"); }
\{                        { printf("Llave Izquierda: {\n"); }
\}                        { printf("Llave Derecha: }\n"); }
\<                        { printf("Menor Que: <\n"); }
\>                        { printf("Mayor Que: >\n"); }
\<=                       { printf("Menor o Igual Que: <=\n"); }
\>=                       { printf("Mayor o Igual Que: >=\n"); }
\!=                       { printf("Diferente: !=\n"); }
\|\|                      { printf("Operador OR: ||\n"); }
\&&                       { printf("Operador AND: &&\n"); }
\!                        { printf("Negación: !\n"); }
sin|cos|tan               { printf("Función Trigonométrica: %s\n", yytext); }
log|ln                    { printf("Función Logarítmica: %s\n", yytext); }
sqrt                      { printf("Función Raíz Cuadrada: sqrt\n"); }
[ \t\n]+                  { }
.                         { printf("Carácter no reconocido: %s\n", yytext); }
%%

int main(int argc, char **argv)
{
    yylex();
    return 0;
}
