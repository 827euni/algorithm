n = int(input())
llist = []
last = []
count = 1

for i in range(n): #O(n)
	a, b = map(int,input().split())
	llist.append([a, b])

llist.sort(key=lambda x : [x[0], x[1]]) #시작점을 기준으로 오름차순 정렬을 한 후, 같을 경우 끝점을 기준으로 오름차순 계산을 합니다.  #O(nlogn) 
last.append(llist[0][1]) #llist[0][1]은 시작점이 가장 작으며, 그 중에서도 끝점이 가장 작은 점이다. 
#O(1)
for i in range(1,n): #O(n)
	if last[0] < llist[i][0]:
		last.sort(reverse=True) #내림차순으로 정렬 후, 마지막 끝점이 가장 큰 값을 제거합니다. O(nlogn)
		del last[-1] #O(1)
	last.sort() 
	last.append(llist[i][1]) #O(1)
#끝점을 기준으로 끝점이 시작점보다 크거나 같다면 막대들은 겹쳐져있는 상태이고, 끝점이 시작점보다 작으면 막대들은 겹치지 않는 것이다.last[0]은 시작점이 가장 작은 것중에, 끝점이 가장 작은 점이므로 그것보다 시작점이 작다면, 막대는 서로 겹치는 상태인 것이다. 
	count = max(count, len(last))
	#count를 매순간 가장 큰 값으로 갱신해나가면서, 최종적으로 count에는 최대값이 저장되게 됩니다. 
print(count)

#최종 수행시간은 O(n^2logn)이 된다. 