%{
#include "calculadora.tab.h"
%}

%%

-[0-9]+(\.[0-9]+)?  { yylval.dval = atof(yytext); return NUMBER; }
"+"                { return ADD; }
"-"                { return SUB; }
"*"                { return MUL; }
"/"                { return DIV; }
"|"              { return ABS; }
\n                 { return EOL; }
[ \t]              ; /* Ignore whitespace */

%%

int yywrap() {
    return 1;
}

