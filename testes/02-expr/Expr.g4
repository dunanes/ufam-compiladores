grammar Expr;

root : expr EOF;

expr : expr (PLUS | SUB) expr 
     | NUM ;

NUM : [0-9]+;
PLUS : '+';
SUB : '-'; 
WS : [ \n]+ -> skip;