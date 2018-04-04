import sys
import lex
import ply.yacc as yacc

# Get the token map
tokens = lex.tokens

def p_statement(t):
    '''
    statement : expression_statement
              | selection_statement
              | iteration_statement
    '''
    pass

# type-specifier:
def p_type_specifier(t):
    '''
    type_specifier : INT
                      | BOOL
                      | STRING
    '''
    pass

# expression_statement
def p_expression_statement_1(t):
    'expression_statement : declaration_expression SEMI'

# declaration_expression
def p_declaration_expression_1(t):
    'declaration_expression : assignment_expression'

def p_declaration_expression_2(t):
    'declaration_expression : type_specifier declaration_expression'

# selection-statement
def p_selection_statement_1(t):
    'selection_statement : IF LPAREN logical_expression RPAREN LBRACE statement RBRACE'
    pass

def p_selection_statement_2(t):
    'selection_statement : selection_statement ELSE LBRACE statement RBRACE'
    pass

# iteration_statement:
def p_iteration_statement_1(t):
    'iteration_statement : WHILE LPAREN logical_expression RPAREN statement'
    pass

def p_iteration_statement_2(t):
    'iteration_statement : DO statement WHILE LPAREN logical_expression RPAREN SEMI'
    pass

# assignment_expression
def p_assignment_expression_1(t):
    'assignment_expression : additive_expression'
    pass

def p_assignment_expression_2(t):
    'assignment_expression : assignment_expression assignment_operators additive_expression'
    pass

# logical-expression:
def p_logical_expression_1(t):
    'logical_expression : equality_expression'
    pass

def p_logical_expression_2(t):
    'logical_expression : logical_expression logical_operators equality_expression'
    pass

# equality-expression:
def p_equality_expression_1(t):
    'equality_expression : relational_expression'
    pass

def p_equality_expression_2(t):
    'equality_expression : equality_expression equality_operators relational_expression'
    pass

# relational-expression:
def p_relational_expression_1(t):
    'relational_expression : additive_expression'
    pass

def p_relational_expression_2(t):
    'relational_expression : relational_expression relational_operators additive_expression'
    pass

# additive-expression
def p_additive_expression_1(t):
    'additive_expression : multiplicative_expression'
    pass

def p_additive_expression_2(t):
    'additive_expression : additive_expression additive_operators multiplicative_expression'
    pass

# multiplicative_expression
def p_multiplicative_expression_1(t):
    'multiplicative_expression : primary_expression'
    pass

def p_multiplicative_expression_2(t):
    'multiplicative_expression : multiplicative_expression multiplicative_operators primary_expression'
    pass

''' TERMINALS '''
def p_assignment_operators(t):
    '''
    assignment_operators : EQUALS
    '''
    pass

def p_logical_operators(t):
    '''
    logical_operators : LAND
                      | LOR
    '''
    pass

def p_equality_operators(t):
    '''
    equality_operators : EQ
                       | NE
    '''
    pass

def p_relational_operators(t):
    '''
    relational_operators : LT
                         | GT
                         | LE
                         | GE
    '''
    pass

# additive_operators
def p_additive_operators(t):
    '''
    additive_operators : PLUS
                       | MINUS
    '''

# multiplicative_operators
def p_multiplicative_operators(t):
    '''
    multiplicative_operators : TIMES
                             | DIVIDE
    '''

# primary-expression:
def p_primary_expression(t):
    '''
    primary_expression :  ID
                       |  DIGIT
    '''
    pass

def p_error(t):
    print("Whoa. We're hosed")

import profile
# Build the grammar

yacc.yacc()
