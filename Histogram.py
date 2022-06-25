def error(start, last):
	FinalRsum = Rsum[last] - Rsum[start-1]
	FinalSqsum = Sqsum[last] - Sqsum[start-1]
	error = FinalSqsum - (FinalRsum**2)/(last-start+1)
	return error

def final(B, n): # 그룹이 3개 일 때, j는 1부터 n까지, k역시도 1부터 n-2까지 진행해야하고, 이 모든 것은 B만큼 계속 곱해져야 하므로, O(B*n^2)이 되어야만 한다. 
	for i in range(2, B+1): #그룹은 2개에서부터 B개까지만 만들 수 있다. 
		for j in range(1, n+1): 
			for k in range(1, j): 
				# 마지막 그룹에서 첫번째의 숫자가 k일 때, 원래의 오차의 합과 k부터 j-1까지의 합에 마지막 오차를 더하는 것 중 작은 값이다. 
				minn[i][j] = min(minn[i][j], minn[i-1][k] + error(k+1, j)) 
	return minn[B][n]

B, n = map(int, input().split())
A = [0]
Rsum = [0] * (n+1)
Sqsum = [0] * (n+1)
minn = [] #minn[i][j]는 1부터 j-1까지 i개의 그룹으로 만들어지는 최소 오차값

for i in range(1,n+1):
	A.append(int(input()))
	Rsum[i] = Rsum[i-1] + A[i]
	Sqsum[i] = Sqsum[i-1] + A[i]**2
	
for _ in range(B+1):
	minn.append([100000000000000000000]*(n+1)) # 계속 최솟값을 찾아내야 하기 때문에, 최초 최소값은 절대 도달할 수 없을 것 같은 큰 값을 집어넣었습니다. 

	
for i in range(1,n+1): #min의 최초조건 기입.
	minn[1][i] = error(1, i)
	
print(round(final(B,n),3))

# 만약 A에 들어있는 개수가 2라고 할 때, 
# 평균 = (a+b+c) / 2
# 오차 = (평균 - a)^2 + (평균 - b)^2 이고 평균을 m이라고 치환하면,
		#  m^2 - 2am + a^2 + m^2 - 2bm + b^2 
		#	 a^2 + b^2 + 2m^2 - 2m(a+b+c)
		# a + b = 2m이므로, a^2 + b^2 + - 2m^2
		# 따라서, 오차 = a^2 + b^2 + c^2 -(a+b+c)^2/2

# 만약 A에 들어있는 개수가 3이라고 할 때, 
# 평균 = (a+b+c) / 3
# 오차 = (평균 - a)^2 + (평균 - b)^2 +  + (평균 - c)^2 이고 평균을 m이라고 치환하면,
		#  m^2 - 2am + a^2 + m^2 - 2bm + b^2 + m^2 - 2cm + c^2
		#	 a^2 + b^2 + c^2 +3m^2 - 2m(a+b+c)
		# a + b + c = 3m이므로, a^2 + b^2 + c^2 - 3m^2
		# 따라서, 오차 = a^2 + b^2 + c^2 -(a+b+c)^2/3
# 즉, 최종 오차식은 (각 제곱의 합) -(각 항의 합)^2/(A에 들어있는 원소의 개수)

