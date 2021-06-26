grammar Sakura;


// Keywords
VAR : 'var';
CONST : 'const';
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


// parsers
block
    :
    (PASS SEMI_COLON
    | Comment SEMI_COLON
    | decvar SEMI_COLON
    | defvar SEMI_COLON
    | assvar SEMI_COLON
    | decfunc SEMI_COLON
    | funcReturn SEMI_COLON
    | defunc
    | callfunc SEMI_COLON
    )*;

// expression
literalValue
    : (Interger|Identifier|String|Decimal);
expr
    : literalValue
    | callfunc
    | expr POWER expr
    | expr (STAR|DIV) expr
    | expr (ADD|MINUS) expr;

// variable
decvar
    : VAR Identifier;
defvar
    : CONST? VAR Identifier ASSIGN expr;
assvar
    : Identifier ASSIGN expr;

// function
funcArgs
    : (((decvar|defvar) COMMA)* (decvar|defvar))?;
funcHead
    : FUNC Identifier OPEN_PAREN funcArgs CLOSE_PAREN (ARROW Identifier)?;
decfunc
    : funcHead;
funcReturn
    : RETURN expr;
defunc
    : funcHead OPEN_BRACE block CLOSE_BRACE;
callfunc
    : Identifier OPEN_PAREN ((expr COMMA)* expr)? CLOSE_PAREN;
