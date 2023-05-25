def solution(myString,pat):
    num=myString[::-1].find(pat[::-1])
    return myString[:len(myString)-num]
  
myString=input('string is:')
pat=input('finding is')
print(solution(myString,pat))