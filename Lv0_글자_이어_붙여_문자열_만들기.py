def solution(string,index):
    string2=''
    for i in index: 
        string2=string2+string[int(i)]
    return string2

my_string=input('my_String: ')
index_list=input('index_list: ').split(',')
print(solution(my_string,index_list))