from sly import Lexer

class lex(Lexer):
    literals = {";","=","\n","==","+","-","*","/","%","!",",","(",")","{","}","[","]","<",">","."}
    ignore = " \n\t"
    tokens = {"ID","INT","PRINT","CONST"}
    CONST = r'[0-9]+'
    ID = r'[a-zA-Z][a-zA-Z_0-9]*'
    ID ['print'] = PRINT 
    ID ['int'] = INT
    def CONST(self,t):
        t.value=int(t.value)
        return t


# Level1  of Tiny C:

# a) Program consists of only one function main()
# b) Keywords  :   int, print
# c) Datatypes :  int 
# d) Identifiers :  starts with letter followed by one or more digits or underscore
# e) The statements  allowed are  declaration statement, assignment statement, print statement 
# f) Print syntax:   print identifier
