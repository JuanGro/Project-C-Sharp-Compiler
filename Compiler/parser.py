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
    '''type_specifier : INT
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
    'selection_statement : IF LPAREN or_expression RPAREN statement'
    pass

# def p_selection_statement_2(t):
#     'selection_statement : IF LPAREN or_expression RPAREN statement ELSE statement '
#     pass

# iteration_statement:
def p_iteration_statement_1(t):
    'iteration_statement : WHILE LPAREN or_expression RPAREN statement'
    pass

def p_iteration_statement_2(t):
    'iteration_statement : DO statement WHILE LPAREN or_expression RPAREN SEMI'
    pass

# assignment_expression
def p_assignment_expression_1(t):
    'assignment_expression : additive_expression'
    pass

def p_assignment_expression_2(t):
    'assignment_expression : assignment_expression EQUALS additive_expression'
    pass

# or-expression:
def p_or_expression_1(t):
    'or_expression : and_expression'
    pass

def p_or_expression_2(t):
    'or_expression : or_expression LOR and_expression'
    pass

# AND-expression
def p_and_expression_1(t):
    'and_expression : equality_expression'
    pass

def p_and_expression_2(t):
    'and_expression : and_expression LAND equality_expression'
    pass

# equality-expression:
def p_equality_expression_1(t):
    'equality_expression : relational_expression'
    pass

def p_equality_expression_2(t):
    'equality_expression : equality_expression EQ relational_expression'
    pass

def p_equality_expression_3(t):
    'equality_expression : equality_expression NE relational_expression'
    pass

# relational-expression:
def p_relational_expression_1(t):
    'relational_expression : additive_expression'
    pass

def p_relational_expression_2(t):
    'relational_expression : relational_expression LT additive_expression'
    pass

def p_relational_expression_3(t):
    'relational_expression : relational_expression GT additive_expression'
    pass

def p_relational_expression_4(t):
    'relational_expression : relational_expression LE additive_expression'
    pass

def p_relational_expression_5(t):
    'relational_expression : relational_expression GE additive_expression'
    pass

# additive-expression
def p_additive_expression_1(t):
    'additive_expression : multiplicative_expression'
    pass

def p_additive_expression_2(t):
    'additive_expression : additive_expression PLUS multiplicative_expression'
    pass

def p_additive_expression_3(t):
    'additive_expression : additive_expression MINUS multiplicative_expression'
    pass

# multiplicative_expression
def p_multiplicative_expression_1(t):
    'multiplicative_expression : primary_expression'
    pass

def p_multiplicative_expression_2(t):
    'multiplicative_expression : multiplicative_expression TIMES primary_expression'
    pass

def p_multiplicative_expression_3(t):
    'multiplicative_expression : multiplicative_expression DIVIDE primary_expression'
    pass

# primary-expression:
def p_primary_expression(t):
    '''
    primary_expression :  ID
                        |   DIGIT
    '''
    pass

def p_error(t):
    print("Whoa. We're hosed")

import profile
# Build the grammar

yacc.yacc()
