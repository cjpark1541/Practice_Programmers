def solution(arr,queries):
    for i in range(len(queries)):
        s=queries[i][0]; e=queries[i][1]; k=queries[i][2]
        for j in range(s,e+1):
            if j%k==0: arr[j]=arr[j]+1
    return arr

arr=[0, 1, 2, 4, 3]; queries=[[0, 4, 1],[0, 3, 2],[0, 3, 3]]
print(solution(arr,queries))