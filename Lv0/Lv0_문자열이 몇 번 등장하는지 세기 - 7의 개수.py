def solution(array):
    new_string=''
    for i in array:
        new_string=new_string+str(i)
    print(new_string)
    i=0; n=0
    while new_string[i:].find(str(7))!=-1: 
        i=new_string[i:].find(str(7))+i+1
        n=n+1
    return n
    
array=[7, 77, 17]
print(solution(array))