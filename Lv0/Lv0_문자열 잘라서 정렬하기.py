def solution(mystring):
    string_list=[]; new_string=''; mystring=mystring+'x'
    for i in mystring:
        if i=='x': 
            string_list.append(new_string)
            new_string=''
        else: 
            new_string=new_string+i
        string_list.sort()
    return(string_list)

mystring=input('string=')
print(solution(mystring))