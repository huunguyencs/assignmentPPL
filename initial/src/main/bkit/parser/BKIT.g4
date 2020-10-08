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

//Program 
program  : declare* EOF;

declare: vardeclare | funcdeclare;

//var declaration
vardeclare: VAR CL idlistinit SM;
idlistinit: idinit (CM idinit)*;
idinit: variable (EQ exp)*;

//function declaration
funcdeclare: FUNCTION CL ID (PARAMETER CL paralist)? body;

//paralist in function
paralist: variable (CM variable)*;

//body in function
body: BODY CL stmt* ENDBODY DOT;

//statement list
stmt: stmt_assign
    | stmt_break
    | stmt_call
    | stmt_con
    | stmt_do
    | stmt_for
    | stmt_if
    | stmt_ret
    | stmt_while
    | vardeclare;
//assignment statement
stmt_assign: variable EQ exp SM;
//if statement
stmt_if: IF exp THEN stmt (ELSEIF exp THEN stmt*)* (ELSE stmt*)? ENDIF DOT;
//for statement
stmt_for: FOR LP for_loop_con RP DO stmt* ENDFOR DOT;

for_loop_con: ID EQ exp CM exp CM exp;
//while statement
stmt_while: WHILE exp DO stmt* ENDWHILE DOT;
//do-while statement
stmt_do: DO stmt* WHILE exp ENDDO DOT;
//break statement
stmt_break: BREAK SM;
//continue statement
stmt_con: CONTINUE SM;
//call_statement
stmt_call: call SM;
//return statement:;
stmt_ret: RETURN exp;

//call function
call: ID LP paralist? RP;



ele_exp: exp index_op;
index_op: LR exp RR (index_op)*;
exp:;

variable: ID | ele_exp;


//KEYWORDS
BODY:       'Body';
BREAK:      'Break';
CONTINUE:   'Continue';
DO:         'Do';
ELSE:       'Else';
ELSEIF:     'ElseIf';
ENDBODY:    'EndBody';
ENDIF:      'EndIf';
ENDFOR:     'EndFor';
ENDWHILE:   'EndWhile';
FOR:        'For';
FUNCTION:   'Function';
IF:         'If';
PARAMETER:  'Parameter';
RETURN:     'Return';
THEN:       'Then';
VAR:        'Var';
WHILE:      'While';
TRUE:       'True';
FALSE:      'Fasle';
ENDDO:      'EndDo';

//OPERATORS
ASSIGN:         '=';
ADD:            '+';
ADDF:      '+.';
SUB:            '-';
SUBF:      '-.';
MUL:            '*';
MULF:      '*.';
DIV:            '\\';
DIVF:      '\\.';
MOD:            '%';
NOT:            '!';
AND:            '&&';
OR:             '||';
EQ:          '==';
NEQ:      '!='|'=/=';
LE:           '<';
GT:        '>';
LTE:     '<=';
GTE:  '>=';
LEF:     '<.';
GTF:  '>.';
LTEF:   '<=.';
GTEF:'>=.';

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

BOOLLIT: TRUE | FALSE;
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

