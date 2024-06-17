grammar Html;

root: questao+;

questao: (qTexto | qRadioBox | qCheckBox | qMenu | qButton);

qTexto: 'TEXTO' NUMERO NUMERO str_;

qRadioBox: 'ESCOLHAUMA' str_ opcoes;

qCheckBox: 'ESCOLHAVARIAS' str_ opcoes;

qMenu: 'MENU' str_ opcoes;

qButton: 'BOTAO' str_ str_; // rótulo, ação (alerta)

opcoes: '(' str_ (',' str_)* ')';

str_: STRING;

// TOKENS:
NUMERO: [0-9]+;
STRING: '"' (~["])* '"';
IGNORE: [ \n\r\t] -> skip; 
COMMENT: '#' ~[\r\n]* -> skip;