'''import time

A=11#input('자연수 넣기')
B=11#input('곱하려는 수 넣기')
C=12#input('나눈 나머지')
t_before=time.time_ns()
Result=(A**B)%C
print(Result,f"{time.time_ns()-t_before: .5f}")'''

from math import log10
A=2147483647; B=2147483647; C=12
#map(int, input().split())
result=(B*log10(A)-log10(C))
remainer=(10**result)%1
print(round(C*remainer,1))
