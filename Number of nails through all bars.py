n = int(input())
llist = []
count = 1

for i in range(n): #O(n)
	a, b = map(int,input().split())
	llist.append([a, b])

llist.sort(key=lambda x : [x[1], x[0]]) #끝점을 기준으로 오름차순 정렬을 한 후, 같을 경우 시작점을 따라 오름차순 정렬을 합니다. 끝점을 기준으로 오른차순 정렬을 했기 떄문에, 이 막대 이후에 끝점은 그 전의 막대의 끝점보다 무조건 크거나 같게 됩니다. #O(nlogn)

last = llist[0][1] #끝점이 가장 작은 것중에, 시작점이 가장 작은 막대를 last라고 정의합니다. 

for i in range(1,n): #O(n)
	if last < llist[i][0]:
		last = llist[i][1]
		count += 1
#앞의 과제에서 설명한 것과 같이 한 막대의 끝점이 다른 막대의 시작점과 같거나 크다면, 두 막대는 겹친다고 볼 수 있습니다. last는 둘이 겹칠 때마다 새로 갱신되는 막대의 끝점이고, count는 못의 개수입니다. 뒤의 막대는 위에서 정렬한 것과 같이 반드시 끝점이 크거나 같으므로 갱신을 한다고 해서 모순은 생기지 않습니다. 

print(count)

#따라서 총 수행시간은 O(nlogn)이 됩니다. 