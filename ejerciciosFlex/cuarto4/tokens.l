%{
#include <stdio.h>
%}

%option noyywrap


NUMBER      [0-9]+
ADD         \+
SUB         \-
MUL         \*
DIV         \/
ABS         (abs|\|)
EOL         \n

%%

{NUMBER}    { printf("NUMBER: %s\n", yytext); }
{ADD}       { printf("ADD: %s\n", yytext); }
{SUB}       { printf("SUB: %s\n", yytext); }
{MUL}       { printf("MUL: %s\n", yytext); }
{DIV}       { printf("DIV: %s\n", yytext); }
{ABS}       { printf("ABS: %s\n", yytext); }
{EOL}       { printf("EOL\n"); }
.           { printf("Token no reconocido: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}
