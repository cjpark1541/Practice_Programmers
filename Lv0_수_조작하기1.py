def solution(int_1,n):
    n1=int_1.count('w'); n2=int_1.count('a')
    n3=int_1.count('s'); n4=int_1.count('d')
    n=n+n1-n2+10*n3-10*n4
    return n

int_input=str(input('입력값: '))
initial_n=int(input('처음값: '))
print(solution(int_input,initial_n))