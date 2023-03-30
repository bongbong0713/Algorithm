import sys
import heapq

heap = []
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    s, t = map(int, input().split())
    arr.append([s, t])

arr.sort() #강의 시작시간이 빠른 순서로 정렬
heapq.heappush(heap, arr[0][1]) 
for i in range(1, n):
    if heap[0] > arr[i][0]: #heap에 있는 강의가 끝난 시간이 i번째 강의 시작시간보다 크면 다른 강의실을 잡아야함
        heapq.heappush(heap, arr[i][1]) #따라서 힙에 그 뒤 강의의 끝난 시간을 넣어줘서 heap에 강의실 개수를 추가해준다.
    else: #heap에 있는 강의가 끝난 시간이 i번째 강의 시작시간보다 작으면 다른 강의실을 잡을 필요가 없음
        heapq.heappop(heap) #따라서 힙에서 그 이전 강의를 pop해서 강의실 개수를 줄여주고 
        heapq.heappush(heap, arr[i][1]) #다음 강의의 끝난 시간을 넣어줘서 다음번 강의 시작시간과 비교할 수 있게 heap에 push해줌
print(len(heap)) #heap의 길이가 곧 필요한 강의실의 개수

#heap을 사용하지 않으면 시간초과 오류가 나는 문제 처음에 heap 자료구조를 사용하지 않아서 헤맸다
