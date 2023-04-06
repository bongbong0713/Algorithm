import sys
input=sys.stdin.readline

while True:
    try:
        n=int(input())
        lst=list(map(int, input().split())) 
        
        leng=0 
        lis=[0] 
        
        for i in range(n):
            if lst[i]>lis[leng]: 
                leng+=1
                lis.append(lst[i]) 
            else:
                left = 0
                right = len(lis) - 1
                while left < right:
                    mid = (right + left) // 2

                    if lis[mid] < lst[i]:
                        left = mid + 1
                    else:
                        right = mid 
                
                lis[right]=lst[i] 
                
        print(leng) 
    except: 
        sys.exit(0)
