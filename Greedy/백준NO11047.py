n, k=map(int, input().split())

list=[]
count=0

for i in range(n):
    list.append(int(input()))

list.sort(reverse=True) #큰 수부터 나눠주기 위해 내림차순 정렬

for i in range(n):
    if k/list[i]>=1: #list의 i번째로 나눴을 때 몫이 1보다 크면 나눠진다는 뜻
        count+=k//list[i] #나눈 몫만큼 count에 더해줌
        k-=(k//list[i])*list[i] #list의 i번째로 최대한 빼줌
        

print(count)
