from semantic import *

# Test it out
test1 = '''
console.writeline("Hi");
int a = 2;
string b = "";
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
int a = "hello";
'''
test6 = '''
int result = 0;
int num1 = 9;
int num2 = 10;

if (num1 > num2) {
    result = num1;
    num1 = 10;
}
else {
    result = num2;
}
console.writeline(result);
'''

# Check tests
print("\nTest 1:")
t = yacc.parse(test1)
getSymbolTable(x)
generateCode(test1, 'test1')

print("\nTest 2:")
t = yacc.parse(test2)
getSymbolTable(x)
generateCode(test2, 'test2')

print("\nTest 3:")
t = yacc.parse(test3)
getSymbolTable(x)
generateCode(test3, 'test3')

print("\nTest 4:")
t = yacc.parse(test4)
getSymbolTable(x)
generateCode(test4, 'test4')

print("\nTest 5:")
t = yacc.parse(test5)
getSymbolTable(x)
generateCode(test5, 'test5')

print("\nTest 6:")
t = yacc.parse(test6)
getSymbolTable(x)
generateCode(test6, 'test6')
