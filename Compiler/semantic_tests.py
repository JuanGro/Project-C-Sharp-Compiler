from semantic import *

# Test it out
test1 = '''
console.writeline("Hi");
int a;
string b;
'''
test2 = '''
int number3 = 7;
bool flag2 = false;
string name1 = "Juan";
'''
test3 = '''
int number2 = 6;
'''
test4 = '''
bool FLAG = true;
bool FLAG = false;
'''
test5 = '''
int a;
a = "hello";
'''
test6 = '''
int result;
int num1 = 9;

if (num1 > num2) {
    result = num1;
    num1 = 10;
} else {
    result = num2;
}
'''

# Check tests
print("\nTest 1:")
t = yacc.parse(test1)
getSymbolTable(x)
emptyTerminals(x)

print("\nTest 2:")
t = yacc.parse(test2)
getSymbolTable(x)
emptyTerminals(x)

print("\nTest 3:")
t = yacc.parse(test3)
getSymbolTable(x)
emptyTerminals(x)

print("\nTest 4:")
t = yacc.parse(test4)
getSymbolTable(x)
emptyTerminals(x)

print("\nTest 5:")
t = yacc.parse(test5)
getSymbolTable(x)
emptyTerminals(x)

print("\nTest 6:")
t = yacc.parse(test6)
getSymbolTable(x)
emptyTerminals(x)
