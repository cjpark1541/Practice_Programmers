def solution(a,b):
    first=int(str(a)+str(b)); second=2*a*b
    list_num=[first, second]
    return max(list_num)

a=int(input('첫 숫자:')); b=int(input('두번째 숫자:'))
print(solution(a,b))
