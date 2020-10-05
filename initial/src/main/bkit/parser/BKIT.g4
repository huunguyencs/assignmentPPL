grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : . ;

//KEYWORDS
BODY:       'Body';
BREAK:      'Break';
CONTINUE:   'Continue';
DO:         'Do';
ELSE:       'Else';
ELSE_IF:    'ElseIf';
END_BODY:   'EndBody';
END_IF:     'EndIf';
END_FOR:    'EndFor';
END_WHILE:  'EndWhile';
FOR:        'For';
FUNCTION:   'Function';
IF:         'If';
PARAMETER:  'Parameter';
RETURN:     'Return';
THEN:       'Then';
VAR:        'Var';
WHILE:      'While';
TRUE_:      'True';
FALSE_:     'Fasle';
END_DO:     'EndDo';

//OPERATORS
ASSIGN:     '=';
PLUS:       '+';
PLUS_FLOAT: '+.';
SUB:        '-';
SUB_FLOAT:  '-.';
MUL:        '*';
MUL_FLOAT:  '*.';
DIV:        '\\';
DIV_FLOAT:  '\\.';
MOD:        '%';
NOT:        '!';
AND:        '&&';
OR:         '||';
EQUAL:      '==';
NOT_EQUAl:  '!='|'=/=';
LESS:       '<';
GREATER:    '>';
LESS_EQUAL: '<=';
GREATER_EQUAL:  '>=';
LESS_FLOAT: '<.';
GREATER_FLOAT:  '>.';
LESS_EQUAL_FLOAT:   '<=.';
GREATER_EQUAL_FLOAT:'>=.';

//SEPARATORS
LEFTPAREN:      '(';
RIGHTPAREN:     ')';
LEFTBRACKET:    '[';
RIGHTBRACKET:   ']';
COLON:          ':';
DOT:            '.';
COMMA:          ',';
SEMI:           ';';
LEFTBRACE:      '{';
RIGHTBRACE:     '}';

//LITERALS
LITERAL:
    INTEGER_LITERAL
    | FLOATING_LITERAL
    | BOOLEAN_LITERAL
    | STRING_LITERAL
    ;

INTEGER_LITERAL:
    DECIMALDIGIT
    | ('0o'|'0O') [1-7] OCTALDIGIT*
    | ('0x'|'0X') [1-9a-fA-F] HEXADECIMALDIGIT*
    ;
FLOATING_LITERAL:
    DECIMALDIGIT '.'? (EXPONENT_FLOAT | DIGIT* )?
    | DECIMALDIGIT '.' DIGIT* EXPONENT_FLOAT
    ;

BOOLEAN_LITERAL: TRUE_ | FALSE_;
STRING_LITERAL: UNTERMINAL_STRING '"';




IDENTIFIERS: [a-z] [0-9a-zA-Z_]*;


//FRAGMENT
fragment NONDIGIT: [a-zA-Z_];
fragment DIGIT: [0-9];
fragment NONZERODIGIT: [1-9];

fragment DECIMALDIGIT: '0'| (NONZERODIGIT DIGIT*);
fragment OCTALDIGIT: [0-7];
fragment HEXADECIMALDIGIT: [0-9a-fA-F];
fragment BINARYDIGIT: [01];

fragment SIGN: [+-];
fragment EXPONENT_FLOAT: [eE] SIGN? DIGIT+;

fragment SIMPLE_ESCAPE_SEQUENCE: 
    '\\b' 
    | '\\f' 
    | '\\r' 
    | '\\n' 
    | '\\t' 
    | '\\\'' 
    | '\\\\'
    ;
fragment SCHAR: 
    ~ ["\\\r\n]
    | SIMPLE_ESCAPE_SEQUENCE
    ;
fragment UNTERMINAL_STRING: '"' (SCHAR | DOUBLE_QUOTE_IN_STRING)*;
fragment DOUBLE_QUOTE_IN_STRING: '\'"' SCHAR* '\'"';



//SKIP
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
COMMENT: '**' .*? '**' -> skip;

//ERROR
UNCLOSE_STRING: UNTERMINAL_STRING;
ERROR_CHAR: .;
ILLEGAL_ESCAPE: UNTERMINAL_STRING (SIMPLE_ESCAPE_SEQUENCE| EOF);
UNTERMINATED_COMMENT: '**' (.*? | EOF );
