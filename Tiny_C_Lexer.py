from sly import Lexer

class lex(Lexer):
    literals = {";","=","\n","==","+","-","*","/","%","!",",","(",")","{","}","[","]","<",">","."}
    ignore = " \t"
    tokens = {"ID","INT","PRINT","CONST","DOUBLE","FLOAT"}
    CONST = r'[0-9]+'
    ID = r'[a-zA-Z][a-zA-Z_0-9]*'
    ID ['print'] = PRINT 
    ID ['int'] = INT
    ID ['double'] = DOUBLE
    FLOAT = r'[0-9]+.[0-9][0-9]'
    def CONST(self,t):
        t.value=int(t.value)
        return t
    def FLOAT(self,t):
        t.value=float(t.value)
        return t
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1



# Level1  of Tiny C:

# a) Program consists of only one function main()
# b) Keywords  :   int, print
# c) Datatypes :  int 
# d) Identifiers :  starts with letter followed by one or more digits or underscore
# e) The statements  allowed are  declaration statement, assignment statement, print statement 
# f) Print syntax:   print identifier
