def solution(arr,flag):
    new_arr=[]
    for i in range(int(len(flag))):
        if flag[i]==True: 
            times=int(arr[i])*2; addon_value=arr[i]
            for i in range(times): new_arr.append(addon_value)
        else:
            times=int(arr[i])
            for i in range(times): new_arr.remove(addon_value)
    return new_arr

arr=[3, 2, 4, 1, 3] 
flag=[True, False, True, False, False]
print(solution(arr,flag))
