arr=[3,4,2,3,4,6,3]
print(arr)
n=len(arr)
for i in range(n-1):
	for j in range(i+1,n):
		if arr[i]==arr[j]:
			arr[j]=0

print(arr)