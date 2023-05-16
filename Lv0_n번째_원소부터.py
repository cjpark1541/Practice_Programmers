def solution(list,n):
    list_2=list[int(n-1):int(len(list))]
    return(list_2)

num_list=list(input('list=').split())
number=int(input('n='))
print(solution(num_list,number))


