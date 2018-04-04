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

# Test it out
test1 = '''
// int number1 = 5;
'''
test2 = '''
/*
bool flag;
*/
'''
test3 = '''
int number2 = 6;
'''
test4 = '''
bool FLAG = true;
'''
test5 = '''
Console.WriteLine("Hello World!");
'''
test6 = '''
int number3 = 7;
bool flag2 = false;
string name1 = "Juan";
'''
test7 = '''
while(number1 <= 50) {
    number1 = number1 + 1;
    if(number1 == 35) {
        flag = true;
    } else {
        flag = false;
    }
}
'''
test8 = '''
Console.ReadLine();
Console.WriteLine("Hello World!");
'''
test9 = '''
bool flag = false;
int number1 = 3 + 4 * 5;
name2 = "Carlos";

if(number1 == 35) {
    // flag = true;
    number1 = Console.ReadLine();
} else {
    flag = false;
}

/*
while(number1 <= 50) {
    number1 = number1 + 1;
}
*/

string sentence_aux = "Result";
Console.WriteLine(sentence_aux);
Console.WriteLine(number1);
'''
test10 = '''
flag = false;
bool flag;
'''
test11 = '''
"Hello World";
Console.WriteLine(int number1);
Console.WriteLine(int number_Aux2);
'''
test12 = '''
int number3 = 0;
while true {
    number3 = number3 + 1;
}
'''

# Check tests
print("\nTest 1:")
lex.runmain(data = test1)
print("\nTest 2")
lex.runmain(data = test2)
print("\nTest 3")
lex.runmain(data = test3)
print("\nTest 4")
lex.runmain(data = test4)
print("\nTest 5")
lex.runmain(data = test5)
print("\nTest 6")
lex.runmain(data = test6)
print("\nTest 7")
lex.runmain(data = test7)
print("\nTest 8")
lex.runmain(data = test8)
print("\nTest 9")
lex.runmain(data = test9)
print("\nTest 10")
lex.runmain(data = test10)
print("\nTest 11")
lex.runmain(data = test11)
print("\nTest 12")
lex.runmain(data = test12)
