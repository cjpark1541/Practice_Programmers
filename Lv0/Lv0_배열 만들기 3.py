def solution(arr,interval):
    new_list=[];
    for i in range(len(interval)):
        interval_min=int(min(interval[i]))
        interval_max=int(max(interval[i]))
        new_list.extend(array[interval_min:interval_max])
        new_list=list(map(int, new_list))
    return new_list

array=list(input('array입력:').split()); 
interval_list=[]
while input('계속 넣을거면 O입력')=='O':
    interval_new=list(input('newlist입력').split())
    interval_list.append(interval_new)

print(solution(array,interval_list))