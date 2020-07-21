arr = [[1,1,1,1,1],
		[2,2,2,2,2],
		[3,3,3,3,3],
		[4,4,4,4,4],
		[5,5,5,5,5]]
		
k = 3
n = 5

for i in range(n - k + 1):
	for j in range(n - k + 1):
		s = 0
		
		for p in range(i , k + i):
			for q in range(j , k + j):
				s = s + arr[i][j]
	
		print(str(s) + " ")
	print("/n")