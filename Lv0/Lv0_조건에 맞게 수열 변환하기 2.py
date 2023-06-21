def transform1(arr):
    list_out=[]
    for i in arr:
        if i>=50 and i%2==0: i=i/2; list_out.append(i)
        elif i<50 and i%2==1: i=i*2+1; list_out.append(i)
        else: list_out.append(i)
    return list_out

def solution(arr):
    after_arr=transform1(arr)
    while arr!=after_arr:
        arr=after_arr; after_arr=transform1(arr)
    for i in range(len(arr)):
        if arr[i]==arr[i+1]: break
    return arr,i+1

list_in=list(map(int,list_in))
print(solution(list_in))
