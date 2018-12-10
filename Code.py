import numpy as np

'''
In our board, 0 represents the missing numbers
or the blanks.
Python 2.7
'''

#finds whether x in arr or not
def find(x,arr):
	for i in arr:
		if x==i:
			return 1
	return 0

#finds intersection of two lists
def intersection(c1, c2): 
    lst3 = [filter(lambda x: x in c1, sublist) for sublist in c2]
    return lst3 

#counts number of zeros in our sudoko board
def countzero(arr):	
	ct = 0
	for i in range(9):
		for j in range(9):
			if arr[i][j][0]=='0':
				ct = ct+1
	return ct

#initializing main sudoko board
arr = [[i for i in range(9)] for i in range(9)]
arr = [[0,0,9,3,0,8,0,0,7],[2,3,0,0,5,0,0,8,4],[0,0,8,2,0,1,3,0,0],[0,2,6,0,3,0,0,5,8],[7,0,3,0,2,0,6,0,9],[1,0,5,9,0,4,0,2,0],[0,9,0,0,1,0,5,0,6],[0,5,0,4,0,6,0,7,0],[0,0,2,5,0,3,9,0,1]]
#Its better to initialize the board here itself.
print("INPUT BOARD : ")
print(np.matrix(arr))
print("**********************")
for i in range(0,9):
	for j in range(0,9):
		arr[i][j]= str(arr[i][j])

ct = countzero(arr)

#we have to solve till number of unknowns are not zero.
while(ct>0):
#getting 3X3 matrices from arr
	subarr = [[[str(0) for i in range(3)] for i in range(3)] for i in range(9)]
	m = -3
	n=0
	for i in range(9):
		if i%3==0:
			m=m+3
			n=0
		else:
			n=n+3
		for j in range(3):
			for k in range(3):
				subarr[i][j][k] = arr[j+m][k+n][0]
        
        
	subspace = [[str(i) for i in range(1,10)] for i in range(9)]
	for i in range(9):
		for j in range(3):
			for k in range(3):
				if find(subarr[i][j][k],subspace[i])==1:
					subspace[i].remove(subarr[i][j][k])
          
#core._._._._._.

	possibles = [[[str(x+1) for x in range(9)] for x in range(9)] for x in range(9)]


	copies = [[[str(0) for i in range(9)] for i in range(9)] for i in range(9)]
	q = 0
	m=-3
	n=0
	for i in range(9):
		if i%3==0:
			m=m+3
			n=0
		else:
			n=n+3
		for j in range(3):
			for k in range(3):
				copies[j+m][k+n]=subspace[i]
				
	#print(copies)
	#print(":::::::::::::::::::::::::::::::::::::::::::")
	trr = [i for i in range(1,10)]
	for k in range(9):
		for i in range(9):
			for j in range(9):
				if arr[i][j]=='0':
					for x in range(9):
						if find(arr[i][x],possibles[i][j]):
							possibles[i][j].remove(arr[i][x])
						if find(arr[x][j],possibles[i][j]):
							possibles[i][j].remove(arr[x][j])
					

	#print(possibles)

	for i in range(9):
		for j in range(9):
			#possibles[i][j] = intersection(possibles[i][j],subspace[i])
			if len(possibles[i][j])==9:
				for x in range(9):
					possibles[i][j][x]=[]
				for x in range(8):
					possibles[i][j].remove([])
			else:
				possibles[i][j] = [[n for n in lst if n in frozenset(copies[i][j])] for lst in possibles[i][j]]

	#print(possibles)
	#print("-------------------------------------------------")
	l = []
	
	for i in range(9):
		for j in range(9):
			if len(possibles[i][j])==1:
				if possibles[i][j][0]!=[]:
					arr[i][j]=possibles[i][j][0][0]
			elif (len(possibles[i][j])==possibles[i][j].count([])+1):
				for x in possibles[i][j]:
					if x!=[]:
						arr[i][j]=x[0]
	
	ct = countzero(arr)
	

print("SOLUTION -: ")
brr = [[i for i in range(9)]for j in range(9)]
for a in range(len(arr)):
	for b in range(9):
		brr[a][b] = int(arr[a][b][0])

print(np.matrix(brr))
