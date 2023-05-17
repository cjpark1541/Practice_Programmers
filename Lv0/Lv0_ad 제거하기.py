def solution(list,input):
    list2=[]
    for i in list:
        word=str(i)
        if word.find(input)==-1: list2.append(word)
        else: list2=list2
    return list2

list_input=list(input('input=').split())
Input=str(input('find='))
print(solution(list_input,Input))