def solution(bef,aft):
    for i in aft:
        if bef.find(i)==-1: value=0; break
        else: bef=bef.replace(i,'',1); value=1
    return value

before=input('기존 문자열:'); after=input('목표 문자열:')
print(solution(before, after))