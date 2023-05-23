def solution(a,d,included):
    value=0
    for i in included:
        if i==True: value=value+a
        a=a+d
    return value

a,d=input('a,d입력:').split(',')
included=list(input().split(', '))
bool_included=[]
for i in included:
    if i=='true': bool_included.append(True)
    else: bool_included.append(False)
print(solution(int(a),int(d),bool_included))