grammar QLANG;


// Keywords
CONST : 'const';
PASS : 'pass';
RETURN : 'return';
IF : 'if';
ELIF : 'elif';
ELSE : 'else';
ENUMERATE : 'enumerate';
CASE : 'case';
DEFAULT : 'default';
AND : 'and';
OR : 'or';
AUTO : 'auto';
WHILE : 'while';
CLASS : 'class';
NS : 'namespace';
NEW : 'new';

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
    : NonZeroDigit Digit*|'0';
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
    :((statement SEMI_COLON|smallBlock)*|PASS SEMI_COLON);

statement
    : declareVariable
    | defineVariable
    | assignVariable
    | functionReturn
    | functionCall;

smallBlock
    :
    ( defineFunction
    | defineDecorator
    | fullIf
    | fullEnumerate
    | whileLoop
    );

// expression
literalValue
    : (Interger|Identifier|String|Decimal);
expression
    : literalValue
    | functionCall
    | expression POWER expression
    | expression (STAR|DIV|MOD) expression
    | expression (ADD|MINUS) expression
    | expression (EQUALS|NOT_EQ|GREATER_THAN|LESS_THAN) expression
    | expression AND expression
    | expression OR expression;

// variable
declareVariable
    : (callDecorator|CONST)? Identifier AT (Identifier|AUTO);
defineVariable
    : declareVariable ASSIGN expression;
assignVariable
    : Identifier ASSIGN expression;

// function
functionArgument
    : declareVariable|defineVariable;
functionHead
    : Identifier OPEN_PAREN ((functionArgument COMMA)* functionArgument)? CLOSE_PAREN (ARROW Identifier)?;
functionReturn
    : RETURN expression;
defineFunction
    : functionHead OPEN_BRACE block CLOSE_BRACE;
functionCall
    : Identifier OPEN_PAREN ((expression COMMA)* expression (COMMA assignVariable)*?)? CLOSE_PAREN;

// if
ifCondition
    : IF expression OPEN_BRACE block CLOSE_BRACE;
elifCondition
    : ELIF expression OPEN_BRACE block CLOSE_BRACE;
elseCondition
    : ELSE OPEN_BRACE block CLOSE_BRACE;
fullIf
    : ifCondition elifCondition* elseCondition?;

// enumerate
fullEnumerate
    : ENUMERATE expression OPEN_BRACE caseCondition+ defaultCondition CLOSE_BRACE;
caseCondition
    : CASE expression OPEN_BRACE block CLOSE_BRACE;
defaultCondition
    : DEFAULT OPEN_BRACE block CLOSE_BRACE;

// while
whileLoop
    : WHILE expression OPEN_BRACE block CLOSE_BRACE;

// decorator
defineDecorator
    : AT Identifier OPEN_PAREN ((functionArgument COMMA)* functionArgument)? CLOSE_PAREN OPEN_BRACE block CLOSE_BRACE;
callDecorator
    : AT Identifier (OPEN_PAREN ((functionArgument COMMA)* functionArgument)? CLOSE_PAREN)?;