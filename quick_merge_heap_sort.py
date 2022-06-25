import random, timeit #, sys

#sys.setrecursionlimit(10**9) 
#다양한 n에 대한 그래프를 그리기 위하여, 재귀함수 호출 한계선을 재설정하였습니다.

def quick_sort(A, first, last):
	global Qc, Qs
	
	Qc += 1
	if first>=last: 
		return 
	left, right = first + 1, last
	pivot = A[first]
	
	Qc += 1
	while left <= right:
		
		Qc += 1
		while left<=last and A[left] < pivot:
			Qc += 1
			left+=1
			
		Qc += 1
		while right>first and A[right] > pivot:
			Qc += 1
			right -=1
		
		Qc += 1
		if left <= right:
			A[left], A[right] = A[right], A[left]
			Qs+=1
			left +=1
			right -=1

	Qs += 1
	A[first], A[right] = A[right], A[first]
	quick_sort(A, first, right-1)
	quick_sort(A, first+1, last)
	

def merge_sort(A, first, last):
	global Mc, Ms
	if first >= last:
		Mc += 1
		return 
	merge_sort(A, first, (first+last)//2)
	merge_sort(A, (first+last)//2+1, last)
	merge_two_sorted_lists(A, first, last)
	
def merge_two_sorted_lists(A, first, last):
	global Mc, Ms
	m = (first + last) //2
	i, j = first, m+1
	B = []
	
	Mc += 1
	while i<=m and j<= last:
		
		Mc += 1
		if A[i] <= A[j]:
			Ms += 1
			B.append(A[i])
			i += 1
			
		else:
			Ms += 1
			B.append(A[j])
			j += 1
	
	for k in range(i,m+1):
		Ms += 1
		B.append(A[k])
		
	for k in range(j, last + 1):
		Ms += 1
		B.append(A[k])
		
	for i in range(first, last+1):
		Ms += 1
		A[i] = B[i-first]
			

def heap_sort(A):
	global Hc, Hs
	n = len(A)
	make_heap(A)
	
	for i in range(len(A)-1, -1, -1):
		Hs += 1
		A[0], A[i] = A[i], A[0]
		n -= 1
		heapify_down(A,0,n)

def make_heap(A):
	n = len(A)
	for k in range(n-1,-1,-1): 
		heapify_down(A, k, n)
	
def heapify_down(A, k, n):
	global Hc, Hs
	
	Hc += 1
	while 2*k+1<n:
		L, R = 2*k + 1, 2*k+2
		
		Hc += 1
		if L<n and A[L] > A[k]:
			m = L
		else:
			m = k
			
		Hc += 1
		if R<n and A[R]> A[m]:
			m = R
		
		Hc += 1
		if m != k:
			Hs += 1
			A[k], A[m] = A[m], A[k]
			k = m
		
		else :
			break
	
def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))