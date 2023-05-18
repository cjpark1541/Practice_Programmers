def solution(n_list,n):
    new_list=[]
    for i in range(0,len(n_list),n):
        new_list.append(num_list[i:i+num])
    return new_list
        
num_list=input('list 입력').split(', '); num=int(input('리스트의 수:'))
print(solution(num_list,num))