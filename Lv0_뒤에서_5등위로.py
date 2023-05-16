def solution(list):
    list2=[]
    while not len(list)==5:
        maxval=max(list)
        list.remove(maxval); list2.insert(0,maxval)
        list2
    return list2

list_input=list(input().split()); 
list_input=list(map(int, list_input))
print(solution(list_input))