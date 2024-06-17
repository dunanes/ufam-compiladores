grammar miniC;

program
    : definition+;

definition
    : data_definition
    | function_definition;

data_definition
    : 'int' declarator (',' declarator)* ';';

declarator
    : Identifier;

function_definition
    : type function_header function_body;

type
    : 'int'
    | 'float'
    | 'char'
    | 'void';

function_header
    : declarator parameter_list;

parameter_list
    : '(' parameter_declaration? ')';

parameter_declaration
    : type declarator (',' type declarator)*;

function_body
    : '{' data_definition* statement* '}';

statement
    : expression? ';'
    | 'if' '(' expression ')' statement ('else' statement)?
    | 'while' '(' expression ')' statement
    | 'for' '(' expression? ';' expression? ';' expression? ')' statement
    | 'break' ';'
    | 'continue' ';'
    | 'return' expression? ';'
    | block;

block
    : '{' statement* '}';

expression
    : binary (',' binary)*;

binary
    : Identifier '=' binary
    | Identifier '+=' binary
    | Identifier '-=' binary
    | Identifier '*=' binary
    | Identifier '/=' binary
    | Identifier '%=' binary
    | binary '==' binary
    | binary '!=' binary
    | binary '<' binary
    | binary '<=' binary
    | binary '>' binary
    | binary '>=' binary
    | binary '+' binary
    | binary '-' binary
    | binary '*' binary
    | binary '/' binary
    | binary '%' binary
    | unary;

unary
    : '++' Identifier
    | '--' Identifier
    | Identifier '++'
    | Identifier '--'
    | primary;

primary
    : Identifier
    | CONSTANT_INT
    | '(' expression ')'
    | Identifier '(' argument_list? ')';

argument_list
    : binary (',' binary)*;

Identifier
    : [a-zA-Z_][a-zA-Z0-9_]*;

CONSTANT_INT
    : [0-9]+;

WS
    : [ \t\r\n]+ -> skip;
