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
    int vijay_08;
    b=40;
    vijay_08=30; 
    print vijay_08;
    print b;
}'''
parser.parse(lexer.tokenize(expr))

#Level 1 grammer

# <program>  :=  <return_type><identifier>() {  <statements> }
# <return_type> :=  int
# <statements> :=  <statement>; <statements> | <statement>;
# <statement> := <declaration_stmt> |  <assignment_stmt> | <print_stmt>
# <declaration_stmt> := <type> <list_of_variables>
# <list_of_variables> := <identifier> , <list_of_variables> |  <identifier>
# <assignment_stmt> := <identifier> = <identifier>  |  <identifier> = <constant>
# <print_stmt>            :=  print <identifier>
# <type>                     :=  int

# <identifier>   rule is similar to C
# <constant>  integer constant rule is similar to C
