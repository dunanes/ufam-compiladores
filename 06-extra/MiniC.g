grammar MiniC;
program: definition (definition)* EOF;

INT: 'int';
CHAR: 'char';
TIPO: (INT|CHAR);
IF: 'if';
WHILE: 'while';
ELSE: 'else';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';

definition: data_definition | function_definition;
data_definition: ('int' | 'char') declarator  (',' declarator )* ';'; 

declarator: Identifier;

Identifier: [a-zA-Z_]+[a-zA-Z0-9_]*; // identificadores das variáveis 

function_definition : ('int' | 'char') function_header function_body;
function_header : declarator parameter_list;
parameter_list: '(' (parameter_declaration)?  ')' ;
parameter_declaration : ('int' | 'char') declarator ( ',' ('int' | 'char') declarator )* ;

function_body: '{' (data_definition)* (statement)* '}';

block
 : '{' (statement)+ '}'
 ;

statement
: expression ';'  
| IF '(' expression ')'   statement  ( ELSE statement )? 
| WHILE '(' expression ')'  statement
| BREAK ';' 
| CONTINUE ';' 
| RETURN (expression)? ';' 
| block
| ';'
;

expression : binary ( ',' binary )* ;


binary
: Identifier '=' binary  
| Identifier '+=' binary
| Identifier '-=' binary
| Identifier '*=' binary 
| Identifier '/=' binary 
| Identifier '%=' binary 
| binary '==' binary     
| binary '!=' binary     
| binary '<=' binary     
| binary '>=' binary     
| binary '>' binary      
| binary '<' binary      
| binary '+' binary      
| binary '-' binary      
| binary '*' binary      
| binary '/' binary      
| binary '%' binary      
| unary                  
;


unary
: '++'Identifier
| '--'Identifier
| primary
;

primary
: Identifier 
| CONSTANT_INT
| CONSTANT_CHAR
| '(' expression ')'
| Identifier '('  (argument_list)?  ')' ; 

argument_list: binary (',' binary )* ;

CONSTANT_INT : [0-9]+;
CONSTANT_CHAR : '\'' . '\'' ;

COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;