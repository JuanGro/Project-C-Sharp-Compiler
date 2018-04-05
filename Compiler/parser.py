import sys
import lex
from node import *
import ply.yacc as yacc

# Get the token map
tokens = lex.tokens

def p_program(t):
    'program : statement_list'
    t[0] = Node("program", None, None, [t[1]])

# statement-list
def p_statement_list_1(t):
    'statement_list : empty'
    t[0] = Node("statement_list", None, None, None)

def p_statement_list_2(t):
    'statement_list : statement'
    t[0] = Node("statement_list", None, None, [t[1]])

def p_statement_list_3(t):
    'statement_list : statement_list statement'
    t[0] = Node("statement_list", None, None, [t[1], t[2]])

# statement
def p_statement(t):
    '''
    statement : expression_statement
              | selection_statement
              | iteration_statement
    '''
    t[0] = Node("statement", None, None, [t[1]])

# expression-statement
def p_expression_statement_1(t):
    'expression_statement : declaration_expression SEMI'
    T = Node(t[2], t[2])
    t[0] = Node("expression_statement", None, None, [t[1], T])

def p_expression_statement_2(t):
    'expression_statement : empty SEMI'
    T = Node(t[2], t[2])
    t[0] = Node("expression_statement", None, None, [t[1], T])

def p_expression_statement_3(t):
    'expression_statement : input_expression SEMI'
    T = Node(t[2], t[2])
    t[0] = Node("expression_statement", None, None, [t[1], T])

def p_expression_statement_4(t):
    'expression_statement : output_expression SEMI'
    T = Node(t[2], t[2])
    t[0] = Node("expression_statement", None, None, [t[1], T])

# declaration-expression
def p_declaration_expression_1(t):
    'declaration_expression : assignment_expression'
    t[0] = Node("declaration_expression", None, None, [t[1]])

def p_declaration_expression_2(t):
    'declaration_expression : type_specifier declaration_expression'
    t[0] = Node("declaration_expression", None, None, [t[1], t[2]])

# selection-statement
def p_selection_statement_1(t):
    'selection_statement : IF conditional_expression block_statement_list'
    T = Node(t[1], t[1])
    t[0] = Node("selection_statement", None, None, [T, t[2], t[3]])

def p_selection_statement_2(t):
    'selection_statement : selection_statement ELSE block_statement_list'
    T = Node(t[2], t[2])
    t[0] = Node("selection_statement", None, None, [t[1], T, t[3]])

# iteration-statement:
def p_iteration_statement_1(t):
    'iteration_statement : WHILE conditional_expression block_statement_list'
    T = Node(t[1], t[1])
    t[0] = Node("iteration_statement", None, None, [T, t[2], t[3]])

def p_iteration_statement_2(t):
    'iteration_statement : DO block_statement_list WHILE conditional_expression'
    T1 = Node(t[1], t[1])
    T2 = Node(t[3], t[3])
    t[0] = Node("iteration_statement", None, None, [T1, t[2], T2, t[4]])

# block-statement-list
def p_block_statement_list_1(t):
    'block_statement_list : LBRACE statement_list RBRACE'
    T1 = Node(t[1], t[1])
    T2 = Node(t[3], t[3])
    t[0] = Node("block_statement_list", None, None, [T1, t[2], T2])

# conditional-statement
def p_conditional_expression_1(t):
    'conditional_expression : LPAREN logical_expression RPAREN'
    T1 = Node(t[1], t[1])
    T2 = Node(t[3], t[3])
    t[0] = Node("conditional_expression", None, None, [T1, t[2], T2])

# assignment-expression
def p_assignment_expression_1(t):
    'assignment_expression : variable_expression'
    t[0] = Node("assignment_expression", None, None, [t[1]])

def p_assignment_expression_2(t):
    'assignment_expression : assignment_expression EQUALS logical_expression'
    T = Node(t[2], t[2])
    t[0] = Node("assignment_expression", None, None, [t[1], T, t[3]])

def p_assignment_expression_3(t):
    'assignment_expression : assignment_expression EQUALS input_expression'
    T = Node(t[2], t[2])
    t[0] = Node("assignment_expression", None, None, [t[1], T, t[3]])

