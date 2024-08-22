%{
#include "calculadora.tab.h"
%}

%%
[0-9]+    { yylval = atoi(yytext); return NUMBER; }
"+"       { return ADD; }
"-"       { return SUB; }
"*"       { return MUL; }
"/"       { return DIV; }
"|"       { return ABS; }
\n        { return EOL; }
[ \t]     ; // Ignorar espacios y tabulaciones
.         { printf("Mystery character %c\n", *yytext); }
%%

