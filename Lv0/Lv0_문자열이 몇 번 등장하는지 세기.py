def solution(myString,pat):
    i=0; n=0
    while myString[i:].find(pat)!=-1: 
        i=myString[i:].find(pat)+i+1
        n=n+1
    return n

myString=input('string is:')
pat=input('finding is:')
print(solution(myString,pat))