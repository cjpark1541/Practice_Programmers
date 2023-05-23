def solution(my_string,s,e):
    e=e+1
    new_string=(my_string[s:e])
    return my_string[:s]+new_string[::-1]+my_string[e:]

my_string=input('string입력')
s=int(input('입력값1')); e=int(input('입력값2'))
print(solution(my_string,s,e))