def solution(my_str):
    list_result=[]; addon=''
    for i in (my_str+'a'):
        if i=='a'or i=='b' or i=='c': 
            if addon!='':
                list_result.append(addon)
            addon=''
        else: addon=addon+i
    return(list_result)
    

my_str='baconlettucetomato'
print(solution(my_str))