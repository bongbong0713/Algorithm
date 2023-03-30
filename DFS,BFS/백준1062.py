import sys

def dfs(idx,count,learn,words):
    global result
    
    if count == K - 5: #count가 k-5가 되면 배울 수 있는 양을 채웠다는 뜻
        tmp = 0
        for word in words:
            isin = True
            for w in word:
                if not learn[ord(w) - ord('a')]: #단어 중 하나라도 배우지 못한 알파벳이 있다면 break하고 개수 카운트x
                    isin = False
                    break
            if isin: #단어에 포함된 알파벳을 모두 배운 상태라면 카운트+1
                tmp += 1 
        result = max(tmp, result) #result값을 항상 tmp와 전의 값인 result와 비교해서 최대값으로 갱신
        return

    for i in range(idx, 26):
        if not learn[i]: #dfs로 현재 알파벳을 배운 경우와 배우지 않는 경우 모두 비교하기 위해서 i번째 알파펫을 배울 경우 count+1을 해서 dfs실행하고 안배울 경우 다음i+1번째 배우는 경우로 dfs실행
            learn[i] = True 
            dfs(i, count + 1, learn, words)
            learn[i] = False

N, K = map(int, input().split())

if K < 5: #k가 5보다 작으면 anta tica도 못배우므로 0 출력
    print(0)
    sys.exit()

elif K == 26: #k가 26이면 모든 알파벳을 배울 수 있으므로 N 출력
    print(N)
    sys.exit()

words = [set(sys.stdin.readline().rstrip()) for _ in range(N)] #rstrip으로 중복되는 알파벳 제거
learn = [0] * 26
result = 0


for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = True #anta, tica는 배워야하므로 포함 된 a, c, i, n, t는 무조건 배우게 함

dfs(0, 0, learn, words) #DFS

print(result)
