def max_sum(A, left, right):

	if left == right:
		return A[left]
	mid = (left+right) // 2
		
	left_part = max_sum(A, left, mid)
	right_part = max_sum(A, mid+1, right)
	all_max = max(left_part, right_part)
		
	MIN = 0
	left_sum = 0
	partLeft = MIN
	for i in range(mid, left-1, -1):
		left_sum += A[i]
		partLeft = max(partLeft, left_sum)
		
	right_sum = 0
	partRight = MIN
	for j in range(mid+1, right+1, 1):
		right_sum += A[j]
		partRight = max(partRight, right_sum)
	return max(all_max, partLeft+partRight)

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)