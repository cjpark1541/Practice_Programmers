def solution(n):
    new_array=[]
    for i in range(2,n+1):
        if n%int(i)==0:
            new_array.append(primenumber(i))
    new_list=list(filter(lambda x: x>1, new_array))
    return new_list

def primenumber(n):
    for i in range(2,n):
        if n%int(i)==0: return False
    return n

m=int(input('number='))
print(solution(m))