from parser import *

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
console.writeline("Hi");
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

string sentence_aux = "Result";
console.writeline(sentence_aux);
console.writeline(number1);
'''
test10 = '''
flag = false;
bool flag;
'''
test11 = '''
// "Hello World";
console.writeline(int number1);
console.writeline(int number_Aux2);
'''
test12 = '''
int number3 = 0;

while true {
    number3 = number3 + 1;
}
'''

# Check tests
# print("\nTest 1:")
print("\nTest 1:", test1)
yacc.parse(test1)
# print("\nTest 2:")
print("\nTest 2:", test2)
yacc.parse(test2)
# print("\nTest 3:")
print("\nTest 3:", test3)
yacc.parse(test3)
# print("\nTest 4:")
print("\nTest 4:", test4)
yacc.parse(test4)
# print("\nTest 5:")
print("\nTest 5:", test5)
yacc.parse(test5)
# print("\nTest 6:")
print("\nTest 6:", test6)
yacc.parse(test6)
# print("\nTest 7:")
print("\nTest 7:", test7)
yacc.parse(test7)
# print("\nTest 8:")
print("\nTest 8:", test8)
yacc.parse(test8)
# print("\nTest 9:")
print("\nTest 9:", test9)
yacc.parse(test9)
# print("\nTest 10:")
print("\nTest 10:", test10)
yacc.parse(test10)
# print("\nTest 11:")
print("\nTest 11:", test11)
yacc.parse(test11)
# print("\nTest 12:")
print("\nTest 12:", test12)
yacc.parse(test12)
