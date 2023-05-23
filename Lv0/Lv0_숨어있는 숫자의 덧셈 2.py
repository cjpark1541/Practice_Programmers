def solution(my_string):
    number_string='0'; number_sum=0
    for i in my_string:
        if i.isdecimal()==True: 
            number_string=number_string+str(i)
        else: 
            number_sum=int(number_string)+number_sum
            number_string='0'
        if my_string[len(my_string)-1].isdecimal()==True:
            number_sum=int(number_string)+number_sum
    return(number_sum)

my_string=input('my_string=')
print(solution(my_string))