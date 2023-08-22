from sly import Lexer

class lex(Lexer):
    literals = (";","=","\n","==","+","-","*","/","%","!",",","(",")","{","}","[","]","<",">",".")
    ignore = " \n"
    tokens = ("ID","INT","PRINT","CONST")
    CONST = r'[0-9]+'
    ID = r'[a-zA-Z][a-zA-Z_]*'
    ID ['print'] = PRINT 
    ID ['int'] = INT
obj = lex()