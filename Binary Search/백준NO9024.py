import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    arr = sorted(list(map(int, sys.stdin.readline().split())))

    ans = 0
    nearest = 999999999
    for i in range(n):
        left, right = i+1, n-1
        while left <= right:
            mid = (left+right)//2
            now = arr[i]+arr[mid]
            if now > k:
                right = mid-1
            else:
                left = mid+1
            if abs(k-now) < nearest:
                ans = 1
                nearest = abs(k-now)
            elif abs(k-now) == nearest:
                ans += 1
    print(ans)
