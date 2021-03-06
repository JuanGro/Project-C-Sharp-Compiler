from lex import *

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
console.writeline("Hello World!");
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
console.readline();
console.writeline("Hello World!");
'''
test9 = '''
bool flag = false;
int number1 = 3 + 4 * 5;
name2 = "Carlos";

if(number1 == 35) {
    // flag = true;
    number1 = console.readline();
} else {
    flag = false;
}

/*
while(number1 <= 50) {
    number1 = number1 + 1;
}
*/

string SENTENCE_AUX = "Result";
console.writeline(SENTENCE_AUX);
console.writeline(number1);
'''
test10 = '''
flag = false;
bool flag;
'''
test11 = '''
"Hello World";
console.writeline(int NUMBER1);
console.writeline(int number_Aux2);
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
