// ID: 1812516

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
/*
    Program
*/
program  : vardeclare* funcdeclare* EOF;


/*
    Var declare
*/
vardeclare: VAR CL idlistinit SM;
idlistinit: idinit (CM idinit)*;
idinit: iddimen (AS lit)?;

iddimen: ID dimension?;

dimension: LR INTLIT RR dimension?;

/*
    Function declare
*/
funcdeclare: FUNCTION CL ID (PARAMETER CL paralist)? body;

//paralist in function
paralist: iddimen (CM iddimen)*;

//body in function
body: BODY CL vardeclare* stmt* ENDBODY DOT;

/*
    Statement
*/

//a statement
stmt
    : assign_stmt
    | break_stmt
    | call_stmt
    | continue_stmt
    | do_stmt
    | for_stmt
    | if_stmt
    | return_stmt
    | while_stmt
    ;

stmt_list: vardeclare* stmt*;

//assignment statement
assign_stmt: variable AS exp SM;

//if statement
if_stmt: IF exp THEN stmt_list (ELSEIF exp THEN stmt_list)* (ELSE stmt_list)? ENDIF DOT;

//for statement
for_stmt: FOR LP for_loop_con RP DO stmt_list ENDFOR DOT;
for_loop_con: ID AS exp CM exp CM exp;

//while statement
while_stmt: WHILE exp DO stmt_list ENDWHILE DOT;

//do-while statement
do_stmt: DO stmt_list WHILE exp ENDDO DOT;

//break statement
break_stmt: BREAK SM;

//continue statement
continue_stmt: CONTINUE SM;

//call_statement
call_stmt: call SM;

//return statement:;
return_stmt: RETURN exp? SM;


/*
    Expression
*/
exp
    : exp1 relational exp1
    | exp1
    ;
// exp1
//     : exp1 logical exp2
//     | exp1 adding exp2
//     | exp1 multiplying exp2
//     | exp2
//     ;
exp1
    : exp1 logical exp11
    | exp11
    ;
exp11
    : exp11 adding exp12
    | exp12
    ;
exp12
    : exp12 multiplying exp2
    | exp2
    ;
exp2
    : (SUB | SUBF) exp2
    | NOT exp2
    | exp3
    ;
exp3
    : ele_exp
    | exp4
    ;
exp4
    : call
    | operands
    ;
call: ID LP (exp (CM exp)*)? RP;
operands
    : lit
    | LP exp RP
    | ID
    ;

variable
    : ID
    | ele_exp
    ;
ele_exp : (ID | call) index_op;
index_op: LR exp RR index_op?;
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
    : AND
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

/*
    Literals
*/
arraylit: LB (lit (CM lit)*)? RB;

primitive
    : INTLIT
    | FLOATLIT
    | boollit
    | STRINGLIT
    ;
lit
    : primitive
    | arraylit
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
    | ('0x'|'0X') [1-9A-F] HEXADECIMALDIGIT*
    ;
FLOATLIT
    : DIGIT+ '.'? EXPONENT
    | DIGIT+ '.' DIGIT* EXPONENT?
    ;

STRINGLIT: '"' SCHAR* '"'
    {
        y = str(self.text)
        self.text = y[1:-1]
    };

ID: [a-z][0-9a-zA-Z_]*;

//FRAGMENT
fragment NONDIGIT: [a-zA-Z_];
fragment DIGIT: [0-9];
fragment NONZERODIGIT: [1-9];

fragment DECIMALDIGIT: '0'| (NONZERODIGIT DIGIT*);
fragment OCTALDIGIT: [0-7];
fragment HEXADECIMALDIGIT: [0-9A-F];
fragment BINARYDIGIT: [01];

fragment SIGN: [+-];
fragment EXPONENT: [eE] SIGN? DIGIT+;

fragment ESC_SEQ: '\\' [btnfr'\\];
fragment SCHAR
    : ~ ['"\\\r\n\b\f]
    | ESC_SEQ
    | '\'"'
    ;

//SKIP
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
COMMENT: '**' .*? '**' -> skip;

//ERROR
UNCLOSE_STRING: '"' SCHAR* ( [\r\n\b\f] | EOF)
    {
        y = str(self.text)
        escape = ['\r','\n','\b','\f']
        if y[-1] in escape:
            self.text = y[1:-1]
        else:
            self.text = y[1:]
    };
ERROR_CHAR: .;
ILLEGAL_ESCAPE:  '"' SCHAR* (('\\' ~[btnfr\\]) | ('\'' ~'"'))
    {
        y = str(self.text)
        if y[-1] == '"':
            self.text = y[1:-1]
        else:
            self.text = y[1:]
    };
UNTERMINATED_COMMENT: '**' (.*? | EOF) ;
