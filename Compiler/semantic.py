from parser import *

def getSymbolTable(x):
    symbolTable = []
    if len(x) > 0:
        dictionary = {}
        for element in x:
            if element == 'int' or element == 'bool' or element == 'string':
                dictionary['type'] = element
                dictionary['name'] = ""
                dictionary['value'] = 0
                symbolTable.append(dictionary)
            elif element == 'true' or element == 'false' or str(element).isnumeric() == True or '"' in element:
                dictionary['value'] = element
            elif element == ';':
                dictionary = {}
            else:
                if not any(d['name'] == element for d in symbolTable):
                    dictionary['name'] = element
                # else:
                #     print("Error, variable already declared")
                #     symbolTable.pop()
        if twoDeclarations(symbolTable) == True:
            print("Declaration repeated")
        else:
            printSymbolTable(symbolTable)

def printSymbolTable(symbolTable):
    print("ID" + "\t" + "|" + "Type" + "\t" + "|" + "Value")
    for element in symbolTable:
        print(element['name'] + "\t" + "|" + element['type'] + "\t" + "|" + str(element['value']))

def twoDeclarations(symbolTable):
    for element in symbolTable:
        if element['name'] == '':
            return True
    return False
