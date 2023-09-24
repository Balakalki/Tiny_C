from sly import Parser
from Ast import *
from Function import *
from Program import *
from SymbolTable import *
from Tiny_C_Lexer import lex
from argparse import *
class parse(Parser):
    tokens = lex.tokens 
    literals = lex.literals
    stable=SymbolTable()
    precedence = (('left','='),('left','+','-'),('left','*','/'))
    @_('return_type ID "(" ")" "{" statements "}" ')
    def program(self,value):
        prog = Program()
        fun = Function(value.return_type,value.ID)
        lst=[]
        for i in value.statements:
            if i is not None:
                lst.append(i)
        fun.setStatementsAstList(lst)
        fun.setLocalSymbolTable(self.stable)
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
        return [NameAst(value[0],self.stable)] + value[2]
    @_('ID')
    def list_of_variables(self,value):
        return [NameAst(value[0],self.stable)]
    @_('ID "=" expr')
    def assignment_stmt(self,value):
        symentry=self.stable.getSymbolEntry(value[0])
        if symentry is not None and value[2] is not None:
            left=NameAst(symentry.name,self.stable)
            ass=AssignAst(left,value[2],value.lineno)
            if ass.typeCheckAST()==True:
                return ass
        else:
            print(f"Erro: at line {value.lineno} \n {value[0]} is not declared ")
            left=NameAst(value[0],self.stable)
    @_('expr "+" expr')
    def expr(self,value):
        if value[0] is not None and value[2] is not None:
            return PlusAst(value[0],value[2],value.lineno)
    @_('expr "-" expr')
    def expr(self,value):
        if value[0] is not None and value[2] is not None:
            return MinusAst(value[0],value[2],value.lineno)
    @_('expr "*" expr')
    def expr(self,value):
        if value[0] is not None and value[2] is not None:
            return MultAst(value[0],value[2],value.lineno)
    @_('expr "/" expr')
    def expr(self,value):
        if value[0] is not None and value[2] is not None:
            return DivAst(value[0],value[2],value.lineno)
     
    @_('ID')
    def expr(self,value):
        if self.stable.getSymbolEntry(value[0]) is not None:
            v=self.stable.getSymbolEntry(value.ID)
            return NameAst(v.name,self.stable)
        else:
            print(f"Error: at line {value.lineno} \n {value[0]} is not declared")
    @_('CONST')
    def expr(self,value):
        return NumberAst(value[0])
    @_('FLOAT')
    def expr(self,value):
        return NumberAst(value[0])
    @_('PRINT ID')
    def print_stmt(self,value):
        return PrintAst(NameAst(value[1],self.stable))
    @_('INT')
    def type(self,value):
        return DataType.INT
    @_('DOUBLE')
    def type(self,value):
        return DataType.DOUBLE
    
    
lexer = lex()
parser = parse()
# expr='''int main()
# { 
#     int d,vijay_08,a,b,c;
#     b=10;
#     a=b;
#     vijay_08=b+c; 
#     y=b*c;
#     b=a/c;
#     d=a-b;
#     print vijay_08;
#     print a;
# }'''
agparse = ArgumentParser()
agparse.add_argument("input_file",help="input_file")
agparse.add_argument("-TinyC",help="TinyC")
agparse.add_argument("file",help="file_name")
args=agparse.parse_args()
input=open(args.input_file,"r")
if args.TinyC == "lex":
    f=open(args.file,"w")
    for token in lexer.tokenize(input.read()):
        f.write(f"token name = {token.value} token type = {token.type}\n")
elif args.TinyC == "parse":
    obj = parser.parse(lexer.tokenize(input.read()))
    if obj is None:
        print("not Accepted")
    else:
        print("Accepted")
elif args.TinyC == "ast":
    obj = parser.parse(lexer.tokenize(input.read()))
    if obj is not None:
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
