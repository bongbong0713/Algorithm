n=int(input())

words=[]
alpha=[0 for _ in range(26)] #알파벳 개수만큼 0인 리스트 생성
ans=0
count=0 

for i in range(n): #입력
    w=input()
    words.append(w)

for i in range(n): #단어 개수만큼 
    for j in range(len(words[i])): #해당 단어의 길이 만큼
        alpha[ord(words[i][j])-ord('A')]+=10**(len(words[i])-j-1) #알파벳 리스트에 단어의 제일 앞부터 높은 자리수 부여(예를 들어 ABC면 A에 100, B에 10, C에 1 부여)

alpha.sort(reverse=True) #알파벳 리스트에서 높은 자리수부터 가중치를 부여하기 위해 내림차순으로 정렬

weight=9

for i in range(26): 
    ans+=weight*alpha[i] #9부터 하나씩 줄여가면서 가중치 부여
    weight-=1

print(ans)
