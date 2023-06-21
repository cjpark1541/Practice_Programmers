def solution(numbers):
    num_list=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i,ind in enumerate(num_list):
        numbers=numbers.replace(ind,str(i))
    return numbers

def solution2(numbers):
    dictionary={'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in dictionary.keys():
        numbers=numbers.replace(i,dictionary[i])
    return numbers

numbers="onetwothreefourfivesixseveneightnine"
print(solution(numbers))