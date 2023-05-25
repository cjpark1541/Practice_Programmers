def solution(s):
    list_s=s.split()
    value=0
    for i in list_s:
        if i=='Z': value=value-new_value
        else: 
            new_value=int(i)
            value=value+new_value
    return value

s=str(input('숫자 넣기 ex)1 2 Z 3'))
print(solution(s))
