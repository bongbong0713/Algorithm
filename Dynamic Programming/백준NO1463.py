from collections import deque

x=int(input())

q=deque([x])
visited=[0]*(x+1)  #인풋의 크기+1만큼 visited 리스트 생성

while q: #BFS 방식
    a=q.popleft()
    if a==1: #a를 1로 만들면 break
        break
    if a%3==0 and visited[a//3]==0:  #3으로 나누어 떨어지고 3으로 나눈 값이 방문하지 않았던 값이면 3으로 나눈 몫을 q에 삽입하고 방문처리+횟수 기록
        q.append(a//3)
        visited[a//3]=visited[a]+1
    if a%2==0 and visited[a//2]==0:  #2로 나누어 떨어지면 2으로 나눈 값이 방문하지 않았던 값이면 2로 나눈 몫을 q에 삽입하고 방문처리+횟수 기록
        q.append(a//2)
        visited[a//2]=visited[a]+1
    if visited[a-1]==0:  #3이나 2로 나누어 떨어지지 않으면 1을 빼서 q에 삽입하고 방문처리
        q.append(a-1)
        visited[a-1]=visited[a]+1

print(visited[1]) 
