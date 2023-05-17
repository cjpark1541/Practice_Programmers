def solution(string):
    dict_ref={'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z'}
    list_string=string.split(' '); list_translated=[]
    for i in list_string: list_translated.append(dict_ref[i])
    string=''.join(list_translated)
    return string

string=input(); 
print(solution(string))