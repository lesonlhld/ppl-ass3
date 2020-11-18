grammar BKIT;
//1810482
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

program: SKIP_* variable_decl* SKIP_* body_decl* SKIP_* EOF;

fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment NON_ZERO_DIGIT: [1-9];
fragment OCT_DIGIT: [0-7];
fragment NON_OCT_DIGIT: [1-7];
fragment HEX_DIGIT: [0-9A-F];
fragment NON_HEX_DIGIT: [1-9A-F];
fragment INT_PART: DECIMAL_INTEGER;
fragment DEC_PART: DOT DECIMAL_INTEGER| DOT [0]* NON_ZERO_DIGIT;
fragment EXPONENT: [eE][+-]? DECIMAL_INTEGER;
fragment POINT_FLOAT: (INT_PART DEC_PART) | (INT_PART DOT);
fragment EXPONENT_FLOAT: (INT_PART | POINT_FLOAT) EXPONENT;
fragment WS: [ \t\r\n\f]+; // White-space characters
fragment COMMENT: '**' .*? '**';
fragment NEWLINE: ('\r' '\n'? | '\n');
fragment DOUBLE_QUOTE: ["];
fragment SINGLE_QUOTE: ['];
fragment STRING_CONTENT: '\'"' | ~["\b\f\r\n'\\] | ESCAPE_SEQ;
fragment ESCAPE_SEQ: '\\' [bfrnt'\\"];
fragment ESCAPE_ILLEGAL: '\\' ~[bfrnt'\\"] | ~'\\' | '\'' ~["];
fragment ARRAY_LIST: ARRAY_TYPE (COMMA ARRAY_TYPE)*;
fragment ARRAY_TYPE: (DECIMAL_INTEGER | STRING | BOOLEAN | FLOAT);
fragment DIMENSION: LEFT_BRACKET (DECIMAL_INTEGER | ID) RIGHT_BRACKET;

/*
 * Lexer rules
 */

// Identifiers
ID: [a-z][a-zA-Z0-9_]*;

// Keywords
VAR: 'Var';
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF:'ElseIf';
ENDBODY:'EndBody';
ENDIF:'EndIf';
ENDFOR:'EndFor';
ENDWHILE:'EndWhile';
FOR:'For';
FUNCTION:'Function';
IF:'If';
PARAMETER:'Parameter';
RETURN:'Return';
THEN:'Then';
WHILE:'While';
TRUE:'True';
FALSE:'False';
ENDDO:'EndDo';

// Type
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
BOOLEAN_TYPE: 'boolean';
STRING_TYPE: 'string';

// Operators
ADD: '+';
ADD_F: '+.';
SUB: '-';
SUB_F: '-.';
MULTI: '*';
MULTI_F: '*.';
DIV: '\\';
DIV_F: '\\.';
MOD: '%';

NOT: '!';
ANDAND: '&&';
OROR: '||';

EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
GREATER_THAN: '>';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';
NOT_EQUAL_F: '=/=';
LESS_THAN_F: '<.';
GREATER_THAN_F: '>.';
GREATER_EQUAL_F: '>=.';
LESS_EQUAL_F: '<=.';

// Separators
SEMI: ';';
COLON: ':';
DOT: '.';
COMMA: ',';
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
ASSIGN: '=';

// Literals
DECIMAL_INTEGER: NON_ZERO_DIGIT DIGIT* | [0];
HEX_INTEGER: [0][xX] NON_HEX_DIGIT HEX_DIGIT*;
OCT_INTEGER: [0][oO] NON_OCT_DIGIT OCT_DIGIT*;

FLOAT: POINT_FLOAT | EXPONENT_FLOAT;

BOOLEAN: TRUE | FALSE;

// ARRAY_L: LEFT_BRACE ARRAY_L (COMMA ARRAY_L)* RIGHT_BRACE | LEFT_BRACE ARRAY_LIST? RIGHT_BRACE | ARRAY_LIST ;
// ARRAY_DECL: ID DIMENSION+;

STRING: DOUBLE_QUOTE STRING_CONTENT*? DOUBLE_QUOTE {
		y = str(self.text)
		self.text = y[1:-1]
	};

SKIP_: (COMMENT | WS | NEWLINE) -> skip ; // skip spaces, tabs, newlines or comment

/*
 * Parser rules
 */
variable_decl: VAR COLON variable_list SEMI;

// variable_list: (ID | array_decl) COMMA variable_list | ID | array_decl;

variable_list: variable (ASSIGN init_value)? COMMA variable_list | variable (ASSIGN init_value)?;

variable: ID | array_decl;

array_decl: ID dimension;

dimension: LEFT_BRACKET integer RIGHT_BRACKET dimension | LEFT_BRACKET integer RIGHT_BRACKET;

init_value: literal COMMA init_value | literal;

literal: array | integer | FLOAT  | boolean_literal | STRING;

integer: '-'? (DECIMAL_INTEGER | HEX_INTEGER | OCT_INTEGER);

boolean_literal: TRUE | FALSE ;

array: LEFT_BRACE array_list? RIGHT_BRACE;

array_list: literal COMMA array_list | literal;

body_decl: init_body body;

init_body: FUNCTION COLON ID parameter?;

// parameter: PARAMETER COLON variable_list;

parameter: PARAMETER COLON parameter_list;

parameter_list: variable COMMA parameter_list | variable;

body: BODY COLON stmt_list ENDBODY DOT;

var_list: variable_decl var_list | variable_decl;

// Statement
stmt: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | call_stmt | return_stmt;

stmt_list: var_list? stmt*;

// assign_stmt: ID index_operators? ASSIGN exp SEMI;

assign_stmt: exp6 ASSIGN exp SEMI;

if_stmt: IF exp THEN stmt_list else_if? (ELSE stmt_list)? ENDIF DOT;

else_if: ELSEIF exp THEN stmt_list else_if | ELSEIF exp THEN stmt_list;

for_stmt: FOR LEFT_PAREN for_condition RIGHT_PAREN DO stmt_list ENDFOR DOT;

for_condition: ID ASSIGN exp COMMA exp COMMA exp;

while_stmt: WHILE exp DO stmt_list ENDWHILE DOT;

do_while_stmt: DO stmt_list WHILE exp ENDDO DOT;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

call_stmt: ID LEFT_PAREN exp_list? RIGHT_PAREN SEMI;

return_stmt: RETURN exp? SEMI;

// Funtion call
function_call: ID LEFT_PAREN exp_list? RIGHT_PAREN;

// Expression
exp: exp1 relational_operators exp1 | exp1;

exp1: exp1 boolean_operators exp2 | exp2;

exp2: exp2 adding_operators exp3 | exp3;

exp3: exp3 multiplying_operators exp4 | exp4;

exp4: NOT exp4 | exp5;

exp5: sign_operators exp5 | exp6;

exp6: exp6 index_operators | exp7;

exp7: function_call | LEFT_PAREN exp RIGHT_PAREN | operands;

exp_list: exp COMMA exp_list | exp;

// operands: ID | literal | element_exp;

operands: ID | literal;

// Operators
multiplying_operators: MULTI | MULTI_F | DIV | DIV_F | MOD;

adding_operators: ADD | ADD_F | SUB | SUB_F;

sign_operators: SUB| SUB_F;

boolean_operators: ANDAND | OROR;

relational_operators: EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | GREATER_EQUAL | LESS_EQUAL | NOT_EQUAL_F | LESS_THAN_F | GREATER_THAN_F | GREATER_EQUAL_F | LESS_EQUAL_F;

element_exp: expr_index index_operators;

index_operators: LEFT_BRACKET exp RIGHT_BRACKET index_operators | LEFT_BRACKET exp RIGHT_BRACKET;

expr_index: ID | function_call;

ERROR_CHAR: .;
UNCLOSE_STRING: '"' STRING_CONTENT* ([\b\f\r\n\\] | EOF) {
		y = str(self.text)
		self.text = y[1:]
	};
ILLEGAL_ESCAPE: '"' STRING_CONTENT* ESCAPE_ILLEGAL {
		y = str(self.text)
		self.text = y[1:]
	};
UNTERMINATED_COMMENT: '**' .*?;