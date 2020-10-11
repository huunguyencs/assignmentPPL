grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        errorStr = result.text
        if errorStr[0] == '"':
            result.text = errorStr[1:]       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        errorStr = result.text
        if errorStr[0] == '"':
            result.text = errorStr[1:]
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
program  : declare+ EOF;

declare
    : vardeclare 
    | funcdeclare
    ;

//var declaration
vardeclare: VAR CL idlistinit SM;
idlistinit: idinit (CM idinit)*;
idinit: variable (AS exp)*;

//function declaration
funcdeclare: FUNCTION CL ID (PARAMETER CL paralist)? body;

//paralist in function
paralist: variable (CM variable)*;

//body in function
body: BODY CL stmt* ENDBODY DOT;

//statement list
stmt
    : stmt_assign
    | stmt_break
    | stmt_call
    | stmt_con
    | stmt_do
    | stmt_for
    | stmt_if
    | stmt_ret
    | stmt_while
    | vardeclare
    ;
//assignment statement
stmt_assign: variable AS exp SM;

//if statement
stmt_if: IF exp THEN stmt* (ELSEIF exp THEN stmt*)* (ELSE stmt*)? ENDIF DOT;

//for statement
stmt_for: FOR LP for_loop_con RP DO stmt* ENDFOR DOT;
for_loop_con: ID AS exp CM exp CM exp;

//while statement
stmt_while: WHILE  exp  DO stmt* ENDWHILE DOT;

//do-while statement
stmt_do: DO stmt* WHILE exp ENDDO DOT;

//break statement
stmt_break: BREAK SM;

//continue statement
stmt_con: CONTINUE SM;

//call_statement
stmt_call: call SM;

//return statement:;
stmt_ret: RETURN exp SM;

//call function
call: ID LP (exp (CM exp)*)* RP;



ele_exp: ID index_op;
index_op: LR exp RR (index_op)*;

// expression

exp
    : exp1 relational exp1
    | exp1
    ;
exp1
    : exp1 logical exp2
    | exp1 adding exp2
    | exp1 multiplying exp2
    | exp2
    ;
exp2
    : NOT exp2
    | (SUB | SUBF) exp2 
    | exp3
    ;
exp3: exp3 LR exp RR | exp4;
exp4
    : call 
    | operands
    ;
operands
    : lit 
    | LP exp RP 
    | arraylit 
    | variable
    ;
relational
    : EQ 
    | NEQ 
    | LT 
    | GT 
    | LTE 
    | GTE 
    | LTF 
    | GTF
    | LTEF
    | GTEF
    ;
logical
    :
    AND
    | OR
    ;
adding
    : ADD
    | ADDF
    | SUB
    | SUBF
    ;
multiplying
    : MUL
    | MULF
    | DIV
    | DIVF
    | MOD
    ;
variable
    : ID 
    | ele_exp
    ;
arraylit
    : LB arraylit (CM arraylit)* RB
    | LB lit (CM lit)* RB
    ;

lit
    : INTLIT
    | FLOATLIT
    | boollit
    | STRINGLIT
    ;

boollit: TRUE | FALSE;

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
FALSE:      'False';
ENDDO:      'EndDo';

//OPERATORS
AS:     '=';
ADD:    '+';
ADDF:   '+.';
SUB:    '-';
SUBF:   '-.';
MUL:    '*';
MULF:   '*.';
DIV:    '\\';
DIVF:   '\\.';
MOD:    '%';
NOT:    '!';
AND:    '&&';
OR:     '||';
EQ:     '==';
NEQ:    '!='|'=/=';
LT:     '<';
GT:     '>';
LTE:    '<=';
GTE:    '>=';
LTF:    '<.';
GTF:    '>.';
LTEF:   '<=.';
GTEF:   '>=.';

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

INTLIT
    : DECIMALDIGIT
    | ('0o'|'0O') [1-7] OCTALDIGIT*
    | ('0x'|'0X') [1-9a-fA-F] HEXADECIMALDIGIT*
    ;
FLOATLIT
    : DECIMALDIGIT '.'? EXPONENT
    | DECIMALDIGIT '.' DIGIT+
    | DECIMALDIGIT '.' DIGIT* EXPONENT
    ;


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
fragment SCHAR
    : ~ ['"\\\r\n]
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

