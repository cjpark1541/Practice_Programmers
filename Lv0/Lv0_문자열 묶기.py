def solution(strArr):
    strArr_mix=[]; strArr_q2=[]
    for i in strArr:
        strArr_mix.append(len(i))
    strArr_q1=list(range(min(strArr_mix),max(strArr_mix)+1))
    for i in strArr_q1:
        strArr_q2.append(strArr_mix.count(i))
    return max(strArr_q2)
    
strArr=["a","bc","d","efg","hi"] #list(input().split())
print(solution(strArr))