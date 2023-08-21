from sly import Lexer

class lex(Lexer):
    literals = (";","=","==","+","-","*","/","%","!",",","(",")","{","}","[","]","<",">",".")
    ignore = " "
    tokens = ("ID","INT","PRINT")
    INT = r'[0-9]+'
    ID = r'[a-zA-Z][a-zA-Z_]*'
    ID ['print'] = PRINT 
obj = lex()
expr = input("enter tiny c code");
for token in obj.tokenize(expr):
    print(f'token type = {token.type} token value = {token.value}')