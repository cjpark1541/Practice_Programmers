#def solution(numbers):

numbers="onetwothreefourfivesixseveneightnine"	
dictionary={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,"six":6,"seven":7, "eight":8, "nine":9}
new_list=[]; new_addon=''
for i in numbers:
    if i=='o': numbers=numbers.strip('one'); new_list.append(1)
    elif i=='e': numbers=numbers.strip('eight'); new_list.append(8)
    elif i=='n': numbers=numbers.strip('nine'); new_list.append(9)
    else:
        new_addon=new_addon+i
        print(new_addon)
        if new_addon=='tw': numbers=numbers.strip('two'); new_list.append(2); new_addon=''; print(numbers)
        elif new_addon=='th': numbers=numbers.strip('three'); new_list.append(3); new_addon=''
        elif new_addon=='fo': numbers=numbers.strip('four'); new_list.append(4); new_addon=''
        elif new_addon=='fi': numbers=numbers.strip('five'); new_list.append(5); new_addon=''
        elif new_addon=='si': numbers=numbers.strip('six'); new_list.append(6); new_addon=''
        elif new_addon=='se': numbers=numbers.strip('seven'); new_list.append(7); new_addon=''
        else: new_addon=new_addon