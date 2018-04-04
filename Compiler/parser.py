import sys
import lex
import ply.yacc as yacc

# Get the token map
tokens = lex.tokens

# statement-list
def p_statement_list_1(t):
    'statement_list : empty'
    pass

def p_statement_list_2(t):
    'statement_list : statement'
    pass

def p_statement_list_2(t):
    'statement_list : statement_list statement'
    pass

# statement
def p_statement(t):
    '''
    statement : expression_statement
              | selection_statement
              | iteration_statement
    '''
    pass

# expression-statement
def p_expression_statement_1(t):
    'expression_statement : declaration_expression SEMI'
    pass

def p_expression_statement_2(t):
    'expression_statement : output_expression SEMI'
    pass

# I am not sure!
def p_expression_statement_3(t):
    'expression_statement : input_expression SEMI'
    pass

def p_expression_statement_4(t):
    'expression_statement : empty SEMI'
    pass

# declaration-expression
def p_declaration_expression_1(t):
    'declaration_expression : assignment_expression'
    pass

def p_declaration_expression_2(t):
    'declaration_expression : type_specifier declaration_expression'
    pass

# selection-statement
def p_selection_statement_1(t):
    'selection_statement : IF conditional_expression block_statement_list'
    pass

def p_selection_statement_2(t):
    'selection_statement : selection_statement ELSE block_statement_list'
    pass

# iteration-statement:
def p_iteration_statement_1(t):
    'iteration_statement : WHILE conditional_expression block_statement_list'
    pass

def p_iteration_statement_2(t):
    'iteration_statement : DO block_statement_list WHILE conditional_expression SEMI'
    pass

# block-statement-list
def p_block_statement_list_1(t):
    'block_statement_list : LBRACE statement_list RBRACE'
    pass

# conditional-statement
def p_conditional_expression_1(t):
    'conditional_expression : LPAREN logical_expression RPAREN'
    pass

# assignment-expression
def p_assignment_expression_1(t):
    'assignment_expression : variable_expression'
    pass

def p_assignment_expression_2(t):
    'assignment_expression : assignment_expression EQUALS logical_expression'
    pass

def p_assignment_expression_3(t):
    'assignment_expression : assignment_expression EQUALS input_expression'
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
    'relational_expression : math_expression'
    pass

def p_relational_expression_2(t):
    'relational_expression : relational_expression relational_operators math_expression'
    pass

# math-expression
def p_math_expression_1(t):
    'math_expression : primary_expression'
    pass

def p_math_expression_2(t):
    'math_expression : math_expression math_operators primary_expression'
    pass

# input-expression
def p_input_expression(t):
    'input_expression : CONSOLE DOT READLINE'
    pass

# output-expression
def p_output_expression(t):
    'output_expression : CONSOLE DOT WRITELINE conditional_expression'
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

def p_math_operators(t):
    '''
    math_operators : PLUS
                   | MINUS
                   | TIMES
                   | DIVIDE
    '''
    pass

def p_primary_expression(t):
    '''
    primary_expression :  variable_expression
                       |  DIGIT
                       |  STRING_SENTENCE
    '''
    pass

def p_variable_expression(t):
    '''
    variable_expression : ID
                        | CONSTANT
    '''
    pass

def p_empty(t):
    'empty : '
    pass

def p_error(t):
    print("Error", t)

import profile
# Build the grammar

yacc.yacc()

# while 1:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     yacc.parse(s)
