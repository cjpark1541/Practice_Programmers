def solution(n):
    Colatz=[n]
    while n!=1:
        if n%2==0: n=n/2
        else: n=3*n+1
        Colatz.append(n)
    return Colatz

n=int(input('1000이하의 수를 넣으세요.'))
print(solution(n))
