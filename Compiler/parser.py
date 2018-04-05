import sys
import lex
from node import *
import ply.yacc as yacc

# Get the token map
tokens = lex.tokens

# statement-list
def p_statement_list_1(t):
    'statement_list : empty'
    t[0] = Node('statement-list', t[1])

def p_statement_list_2(t):
    'statement_list : statement'
    t[0] = Node('statement-list', t[1])

def p_statement_list_3(t):
    'statement_list : statement_list statement'
    t[0] = Node('statement-list', t[2])

# statement
def p_statement(t):
    '''
    statement : expression_statement
              | selection_statement
              | iteration_statement
    '''
    t[0] = Node('statement', t[1])

# expression-statement
def p_expression_statement_1(t):
    'expression_statement : declaration_expression SEMI'
    t[0] = Node('expression-statement', t[1], t[2])

def p_expression_statement_2(t):
    'expression_statement : empty SEMI'
    t[0] = Node('expression-statement', t[1], t[2])

def p_expression_statement_3(t):
    'expression_statement : input_expression SEMI'
    t[0] = Node('expression-statement', t[1], t[2])

def p_expression_statement_4(t):
    'expression_statement : output_expression SEMI'
    t[0] = Node('expression-statement', t[1], t[2])

# declaration-expression
def p_declaration_expression_1(t):
    'declaration_expression : assignment_expression'
    t[0] = Node('declaration-expression', t[1])

def p_declaration_expression_2(t):
    'declaration_expression : type_specifier declaration_expression'
    t[0] = Node('declaration-expression', t[2], t[1])

# selection-statement
def p_selection_statement_1(t):
    'selection_statement : IF conditional_expression block_statement_list'
    t[0] = Node('selection-statement', [t[2], t[3]], t[1])

def p_selection_statement_2(t):
    'selection_statement : selection_statement ELSE block_statement_list'
    t[0] = Node('selection-statement', t[3], t[2])

# iteration-statement:
def p_iteration_statement_1(t):
    'iteration_statement : WHILE conditional_expression block_statement_list'
    t[0] = Node('iteration-statement', [t[2], t[3]], t[1])

def p_iteration_statement_2(t):
    'iteration_statement : DO block_statement_list WHILE conditional_expression'
    t[0] = Node('iteration-statement', [t[2], t[4]], [t[1], t[3]])

# block-statement-list
def p_block_statement_list_1(t):
    'block_statement_list : LBRACE statement_list RBRACE'
    t[0] = Node('block-statement-list', t[2], [t[1], t[3]])

# conditional-statement
def p_conditional_expression_1(t):
    'conditional_expression : LPAREN logical_expression RPAREN'
    t[0] = Node('conditional-expression', t[2], [t[1], t[3]])

# assignment-expression
def p_assignment_expression_1(t):
    'assignment_expression : variable_expression'
    t[0] = Node('conditional-expression', t[1])

def p_assignment_expression_2(t):
    'assignment_expression : assignment_expression EQUALS logical_expression'
    t[0] = Node('conditional-expression', t[3], t[2])

def p_assignment_expression_3(t):
    'assignment_expression : assignment_expression EQUALS input_expression'
    t[0] = Node('conditional-expression', t[3], t[2])

# logical-expression:
def p_logical_expression_1(t):
    'logical_expression : equality_expression'
    t[0] = Node('conditional-expression', t[1])

def p_logical_expression_2(t):
    'logical_expression : logical_expression logical_operators equality_expression'
    t[0] = Node('conditional-expression', t[3], t[2])

# equality-expression:
def p_equality_expression_1(t):
    'equality_expression : relational_expression'
    t[0] = Node('conditional-expression', t[1])

def p_equality_expression_2(t):
    'equality_expression : equality_expression equality_operators relational_expression'
    t[0] = Node('conditional-expression', t[3], t[2])

# relational-expression:
def p_relational_expression_1(t):
    'relational_expression : math_expression'
    t[0] = Node('conditional-expression', t[1])

def p_relational_expression_2(t):
    'relational_expression : relational_expression relational_operators math_expression'
    t[0] = Node('conditional-expression', t[3], t[2])

# math-expression
def p_math_expression_1(t):
    'math_expression : primary_expression'
    t[0] = Node('conditional-expression', t[1])

def p_math_expression_2(t):
    'math_expression : math_expression math_operators primary_expression'
    t[0] = Node('conditional-expression', t[3], t[2])

# input-expression
def p_input_expression(t):
    'input_expression : CONSOLE DOT READLINE LPAREN RPAREN'
    t[0] = Node('conditional-expression', [t[1], t[2], t[3], t[4], t[5]])

# output-expression
def p_output_expression(t):
    'output_expression : CONSOLE DOT WRITELINE conditional_expression'
    t[0] = Node('conditional-expression', t[4], [t[1], t[2], t[3]])

''' TERMINALS '''
# type-specifier
def p_type_specifier(t):
    '''
    type_specifier : INT
                   | BOOL
                   | STRING
    '''
    t[0] = Node('type-specifier', t[1])

# logical-operators
def p_logical_operators(t):
    '''
    logical_operators : LAND
                      | LOR
    '''
    t[0] = Node('logical-operators', t[1])

# equality-operators
def p_equality_operators(t):
    '''
    equality_operators : EQ
                       | NE
    '''
    t[0] = Node('equality-operators', t[1])

# relational-operators
def p_relational_operators(t):
    '''
    relational_operators : LT
                         | GT
                         | LE
                         | GE
    '''
    t[0] = Node('relational-operators', t[1])

# math-operators
def p_math_operators(t):
    '''
    math_operators : PLUS
                   | MINUS
                   | TIMES
                   | DIVIDE
    '''
    t[0] = Node('math-operators', t[1])

# primary-expression
def p_primary_expression(t):
    '''
    primary_expression :  variable_expression
                       |  DIGIT
                       |  STRING_SENTENCE
                       |  boolean_expression
    '''
    t[0] = Node('primary-expression', t[1])

# variable-expression
def p_variable_expression(t):
    '''
    variable_expression : ID
                        | CONSTANT
    '''
    t[0] = Node('variable-expression', t[1])

# boolean-expression
def p_boolean_expression(t):
    '''
    boolean_expression : TRUE
                       | FALSE
    '''
    t[0] = Node('boolean-expression', t[1])

def p_empty(t):
    'empty : '
    pass

def p_error(t):
    print("ERROR:", t.value)

import profile
# Build the grammar

yacc.yacc()
