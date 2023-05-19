def solution(array,n):
    abs_list=[]
    for i in array: new_abs=abs(int(i)-n); abs_list.append(new_abs)
    index_number=abs_list.index(min(abs_list))
    return array[index_number]

array_input=input('넣을 list').split(); number=int(input('n='))
print(solution(array_input,number))