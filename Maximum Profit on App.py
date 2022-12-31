
def maximumProfit(arr):
	J=0
	# print(arr)
	arr.sort()
	num = len(arr)
	for i in arr:
		# print(i)
		if J< i*num:
			J = i*num
		num-=1
		# print(J)
    		# num-=1

	return J





n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)
