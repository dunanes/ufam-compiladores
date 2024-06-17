grammar URL;

url: protocolo '://' dominio (':' porta)? caminho? query? fragmento?;

protocolo: 'http' | 'https' | 'ftp';

dominio: LETRA (LETRA | DIGITOS | '.' | '+' | '-')*;

porta: DIGITOS;

caminho: '/' (LETRA | DIGITOS | '.' | '-' | '_')+ ('/' (LETRA | DIGITOS | '.' | '-' | '_')+)*;

query: '?' parametro ('&' parametro)*;

parametro: chave '=' valor;

chave: (LETRA | DIGITOS | '.' | '-' | '_')+;

valor: (LETRA | DIGITOS | '.' | '-' | '_')+;

fragmento: '#' (LETRA | DIGITOS | '.' | '-' | '_')+;

LETRA: [a-zA-Z];
DIGITOS: [0-9]+;

WS: [ \t\r\n]+ -> skip;