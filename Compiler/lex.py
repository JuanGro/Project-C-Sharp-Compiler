import sys

if ".." not in sys.path: sys.path.insert(0,"..")
import ply.lex as lex

''' KEYWORDS '''
keywords = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'int' : 'INTEGER',
   'bool' : 'BOOLEAN',
   'false' : 'FALSE',
   'true' : 'TRUE',
   'Console.ReadLine': 'READ',
   'Console.WriteLine' : 'WRITE',
}

tokens = list(keywords.values()) + [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',

    'EQUALS',
    'NOT_EQUALS',
    'LESS_EQUAL_THAN',
    'GREATER_EQUAL_THAN',
    'LESS_THAN',
    'GREATER_THAN',
    'AND',
    'OR',
    'NOT',

    'ASSIGN',
    'SEMICOLON',
    'QUOTATION_MARK',

    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'LEFT_PARENTHESIS',
    'RIGHT_PARENTHESIS',

    'ID',
    'DIGIT',
    'STRING'
]

states = (('comment', 'exclusive'),)

# Math operators
t_PLUS               = r'\+'
t_MINUS              = r'-'
t_TIMES              = r'\*'
t_DIVIDE             = r'/'
t_POWER              = r'\^'

# Logic operators
t_EQUALS             = r'\=\='
t_NOT_EQUALS         = r'\!\='
t_LESS_EQUAL_THAN    = r'\<\='
t_GREATER_EQUAL_THAN = r'\>\='
t_LESS_THAN          = r'\<'
t_GREATER_THAN       = r'\>'
t_AND                = r'!\&\&'
t_OR                 = r'\|\|'
t_NOT                = r'\!'

# Others
t_ASSIGN             = r'='
t_SEMICOLON          = r';'
t_QUOTATION_MARK     = r'"'

# Symbols
t_LEFT_BRACKET       = r'\{'
t_RIGHT_BRACKET      = r'\}'
t_LEFT_PARENTHESIS   = r'\('
t_RIGHT_PARENTHESIS  = r'\)'

# Inputs and outputs
t_READ               = r'Console.ReadLine'
t_WRITE              = r'Console.WriteLine'
t_STRING             = r'\".*?\"'

''' Function to identify an ID for a variable '''
def t_ID(t):
    r'[a-zA-Z_.][a-zA-Z_.0-9]*'
    t.type = keywords.get(t.value, 'ID')    # Check for reserved words
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

def t_SINGLE_COMMENT(t):
    r'//.*'
    pass
    # No return value. Token discarded

def t_comment(t):
    r'/\*'
    t.lexer.begin('comment')
    #print(t.value)

def t_comment_body_part(t):
    r'(.|\n)*\*/'
    t.lexer.begin('INITIAL')
    #print(t)

''' Ignore the tabs and spaces '''
t_ignore = " \t"

''' Function to avoid new line as a token '''
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

''' Function to know if there is a token not recognized '''
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_comment_error = t_error
t_comment_ignore = t_ignore

# Build the lexer
lexer = lex.lex()

# Test it out
test1 = '''
bool flag;
// Console.WriteLine(number1);
'''

# Give the lexer some input
#lexer.input(test1)
lex.runmain(data=test1)
