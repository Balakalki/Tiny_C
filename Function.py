from Ast import *
from SymbolTable import SymbolTable
class Function:
	def __init__(self, returnType, name):
		self.returnType = returnType
		self.name       = name
		self.statementsAstList = []
		self.localSymbolTable = SymbolTable()
	def setStatementsAstList(self, sastList):
		self.statementsAstList = sastList
	def getStatementsAstList(self):
		return self.statementsAstList
	def setLocalSymbolTable(self,localList):
		self.localSymbolTable = localList
	def getLocalSymbolTable(self):
		return self.localSymbolTable
	def print(self):
		print(f"function name: {self.name} function return type: {self.returnType} body:")
		for statement in self.getStatementsAstList():
			if type(statement)==list:
				for j in statement:
					if type(j)==DataType:
						print("    ",j)
					elif type(j)==NameAst:
						j.print()
			elif type(statement) == AssignAst:
				print("  statement:  ",statement.print())
			elif type(statement) == PrintAst:
				statement.print()
	