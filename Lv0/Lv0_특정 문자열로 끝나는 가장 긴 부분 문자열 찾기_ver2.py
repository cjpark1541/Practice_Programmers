def solution(myString,pat):
    num=myString[::-1].find(pat[::-1])
    return myString[:len(myString)-num]
  
myString='AbCdEFG' #input('string is:')
pat="dE"    #input('finding is')
print(solution(myString,pat))