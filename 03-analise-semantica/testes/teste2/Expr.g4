grammar Expr;
root : expr EOF;
expr : expr DIV expr # Div
| expr MUL expr # Mul
| expr PLUS expr # Sum
| expr SUB expr # Sub
| NUM # Value
;

NUM : [0-9]+;
DIV : '/';
MUL : '*';
PLUS : '+';
SUB : '-';
WS : [ \n]+ -> skip;