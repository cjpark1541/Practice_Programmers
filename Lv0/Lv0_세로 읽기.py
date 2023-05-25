def solution(my_string,m,c):
    string_list=[]; wanted_string=''
    for i in range(0,len(my_string),m):
        new_string=my_string[int(i):int(i)+m]
        string_list.append(new_string)
    for j in string_list:
        wanted_string=wanted_string+j[c-1]
    return wanted_string

my_string=input('string:')
m,c=input('m,c=').split(',')
print(solution(my_string,int(m),int(c)))