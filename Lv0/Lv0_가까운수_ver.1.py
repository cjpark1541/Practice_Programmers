def solution(array,n):
    array.append(n); array.sort()
    i=array.index(n)
    if i==0: number=array[i+1]
    elif i==len(array)-1: number=array[i-1]
    else: 
        if abs(n-array[i-1])>abs(n-array[i+1]):
            number=array[i+1]
        else:
            number=array[i-1]
    return number    


array=list(input('input list=","이용').split(',')); array=list(map(int,array))
n=int(input('원하는 value:'))
print(solution(array,n))