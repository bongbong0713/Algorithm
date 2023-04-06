import sys
from math import factorial

t=int(sys.stdin.readline())

for _ in range(t):
    n, m=map(int, sys.stdin.readline().split())
    Max=max(n, m)
    Min=min(n, m)
    print(factorial(Max)//(factorial(Min)*factorial(Max-Min)))
