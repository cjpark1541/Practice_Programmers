def solution(x1,x2,x3,x4):
    return sol_down(sol_up(x1,x2),sol_up(x3,x4))

def sol_up(x1,x2):
    if x1 or x2 == True: return True
    else: return False

def sol_down(x1,x2):
    if x1 and x2 == True: return True
    else: return False

x1,x2,x3,x4=True,False,False,False
print(solution(x1,x2,x3,x4))