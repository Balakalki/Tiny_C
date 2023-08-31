from sly import Parser
from Tiny_C_Lexer import lex
class parse(Parser):
    tokens = lex.tokens 
    literals = lex.literals
    memory = {}
    var_list = []
    @_('return_type ID "(" ")" "{" statements "}" ')
    def program(self,value):
        print("accepted")
    @_('INT')
    def return_type(self,value):
        pass
    @_('statement ";" statements')
    def statements(self,value):
        pass
    @_('statement ";"')
    def statements(self,value):
        pass
    @_('declaration_stmt')
    def statement(self,value):
        pass
    @_('assignment_stmt')
    def statement(self,value):
        pass
    @_('print_stmt')
    def statement(self,value):
        pass
    @_('type list_of_variables')
    def declaration_stmt(self,value):
        pass
    @_('ID "," list_of_variables')
    def list_of_variables(self,value):
        pass
    @_('ID')
    def list_of_variables(self,value):
        pass
    @_('ID "=" ID')
    def assignment_stmt(self,value):
        pass
    @_('ID "=" CONST')
    def assignment_stmt(self,value):
        pass
    @_('PRINT ID')
    def print_stmt(self,value):
        pass
    @_('INT')
    def type(self,value):
        pass
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
