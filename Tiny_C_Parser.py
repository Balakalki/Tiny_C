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
    @_('declaration_stmt','assignment_stmt','print_stmt')
    def statement(self,value):
        return value[0]
    @_('type list_of_variables')
    def declaration_stmt(self,value):
        for val in value[1]:
            if self.stable.nameInSymbolTable(val.symbolEntry)==False:
                v =SymbolTableEntry(val.symbolEntry,value[0])
                # lst.append(NameAst(v))
                # self.stable.addSymbol(v)
                self.stable.addSymbol(v)
            else:
                print(f"Error: redeclaration of '{val.symbolEntry}'")
    @_('ID "," list_of_variables')
    def list_of_variables(self,value):
        return [NameAst(value[0])] + value[2]
    @_('ID')
    def list_of_variables(self,value):
        return [NameAst(value[0])]
    @_('ID "=" ID')
    def assignment_stmt(self,value):
        symentry=self.stable.getSymbolEntry(value[0])
        left=NameAst(symentry.name)
        symentry=self.stable.getSymbolEntry(value[2])
        right=NameAst(symentry.name)
        return AssignAst(left,right,0)
    @_('ID "=" CONST')
    def assignment_stmt(self,value):
        symentry=self.stable.getSymbolEntry(value[0])
        left=NameAst(symentry.name)
        return AssignAst(left,NumberAst(value[2]),0)
    @_('PRINT ID')
    def print_stmt(self,value):
        return PrintAst(NameAst(value[1]))
        # for i in self.stable.table:
        #     if i.name == value.ID:
        #         return PrintAst(i)
    @_('INT')
    def type(self,value):
        return DataType.INT
    @_('CONST')
    def assignment_stmt(self,value):
        value[0]=NumberAst(int(value[0]))
        return NumberAst(int(value[0]))
    
lexer = lex()
parser = parse()
expr='''int main()
{ 
    int y;
    int d,vijay_08,a,b,c;
    b=40;
    vijay_08=30; 
    print vijay_08;
    print a;
}'''
obj = parser.parse(lexer.tokenize(expr))
obj.print()
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
