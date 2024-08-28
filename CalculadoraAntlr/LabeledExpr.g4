grammar LabeledExpr;

prog:   stat+ ;

stat:   expr NEWLINE # printExpr
    |   ID '=' expr NEWLINE # assign
    |   NEWLINE # blank
    ;

expr:   expr op=('*'|'/') expr # MulDiv
    |   expr op=('+'|'-') expr # AddSub
    |   INT # int
    |   FLOAT # float
    |   ID # id
    |   '(' expr ')' # parens
    ;

MUL : '*' ; 
DIV : '/' ; 
ADD : '+' ; 
SUB : '-' ; 
INT : [0-9]+ ; 
FLOAT : [0-9]+ '.' [0-9]* ; 
ID  : [a-zA-Z]+ ; 
NEWLINE:'\r'? '\n' ; 
WS  : [ \t]+ -> skip ; 
