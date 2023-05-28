def solution(arr,queries):
    for i in range(len(queries)):
        i_min=min(queries[i]); i_max=max(queries[i])
        for j in range(i_min,i_max):
            
        arr[i_min],arr[i_max]=arr[i_max],arr[i_min]
    return arr


arr=[0, 1, 2, 4, 3]; queries=[[0, 4, 1],[0, 3, 2],[0, 3, 3]]
#s=0, e=4, k=1 / s=0 e=3 k=2 / s=0 e=3 k=3
