from semantic import *

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
console.writeline(number2);
'''
test4 = '''
bool FLAG = true;
console.writeline(FLAG);
'''
test5 = '''
console.writeline("Hi");
'''
test6 = '''
int number3 = 7;
bool flag2 = false;
string name1 = "Juan";

console.writeline(number3);
console.writeline(flag2);
console.writeline(name1);
'''
test7 = '''
int number1 = 0;
bool flag = false;

while(number1 <= 50) {
    number1 = number1 + 1;
    if(number1 == 35) {
        flag = true;
        if (number1 == 35) {
            flag = true;
        }
    }
    else {
        flag = false;
    }
    console.writeline(number1);
}
console.writeline(flag);
'''
test8 = '''
console.readline();
console.writeline("Hello World!");
'''
test9 = '''
bool flag = false;
int number1 = 3 + 4 * 5;
name2 = "Carlos";

if(number1 == 35) {
    // flag = true;
    number1 = "hi";
}
else {
    flag = false;
}

/*
while(number1 <= 50) {
    number1 = number1 + 1;
}
*/

string sentence_aux = "Result";
console.writeline(sentence_aux);
console.writeline(number1);
'''
test10 = '''
flag = false;
bool flag;
int a;
;
'''
test11 = '''
"Hello World" = 2;
console.writeline(int number1);
console.writeline(int number_Aux2);
'''
test12 = '''
int number3 = 0;

while false {
    number3 = number3 + 1;
}
'''
test13 = '''
0 = number2;

if (CONSTANT > 2) {
    console.writeline("YES");
}
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

print("\nTest 7:")
t = yacc.parse(test7)
getSymbolTable(x)
generateCode(test7, 'test7')

print("\nTest 8:")
t = yacc.parse(test8)
getSymbolTable(x)
generateCode(test8, 'test8')

print("\nTest 9:")
t = yacc.parse(test9)
getSymbolTable(x)
generateCode(test9, 'test9')

print("\nTest 10:")
t = yacc.parse(test10)
getSymbolTable(x)
generateCode(test10, 'test10')

print("\nTest 11:")
t = yacc.parse(test11)
getSymbolTable(x)
generateCode(test11, 'test11')

print("\nTest 12:")
t = yacc.parse(test12)
getSymbolTable(x)
generateCode(test12, 'test12')

print("\nTest 13:")
t = yacc.parse(test13)
getSymbolTable(x)
generateCode(test13, 'test13')
