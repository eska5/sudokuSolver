from pyswip import Prolog
import numpy as np

prolog = Prolog()

prolog.consult("sudoku.pl")

def py2pl(var):
    if type(var) is list:
        lst_string = ','.join(map(lambda item: '_' if item is None else str(item), var))
        return '[' + lst_string + ']'



def SudokuRecursionV(x,y,sudokuMapTwo,xp,yp):
	if x == 9:
		for p in range(9):
			print(sudokuMapTwo[p])
		print("------")
		return
	if sudokuMapTwo[x][y] == 0:
		squareList = [0]*9
		for i in range(3):
			for j in range(3):
				squareList[(i*3)+j]=sudokuMapTwo[(x//3*3)+i][(y//3*3)+j]
		for Z in range(1,10):
			counter = 3
			queries = [
				f'not_in_list({Z}, {py2pl(sudokuMapTwo[x])})',
				f'not_in_list({Z}, {py2pl([row[y] for row in sudokuMapTwo])})',
				f'not_in_list({Z}, {py2pl(squareList)})',
			]
			for query in queries:
				if bool(list(prolog.query(query))) == True:
					counter = counter - 1

			if counter == 0:
				sudokuMapTwo[x][y] = Z
				#for p in range(9):
				#	print(sudokuMapTwo[p])
				#print("------",{Z},{x},{y})
				if y==8:
					SudokuRecursionV(x+1,0,sudokuMapTwo,x,y)
				else:
					SudokuRecursionV(x,y+1,sudokuMapTwo,x,y)
		sudokuMapTwo[x][y]=0
		sudokuMapTwo[xp][yp] = 0
	else:
		if y == 8:
			SudokuRecursionV(x + 1, 0, sudokuMapTwo, xp, yp)
		else:
			SudokuRecursionV(x, y + 1, sudokuMapTwo, xp, yp)



#main

sudokuMap = [
[0, 0, 0, 0, 0, 0, 0, 2, 3],
[0, 0, 0, 0, 9, 6, 1, 0, 0],
[0, 5, 0, 0, 0, 0, 7, 0, 0],
[3, 4, 0, 5, 0, 2, 0, 7, 0],
[2, 0, 0, 7, 0, 8, 0, 3, 6],
[0, 0, 0, 0, 3, 0, 0, 0, 0],
[0, 0, 1, 9, 8, 0, 0, 0, 0],
[6, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 7, 0, 0, 0, 0, 0, 5],
]

SudokuRecursionV(0,0,sudokuMap,0,0)