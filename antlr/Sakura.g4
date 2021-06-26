grammar Sakura;


// Keywords
VAR : 'var';
FUNC : 'func';
PASS : 'pass';
RETURN : 'return';

// Symbols
DOT : '.';
STAR : '*';
OPEN_PAREN : '(' {openBrace();};
CLOSE_PAREN : ')' {closeBrace();};
COMMA : ',';
COLON : ':';
SEMI_COLON : ';';
POWER : '**';
ASSIGN : '=';
OPEN_BRACK : '[' {openBrace();};
CLOSE_BRACK : ']' {closeBrace();};
ADD : '+';
MINUS : '-';
DIV : '/';
MOD : '%';
OPEN_BRACE : '{' {openBrace();};
CLOSE_BRACE : '}' {closeBrace();};
LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ : '!=';
AT : '@';
ARROW : '->';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MULT_ASSIGN : '*=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';


// Others
Comment
    : '#' ~[\r\n]* '\r'? '\n' -> channel(HIDDEN) ;
WS
    : [ \r\t\n]+ -> channel(HIDDEN) ;
Newline
    : '\r'? '\n';

// Numbers
fragment Digit
    : [0-9];
fragment NonZeroDigit
    : [1-9];
Interger
    : (MINUS? NonZeroDigit Digit*|'0');
Decimal
    : Interger DOT Digit+;

// Characters
fragment Char
    : [a-zA-Z];
Identifier
    : (Char|'_') (Digit|Char|'_')*;
String
    : '"' ~["\\\r\n]+? '"';


// Parsers
block
    : (PASS SEMI_COLON|Comment|decvar|defvar|assvar|decfunc|funcReturn|defunc|callfunc)*;

literalValue
    : (Interger|Identifier|String|Decimal);

// variable
decvar
    : VAR Identifier SEMI_COLON;
defvar
    : VAR Identifier ASSIGN literalValue SEMI_COLON;
assvar
    : Identifier ASSIGN literalValue SEMI_COLON;

// function
funcArgs
    :
    (((VAR Identifier|VAR Identifier ASSIGN literalValue) COMMA)*
    (VAR Identifier|VAR Identifier ASSIGN literalValue)| );
funcHead
    : FUNC Identifier OPEN_PAREN funcArgs CLOSE_PAREN (ARROW Identifier)?;
decfunc
    : funcHead SEMI_COLON;
funcReturn
    : RETURN literalValue SEMI_COLON;
defunc
    : funcHead OPEN_BRACE block CLOSE_BRACE;
callfunc
    : Identifier OPEN_PAREN ((literalValue COMMA)* literalValue| ) CLOSE_PAREN SEMI_COLON;