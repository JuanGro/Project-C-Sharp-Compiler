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
    completeFilename = 'output/' + filename + '.py'
    f = open(completeFilename, 'w')
    f.write(code)

    with open(completeFilename) as f:
        solveConflicts(f, completeFilename)


def solveConflicts(f, filename):
    newCode = ""
    for line in f:
        if len(line.split(" ")) > 2:
            if 'if' in line or 'while' in line:
                line = line.replace('\n', '')
                line += ':\n'
            newCode += line
    f = open(filename, 'w')
    f.write(newCode)
