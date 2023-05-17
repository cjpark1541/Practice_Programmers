def solution(arr,idx,val):
    j=int(idx)
    newstr=''.join(arr[j:])
    value=int(newstr.find(val))
    if value!=-1: value=idx+value
    return value

array=input('입력(ex 0, 0, 0, 1):').split(', ')
index=int(input('index 입력:'))
value=input('찾을 value:')
print(solution(array,index,value))