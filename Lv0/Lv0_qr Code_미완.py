def solution(q, r, code):
    index=0; letter=''
    for i in code:
        if index%q==r: letter=letter+i
        index=index+1
    return letter

code="programmers"
q=1; r=0
print(solution(q,r,code))
