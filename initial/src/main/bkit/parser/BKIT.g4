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
ASSIGN:         '=';
ADD:            '+';
ADD_FLOAT:      '+.';
SUB:            '-';
SUB_FLOAT:      '-.';
MUL:            '*';
MUL_FLOAT:      '*.';
DIV:            '\\';
DIV_FLOAT:      '\\.';
MOD:            '%';
NOT:            '!';
AND:            '&&';
OR:             '||';
EQUAL:          '==';
NOT_EQUAL:      '!='|'=/=';
LESS:           '<';
GREATER:        '>';
LESS_EQUAL:     '<=';
GREATER_EQUAL:  '>=';
LESS_FLOAT:     '<.';
GREATER_FLOAT:  '>.';
LESS_EQUAL_FLOAT:   '<=.';
GREATER_EQUAL_FLOAT:'>=.';

//SEPARATORS
LP:     '(';
RP:     ')';
LR:     '[';
RR:     ']';
CL:     ':';
DOT:    '.';
CM:     ',';
SM:     ';';
LB:     '{';
RB:     '}';

//LITERALS

INTLIT:
    DECIMALDIGIT
    | ('0o'|'0O') [1-7] OCTALDIGIT*
    | ('0x'|'0X') [1-9a-fA-F] HEXADECIMALDIGIT*
    ;
FLOATLIT:
    DECIMALDIGIT '.'? EXPONENT
    | DECIMALDIGIT '.' DIGIT+
    | DECIMALDIGIT '.' DIGIT* EXPONENT
    ;

BOOLLIT: TRUE_ | FALSE_;
STRINGLIT: '"' SCHAR* '"';


ID: [a-z][0-9a-zA-Z_]*;


//FRAGMENT
fragment NONDIGIT: [a-zA-Z_];
fragment DIGIT: [0-9];
fragment NONZERODIGIT: [1-9];

fragment DECIMALDIGIT: '0'| (NONZERODIGIT DIGIT*);
fragment OCTALDIGIT: [0-7];
fragment HEXADECIMALDIGIT: [0-9a-fA-F];
fragment BINARYDIGIT: [01];

fragment SIGN: [+-];
fragment EXPONENT: [eE] SIGN? DIGIT+;

fragment ESC_SEQ: '\\' [btnfr'\\];
fragment SCHAR: 
    ~ ['"\\\r\n]
    | ESC_SEQ
    | '\'"'
    ;

//SKIP
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
COMMENT: '**' .*? '**' -> skip;

//ERROR
UNCLOSE_STRING: '"' SCHAR* ( [\r\n] | EOF);
ERROR_CHAR: .;
ILLEGAL_ESCAPE:  '"' SCHAR* (('\\' ~[btnfr'\\]) | ('\'' ~'"'));
UNTERMINATED_COMMENT: '**' (.*? | EOF) ;

