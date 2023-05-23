def solution(myString,pat):
    i=0
    while myString[i:].find(pat)!=-1: 
        i=myString[i:].find(pat)+i+1
    return myString[:i+1]
    
myString=input('string is:')
pat=input('finding is')
print(solution(myString,pat))




    