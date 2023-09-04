
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
		print("  ",self.value)
	def getDataType(self):
		return type(self.value)
	def typeCheckAST(self):
		pass


class NameAst(AST):
	def __init__(self, symbolEntry):
		self.symbolEntry = symbolEntry
	def print(self):
		self.symbolEntry.print()
	def getDataType(self):
		return self.symbolEntry.getDataType()
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
		return f"Assignment: {self.left} = {self.right} (Line {self.lineNo})"
	
class PrintAst(AST):
	def __init__(self,symbolEntry):
		self.symbolEntry= symbolEntry
	def print(self):
		self.symbolEntry.print()
	def getDataType(self):
		pass
	def typeCheckAST(self):
		pass



