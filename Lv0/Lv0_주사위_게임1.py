a,b=input().split()
a=int(a); b=int(b)

if a%2==1 or b%2==1:
    if a%2==1 and b%2==1: score=a**2+b**2
    else: score=2*(a+b)
else: score=abs(a-b)
print(score)