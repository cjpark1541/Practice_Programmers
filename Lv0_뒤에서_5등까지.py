def solution(list):
    list2=[]
    while not len(list2)==5:
        minval=min(list)
        list.remove(minval); list2.append(minval)
    return list2

list_input=list(input().split()); 
list_input=list(map(int, list_input))
print(solution(list_input))