from sly import Parser
from Tiny_C_Lexer import lex
class parse(Parser):
    tokens = lex.tokens 
    literals = lex.literals
    memory = {}
    @_('return_type ID "(" ")" "{" statements "}" ')
    def program(self,value):
        return value[5]
    @_('INT')
    def return_type(self,value):
        return value[0]
    @_('statement ";" statements')
    def statements(self,value):
        return value[2]
    @_('statement ";"')
    def statements(self,value):
        return value[0]
    @_('declaration_stmt')
    def statement(self,value):
        return value[0]
    @_('assignment_stmt')
    def statement(self,value):
        return value[0]
    @_('print_stmt')
    def statement(self,value):
        return value[0]
    @_('type list_of_variables')
    def declaration_stmt(self,value):
        return value[1]
    @_('ID "," list_of_variables')
    def list_of_variables(self,value):
        return value[0]
    @_('ID')
    def list_of_variables(self,value):
        return value[0]
    @_('ID "=" ID')
    def assignment_stmt(self,value):
        self.memory[value[0]] = self.memory[value[2]]
    @_('ID "=" CONST')
    def assignment_stmt(self,value):
        self.memory[value[0]] = value[2]
    @_('PRINT ID')
    def print_stmt(self,value):
        print(self.memory[value[1]])
    @_('INT')
    def type(self,value):
        return value[0]
    @_('CONST')
    def assignment_stmt(self,value):
        return int(value[0])
    
lexer = lex()
parser = parse()
expr='''int main()
{ 
    int a;
    b=40;
    a=30; 
    print a;
    print b;
}'''
parser.parse(lexer.tokenize(expr))