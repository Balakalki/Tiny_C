from sly import Parser
from Ast import *
from Function import *
from Program import *
from SymbolTable import *
from Tiny_C_Lexer import lex
class parse(Parser):
    tokens = lex.tokens 
    literals = lex.literals
    stable=SymbolTable()
    precedence = (('left','='),('left','+','-'),('left','*','/'))
    @_('return_type ID "(" ")" "{" statements "}" ')
    def program(self,value):
        prog = Program()
        fun = Function(value.return_type,value.ID)
        fun.setStatementsAstList(value.statements)
        fun.setLocalSymbolTable(self.stable.table)
        prog.addFunctionDetails(value[1],fun)
        if prog.getMainFunction() is None:
            print("Error: main function is not defined")
        return prog
    @_('INT')
    def return_type(self,value):
        return value[0]
    @_('statement ";" statements')
    def statements(self,value):
        return [value[0]] + value[2]
    @_('statement ";"')
    def statements(self,value):
        return [value[0]]
    @_('declaration_stmt','assignment_stmt','print_stmt','expr')
    def statement(self,value):
        return value[0]
    @_('type list_of_variables')
    def declaration_stmt(self,value):
        for val in value[1]:
            if self.stable.nameInSymbolTable(val.symbolEntry)==False:
                v =SymbolTableEntry(val.symbolEntry,value[0])
                self.stable.addSymbol(v)
            else:
                print(f"Error: redeclaration of '{val.symbolEntry}'")
    @_('ID "," list_of_variables')
    def list_of_variables(self,value):
        return [NameAst(value[0])] + value[2]
    @_('ID')
    def list_of_variables(self,value):
        return [NameAst(value[0])]
    # @_('ID "=" ID')
    # def assignment_stmt(self,value):
    #     symentry=self.stable.getSymbolEntry(value[0])
    #     left=NameAst(symentry.name)
    #     symentry=self.stable.getSymbolEntry(value[2])
    #     right=NameAst(symentry.name)
    #     return AssignAst(left,right,value.lineno)
    @_('ID "=" expr')
    def assignment_stmt(self,value):
        symentry=self.stable.getSymbolEntry(value[0])
        if symentry is not None:
            left=NameAst(symentry.name)
        else:
            print(f"Erro: {value[0]} is not declared at line {value.lineno}")
            left=NameAst(value[0])
        return AssignAst(left,value[2],value.lineno)
    @_('expr "+" expr')
    def expr(self,value):
        return PlusAst(value[0],value[2],value.lineno)
    @_('expr "-" expr')
    def expr(self,value):
        return MinusAst(value[0],value[2],value.lineno)
    @_('expr "*" expr')
    def expr(self,value):
        return MultAst(value[0],value[2],value.lineno)
    @_('expr "/" expr')
    def expr(self,value):
        return DivAst(value[0],value[2],value.lineno)
     
    @_('ID')
    def expr(self,value):
        v=self.stable.getSymbolEntry(value.ID)
        return NameAst(v.name)
    @_('CONST')
    def expr(self,value):
        return NumberAst(value[0])
    @_('PRINT ID')
    def print_stmt(self,value):
        return PrintAst(NameAst(value[1]))
    @_('INT')
    def type(self,value):
        return DataType.INT
    
    
lexer = lex()
parser = parse()
expr='''int main()
{ 
    int y;
    int d,vijay_08,a,b,c;
    vijay_08=b+10; 
    a=b*c;
    b=a/c;
    d=a-b;
    print vijay_08;
    print a;
}'''
obj = parser.parse(lexer.tokenize(expr))
obj.print()
#Level 1 grammer

# <program>  :=  <return_type><identifier>() {  <statements> }
# <return_type> :=  int
# <statements> :=  <statement>; <statements> | <statement>;
# <statement> := <declaration_stmt> |  <assignment_stmt> | <print_stmt> | expr
# <expr> := <expr> + <expr> | <expr> - <expr> | <expr> * <expr> | <expr> / <expr> | <constant>
# <declaration_stmt> := <type> <list_of_variables>
# <list_of_variables> := <identifier> , <list_of_variables> |  <identifier>
# <assignment_stmt> := <identifier> = <identifier>  |  <identifier> = <constant>
# <print_stmt>            :=  print <identifier>
# <type>                     :=  int

# <identifier>   rule is similar to C
# <constant>  integer constant rule is similar to C
