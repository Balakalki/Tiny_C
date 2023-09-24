
from enum import Enum
from abc import *
from SymbolTable import SymbolTable
from SymbolTable import SymbolTableEntry

DataType = Enum('DataType',['INT','DOUBLE'])

class AST(metaclass=ABCMeta):
	@abstractmethod
	def print(self):
		pass
	@abstractmethod
	def typeCheckAST(self):
		pass
	@abstractmethod
	def getDataType(self):
		pass

class NumberAst(AST):
	def __init__(self, number):
		self.value = number
	def print(self):
		print(f"Num:{self.value}",end="")
	def getDataType(self):
		return type(self.value)
	def typeCheckAST(self):
		pass


class NameAst(AST):
	def __init__(self, symbolEntry):
		self.symbolEntry = symbolEntry
	def print(self):
		print("Name:",self.symbolEntry,end="")
	def getDataType(self):
		return SymbolTable.getSymbolEntry(self.symbolEntry).getDataType()
	def typeCheckAST(self):
		pass
class AssignAst(AST):
	def __init__(self,left,right,lineNo):
		self.left = left
		self.right = right
		self.lineNo = lineNo
	def getDataType(self):
		pass
	def typeCheckAST(self):
		if(self.left.getDataType()== self.right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("\t\tAssign:")
		print("\t\t\tLHS (",end="")
		self.left.print()
		print(")")
		print("\t\t\tRHS (",end="")
		self.right.print()
		print(")")
	
class PrintAst(AST):
	def __init__(self,symbolEntry):
		self.symbolEntry= symbolEntry
	def print(self):
		print("\t\tPrint: ")
		print(f"\t\t\t",end="")
		self.symbolEntry.print()
		print()
	def getDataType(self):
		pass
	def typeCheckAST(self):
		pass
# class ArthimaticAst(AST):
# 	def __init__(self,left,right,oparator,lineno):
# 		self.left=left
# 		self.right=right
# 		self.oparator=oparator
# 		self.lineno=lineno
# 	def print(self):
# 		print("Arithmatic:")
# 		print("\t\t\t\tLHS (",end="")
# 		self.left.print()
# 		print(")")
# 		print("\t\t\t\toparator (",end="")
# 		print(self.oparator,end="")
# 		print(")")
# 		print("\t\t\t\tRHS (",end="")
# 		self.right.print()
# 		print(")",end= "")
# 	def getDataType(self):
# 		pass
# 	def typeCheckAST(self):
# 		if(self.left.getDataType() == self.right.getDataType()):
# 			return True
# 		else:
# 			return False
# class RelationAst(AST):
# 	def __init__(self,left,right,relation,lineno):
# 		self.left=left
# 		self.right=right
# 		self.relation=relation
# 		self.lineno=lineno
# 	def print(self):
# 		print("relation:")
# 		print("\t\t\t\tLHS (",end="")
# 		self.left.print()
# 		print(")")
# 		print("\t\t\t\trelation (",end="")
# 		print(self.oparator,end="")
# 		print(")")
# 		print("\t\t\t\tRHS (",end="")
# 		self.right.print()
# 		print(")",end= "")
# 	def getDataType(self):
# 		pass
# 	def typeCheckAST(self):
# 		if(self.left.getDataType() == self.right.getDataType()):
# 			return True
# 		else:
# 			return False
class PlusAst(AST):
	def __init__(self,left,right,lineNo):
		self.left=left
		self.right=right
		self.lineNo=lineNo
	def print(self):
		print("Plus:")
		print("\t\t\t\tLHS (",end="")
		self.left.print()
		print(")")
		print("\t\t\t\tRHS (",end="")
		self.right.print()
		print(")",end= "")
	def getDataType(self):
		pass
	def typeCheckAST(self):
		if(self.left.getDataType()==self.right.getDataType):
			return True
		else:
			return False
class MinusAst(AST):
	def __init__(self,left,right,lineNo):
		self.left=left
		self.right=right
		self.lineNo=lineNo
	def print(self):
		print("Minus:")
		print("\t\t\t\tLHS (",end="")
		self.left.print()
		print(")")
		print("\t\t\t\tRHS (",end="")
		self.right.print()
		print(")",end= "")
	def getDataType(self):
		pass
	def typeCheckAST(self):
		if(self.left.getDataType()==self.right.getDataType):
			return True
		else:
			return False
class MultAst(AST):
	def __init__(self,left,right,lineNo):
		self.left=left
		self.right=right
		self.lineNo=lineNo
	def print(self):
		print("Mult:")
		print("\t\t\t\tLHS (",end="")
		self.left.print()
		print(")")
		print("\t\t\t\tRHS (",end="")
		self.right.print()
		print(")",end= "")
	def getDataType(self):
		pass
	def typeCheckAST(self):
		if(self.left.getDataType()==self.right.getDataType):
			return True
		else:
			return False
class DivAst(AST):
	def __init__(self,left,right,lineNo):
		self.left=left
		self.right=right
		self.lineNo=lineNo
	def print(self):
		print("Div:")
		print("\t\t\t\tLHS (",end="")
		self.left.print()
		print(")")
		print("\t\t\t\tRHS (",end="")
		self.right.print()
		print(")",end= "")
	def getDataType(self):
		pass
	def typeCheckAST(self):
		if(self.left.getDataType()==self.right.getDataType):
			return True
		else:
			return False
class LessthanAst:
	def __init__(self,left,right,lineNo):
		self.left=left
		self.right=right
		self.lineNo=lineNo
	def print(self):
		print("\t\tLessthan:")
		print("\t\t\tLHS (",end="")
		self.left.print()
		print(")")
		print("\t\t\tRHS (",end="")
		self.right.print()
		print(")")
	def getDataType(self):
		pass
	def typeCheckAST(self):
		if(self.left.getDataType()==self.right.getDataType):
			return True
		else:
			return False
class GreaterthanAst:
	def __init__(self,left,right,lineNo):
		self.left=left
		self.right=right
		self.lineNo=lineNo
	def print(self):
		print("\t\tGreaterthan:")
		print("\t\t\tLHS (",end="")
		self.left.print()
		print(")")
		print("\t\t\tRHS (",end="")
		self.right.print()
		print(")")
	def getDataType(self):
		pass
	def typeCheckAST(self):
		if(self.left.getDataType()==self.right.getDataType):
			return True
		else:
			return False
