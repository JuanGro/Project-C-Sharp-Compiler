tokensDictionary = {
    'if' : 'if',
    'else' : 'else:',
    'while' : 'while',
    'int' : '',
    'bool' : '',
    'string' : '',
    'console' : 'print',
    'writeline' : '',
    'readline' : '',
    'true' : 'True',
    'false' : 'False',
    '||' : 'or',
    '&&' : 'and'
}

symbolsDictionary = {
    '(' : ' ',
    ')' : ' ',
    '{' : ' ',
    '}' : ' ',
    ';' : ' ',
    '.' : ' ',
}

def generateCode(test, filename):
    code = ""
    testAux = ""

    for element in test:
        if element in symbolsDictionary:
            testAux += symbolsDictionary[element]
        else:
            testAux += element

    # print("e:",testAux.replace('\n', '\n ').split(' '))
    for element in testAux.replace('\n', '\n ').split(' '):
        if element.replace('\n', '') in tokensDictionary:
            if tokensDictionary[element] != '':
                code += tokensDictionary[element] + " "
            else:
                code += tokensDictionary[element]
        elif element == '\n' or element == '\t':
            code += element
        elif element == '':
            code += " "
        else:
            code += element + " "
    f = open('output/' + filename + '.py', 'w')
    f.write(code)
