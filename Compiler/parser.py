import sys
import lex
import ply.yacc as yacc

# Get the token map
tokens = lex.tokens

def p_block_statement_list_1(t):
    'block_statement_list : LBRACE statement_list RBRACE'
    pass

def p_statement_list_1(t):
    'statement_list : statement'
    pass

def p_statement_list_2(t):
    'statement_list : statement_list statement'
    pass

def p_statement(t):
    '''
    statement : expression_statement
              | selection_statement
              | iteration_statement
    '''
    pass

# expression_statement
def p_expression_statement_1(t):
    'expression_statement : declaration_expression SEMI'
    pass

# declaration_expression
def p_declaration_expression_1(t):
    'declaration_expression : assignment_expression'
    pass

def p_declaration_expression_2(t):
    'declaration_expression : type_specifier declaration_expression'
    pass

# selection-statement
def p_selection_statement_1(t):
    'selection_statement : IF conditional_statement block_statement_list'
    pass

def p_selection_statement_2(t):
    'selection_statement : selection_statement ELSE block_statement_list'
    pass

# iteration-statement:
def p_iteration_statement_1(t):
    'iteration_statement : WHILE conditional_statement block_statement_list'
    pass

def p_iteration_statement_2(t):
    'iteration_statement : DO block_statement_list WHILE conditional_statement SEMI'
    pass

# conditional-statement
def p_conditional_statement_1(t):
    'conditional_statement : LPAREN logical_expression RPAREN'
    pass

# assignment-expression
def p_assignment_expression_1(t):
    'assignment_expression : additive_expression'
    pass

def p_assignment_expression_2(t):
    'assignment_expression : assignment_expression EQUALS additive_expression'
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
def p_type_specifier(t):
    '''
    type_specifier : INT
                   | BOOL
                   | STRING
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

def p_additive_operators(t):
    '''
    additive_operators : PLUS
                       | MINUS
    '''
    pass

def p_multiplicative_operators(t):
    '''
    multiplicative_operators : TIMES
                             | DIVIDE
    '''
    pass

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
