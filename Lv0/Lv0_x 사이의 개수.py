def solution(string,letter):
    list_n=[]; val=0
    for i in string:
        if not str(i)==letter: val=val+1
        else: list_n.append(val); val=0
    list_n.append(val)
    return list_n

string_input=list(input('입력(x포함): '))
letter=str(input('구분 문자열: '))
print('answer:',solution(string_input,letter))