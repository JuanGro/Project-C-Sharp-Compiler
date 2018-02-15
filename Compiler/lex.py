import sys

if ".." not in sys.path: sys.path.insert(0,"..")
import ply.lex as lex

''' KEYWORDS that you can't use '''
keywords = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'int' : 'INTEGER_TYPE',
   'bool' : 'BOOLEAN_TYPE',
   'string' : 'STRING_TYPE',
   'false' : 'FALSE',
   'true' : 'TRUE',
   'Console.ReadLine': 'READ',
   'Console.WriteLine' : 'WRITE',
}

''' TOKENS to identify in the program '''
tokens = list(keywords.values()) + [
    # Math operators
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    # Logic operators
    'EQUALS', 'NOT_EQUALS', 'LESS_EQUAL_THAN', 'GREATER_EQUAL_THAN', 'LESS_THAN', 'GREATER_THAN', 'AND', 'OR', 'NOT',
    # Others
    'ASSIGN', 'SEMICOLON', 'QUOTATION_MARK',
    # Symbols
    'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS',
    # Inputs and outputs
    'ID', 'DIGIT', 'STRING']

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

''' Function to ignore comments '''
def t_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    print("Comment present")

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

Console.WriteLine("Result");
Console.WriteLine(number1);
'''
test10 = '''
flag = false;
bool flag;
'''
test11 = '''
"Hello World";
Console.WriteLine(int number1);
Console.WriteLine(int NUMBER2);
'''
test12 = '''
int number3 = 0;
while true {
    number3 = number3 + 1;
}
'''

# Check tests
print("\nTest 1")
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
