#BFS로 풀었습니다
import sys
from collections import deque
ip = sys.stdin.readline
INF = int(1e9)

time = [INF] * 1000001
visited = [False] * 1000001

n,k = map(int,ip().split())

def sol(n,k) :
    if n == k : return 0 #n과 k가 같으면 같은 위치에 있는 것이므로 0
    queue = deque()
    queue.append(n)
    visited[n] = True
    time[n] = 0
    while queue :
        temp = queue.popleft()
        minus = temp - 1
        plus = temp + 1
        teleport = 2 * temp
        if temp == k : return time[temp]
        if 0 <= teleport and teleport <= 1000000 and not visited[teleport] : # 1번 조건문
            visited[teleport] = True
            time[teleport] = time[temp]
            queue.append(teleport)
        if 0 <= minus and minus <= 1000000 and not visited[minus] : # 2번 조건문
            visited[minus] = True
            time[minus] = time[temp] + 1
            queue.append(minus)
        if 0 <= plus and plus <= 1000000 and not visited[plus] : # 3번 조건문
            visited[plus] = True
            time[plus] = time[temp] + 1
            queue.append(plus)
        
print(sol(n,k))
