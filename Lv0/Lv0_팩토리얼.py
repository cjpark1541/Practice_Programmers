from functools import reduce
def multiply(list): 
    multiply_value=reduce(lambda x,y:x*y,list)
    return multiply_value   #함수 list 내 곱셈 정의

def solution(number):
    value=1; i=1
    while value<=number: 
        i=i+1; fac_list=list(range(1,i))
        value=multiply(fac_list)
    return i-2, value

n=int(input('n=')); print(solution(n))