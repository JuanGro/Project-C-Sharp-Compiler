from parser import *
from generate_code import *

def getSymbolTable(x):
    symbolTable = []
    if len(x) > 0:
        dictionary = {}
        for element in x:
            if element == 'int' or element == 'bool' or element == 'string':
                dictionary['type'] = element
                dictionary['name'] = ""
                if element == 'int':
                    dictionary['value'] = 0
                elif element == 'bool':
                    dictionary['value'] = 'true'
                else:
                    dictionary['value'] = '""'
                symbolTable.append(dictionary)
            elif element == 'true' or element == 'false' or str(element).isnumeric() == True or '"' in element:
                if 'type' in dictionary.keys():
                    if element == 'true' or element == 'false':
                        if dictionary['type'] == 'bool':
                            dictionary['value'] = element
                        else:
                            print("ERROR WHEN ASSIGN VALUE")
                            return 'Error'
                    elif str(element).isnumeric() == True:
                        if dictionary['type'] == 'int':
                            dictionary['value'] = element
                        else:
                            print("ERROR WHEN ASSIGN VALUE")
                            return 'Error'
                    elif '"' in element:
                        if dictionary['type'] == 'string':
                            dictionary['value'] = element
                        else:
                            print("ERROR WHEN ASSIGN VALUE")
                            return 'Error'
            elif element == ';':
                dictionary = {}
            else:
                if not any(d['name'] == element for d in symbolTable):
                    dictionary['name'] = element
                    if 'type' not in dictionary:
                        print(element, "not initialized")
                        emptyTerminals(x)
                        return 'error'
        emptyTerminals(x)
        if twoDeclarations(symbolTable) == True:
            print("Declaration repeated")
            return 'error'
        else:
            printSymbolTable(symbolTable)
            return 0

def printSymbolTable(symbolTable):
    if len(symbolTable) > 0:
        print("ID" + "\t" + "|" + "Type" + "\t" + "|" + "Value")
        for element in symbolTable:
            print(element['name'] + "\t" + "|" + element['type'] + "\t" + "|" + str(element['value']))

def twoDeclarations(symbolTable):
    for element in symbolTable:
        if element['name'] == '':
            return True
    return False
