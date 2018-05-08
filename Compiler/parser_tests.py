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
int number1 = 0;
bool flag = false;

while(number1 <= 50) {
    number1 = number1 + 1;
    if(number1 == 35) {
        flag = true;
        if (number1 == 35) {
            flag = true;
        }
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
    number1 = "hi";
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

while true {
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
print(t.print_node())

print("\nTest 2:")
t = yacc.parse(test2)
print(t.print_node())

print("\nTest 3:")
t = yacc.parse(test3)
print(t.print_node())

print("\nTest 4:")
t = yacc.parse(test4)
print(t.print_node())

print("\nTest 5:")
t = yacc.parse(test5)
print(t.print_node())

print("\nTest 6:")
t = yacc.parse(test6)
print(t.print_node())

print("\nTest 7:")
t = yacc.parse(test7)
print(t.print_node())

print("\nTest 8:")
t = yacc.parse(test8)
print(t.print_node())

print("\nTest 9:")
t = yacc.parse(test9)
print(t.print_node())

print("\nTest 10:")
t = yacc.parse(test10)
print(t.print_node())

print("\nTest 11:")
t = yacc.parse(test11)
print(t.print_node())

print("\nTest 12:")
t = yacc.parse(test12)
print(t.print_node())

print("\nTest 13:")
t = yacc.parse(test13)
print(t.print_node())
