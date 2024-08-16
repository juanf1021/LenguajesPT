%{
#include <stdio.h>
%}

%%


[+-]?[0-9]+(\.[0-9]+)?i            { printf("Número imaginario: %s\n", yytext); }
[+-]?[0-9]+(\.[0-9]+)?              { printf("Número real: %s\n", yytext); }
[+-]?[0-9]+(\.[0-9]+)?[+-][0-9]+(\.[0-9]+)?i { printf("Número complejo: %s\n", yytext); }
[+-]?[0-9]+(\.[0-9]+)?[+-][0-9]+(\.[0-9]+)?  { printf("Número complejo: %s\n", yytext); }
[ ]+                                ; 
\n                                  ; 
.                                   { printf("Entrada no válida: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    yylex();
    return 0;
}
