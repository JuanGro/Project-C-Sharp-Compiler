import sys

if ".." not in sys.path: sys.path.insert(0, "..")
import ply.lex as lex

''' KEYWORDS that you can't use '''
reserved = (
   'IF', 'ELSE', 'DO', 'WHILE', 'INT', 'BOOL', 'STRING'
)

''' TOKENS to identify in the program '''
tokens = reserved + (
    # Literals
    'ID',
    # Math operators
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    # Logic operators
    'LOR', 'LAND',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    # Assignment =
    'EQUALS',
    # Delimeters ( ) { } . ;
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'DOT', 'SEMI',
    # STRING sentence
    'STRING_SENTENCE',
    # Digits
    'DIGIT',
    # Console
    'CONSOLE',
    # Inputs and outputs
    'WRITELINE', 'READLINE'
)

# Completely ignored characters
t_ignore = ' \t\x0c'

# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Console
t_CONSOLE = r'Console'

# Inputs and outputs
t_WRITELINE = r'WriteLine'
t_READLINE = r'ReadLine'

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

# Assignment operators
t_EQUALS = r'='

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_SEMI = r';'

# Strings
t_STRING_SENTENCE = r'\".*?\"'

# Identifiers and reserved words
reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[a-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t

''' Function to identify a number '''
def t_DIGIT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %s" % t.value)
        t.value = 0
    return t

''' Function to ignore comments '''
def t_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    # print("Comment present")

''' Function to know if there is a token not recognized '''
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