# logical-expression:
def p_logical_expression_1(t):
    'logical_expression : equality_expression'
    t[0] = Node("logical_expression", None, None, [t[1]])

def p_logical_expression_2(t):
    'logical_expression : logical_expression logical_operators equality_expression'
    t[0] = Node("logical_expression", None, None, [t[1], t[2], t[3]])

# equality-expression:
def p_equality_expression_1(t):
    'equality_expression : relational_expression'
    t[0] = Node("equality_expression", None, None, [t[1]])

def p_equality_expression_2(t):
    'equality_expression : equality_expression equality_operators relational_expression'
    t[0] = Node("equality_expression", None, None, [t[1], t[2], t[3]])

# relational-expression:
def p_relational_expression_1(t):
    'relational_expression : math_expression'
    t[0] = Node("relational_expression", None, None, [t[1]])

def p_relational_expression_2(t):
    'relational_expression : relational_expression relational_operators math_expression'
    t[0] = Node("relational_expression", None, None, [t[1], t[2], t[3]])

# math-expression
def p_math_expression_1(t):
    'math_expression : primary_expression'
    t[0] = Node("math_expression", None, None, [t[1]])

def p_math_expression_2(t):
    'math_expression : math_expression math_operators primary_expression'
    t[0] = Node("math_expression", None, None, [t[1], t[2], t[3]])

# input-expression
def p_input_expression(t):
    'input_expression : CONSOLE DOT READLINE LPAREN RPAREN'
    T1 = Node(t[1], t[1])
    T2 = Node(t[2], t[2])
    T3 = Node(t[3], t[3])
    T4 = Node(t[4], t[4])
    T5 = Node(t[5], t[5])
    t[0] = Node("input_expression", None, None, [T1, T2, T3, T4, T5])

# output-expression
def p_output_expression(t):
    'output_expression : CONSOLE DOT WRITELINE conditional_expression'
    T1 = Node(t[1], t[1])
    T2 = Node(t[2], t[2])
    T3 = Node(t[3], t[3])
    t[0] = Node("output_expression", None, None, [T1, T2, T3, t[4]])

''' TERMINALS '''
# type-specifier
def p_type_specifier(t):
    '''
    type_specifier : INT
                   | BOOL
                   | STRING
    '''
    T = Node(t[1], t[1])
    t[0] = Node('type_specifier', None, None, [T])

# logical-operators
def p_logical_operators(t):
    '''
    logical_operators : LAND
                      | LOR
    '''
    T = Node(t[1], t[1])
    t[0] = Node('logical_operators', None, None, [T])

# equality-operators
def p_equality_operators(t):
    '''
    equality_operators : EQ
                       | NE
    '''
    T = Node(t[1], t[1])
    t[0] = Node('equality_operators', None, None, [T])

# relational-operators
def p_relational_operators(t):
    '''
    relational_operators : LT
                         | GT
                         | LE
                         | GE
    '''
    T = Node(t[1], t[1])
    t[0] = Node('relational_operators', None, None, [T])

# math-operators
def p_math_operators(t):
    '''
    math_operators : PLUS
                   | MINUS
                   | TIMES
                   | DIVIDE
    '''
    T = Node(t[1], t[1])
    t[0] = Node('math_operators', None, None, [T])

# primary-expression
def p_primary_expression(t):
    '''
    primary_expression :  variable_expression
                       |  TRUE
                       |  FALSE
                       |  DIGIT
                       |  STRING_SENTENCE
    '''
    T = Node(t[1], t[1])
    t[0] = Node('primary_expression', None, None, [T])

# variable-expression
def p_variable_expression(t):
    '''
    variable_expression : ID
                        | CONSTANT
    '''
    T = Node(t[1], t[1])
    t[0] = Node('variable_expression', None, None, [T])

def p_empty(t):
    'empty : '
    t[0] = Node('empty', None, None, None)

def p_error(t):
    print("ERROR:", t.value)

import profile
# Build the grammar

yacc.yacc()
