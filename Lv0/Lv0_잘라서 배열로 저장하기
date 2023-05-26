def solution(my_str,n):
    new_str=''; new_list=[]
    for i in my_str:
        new_str=new_str+i
        if len(new_str)==n: new_list.append(new_str); new_str=''
    new_list.append(new_str); new_list=list(filter(None, new_list))
    return new_list

my_str=input('문자입력:')
n=int(input('숫자입력:'))
print(solution(my_str,n))