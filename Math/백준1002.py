n=int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2=map(int, input().split())
    Add = (r1+r2)**2
    Sub = (r1-r2)**2
    Dist = (x2-x1)**2 + (y2-y1)**2

    # 좌표가 같고, 거리가 같은 경우: 무한대
    if (Dist == 0) and (Sub == 0):
        print(-1)
    # 교점이 1 개
    elif (Dist == Add) or (Dist == Sub):
        print(1)
    # 교점이 2 개
    elif (Sub < Dist) and (Dist < Add):
        print(2)
    # 교점이 0 개
    else:
        print(0)
