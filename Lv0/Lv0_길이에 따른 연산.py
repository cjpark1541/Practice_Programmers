def solution(num_list):
    
    if len(num_list)<10:
        value=1
        for i in num_list: value=value*int(i)
    else:
        value=0
        for i in num_list: value=value+int(i)
    return value

num_list=[2, 3, 4, 5]
print(solution(num_list))