lexer grammar LTLLexer;

// Separator
LPAREN: '(';
RPAREN: ')';

// Operators
NEGATION: '!';
CONJUNCTION: '/\\';
DISJUNCTION: '\\/';
IMPLICATION: '->';
NEXT: 'X';
ALWAYS: 'G';
EVENTUALLY: 'F';
UNTIL: 'U';

// Keyword
TRUE: 'true';
FALSE: 'false';

// Identifier
IDENTIFIER: [a-z];

// Whitespace
WS: [ \t\r\n]+ -> skip;
