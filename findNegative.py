arr = [[-1,-1,2,3],
		[-1,2,3,4],
		[2,-3,4,5]]
		
aSize = len(arr)
eleSize = len(arr[0])
count = 0

for i in range(aSize):
	for j in range(eleSize):
		if(arr[i][j] < 0):
			count = count + 1
print(count)			