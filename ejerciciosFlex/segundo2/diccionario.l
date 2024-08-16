%{
#include <stdio.h>
%}

%%
engineer      { printf("ingeniero "); }
engineers     { printf("ingenieros "); }
computer      { printf("computadora "); }
computers     { printf("computadoras "); }
algorithm     { printf("algoritmo "); }
algorithms    { printf("algoritmos "); }
circuit       { printf("circuito "); }
circuits      { printf("circuitos "); }
software      { printf("software "); }
hardware      { printf("hardware "); }
network       { printf("red "); }
networks      { printf("redes "); }
data          { printf("datos "); }
system        { printf("sistema "); }
systems       { printf("sistemas "); }
design        { printf("diseño "); }
designs       { printf("diseños "); }
and           { printf("y "); }
or            { printf("o "); }
if            { printf("si "); }
else          { printf("sino "); }
while         { printf("mientras "); }
for           { printf("para "); }
function      { printf("función "); }
variable      { printf("variable "); }
variables     { printf("variables "); }
input         { printf("entrada "); }
output        { printf("salida "); }
process       { printf("proceso "); }
processes     { printf("procesos "); }
flowchart     { printf("diagrama de flujo "); }

[ \t\n]+     {  }
.            { printf("%s ", yytext); } 
%%

int main(int argc, char **argv)
{
    yylex();
    return 0;
}
