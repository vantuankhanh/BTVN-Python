def del_spec(string):
    str_return=''
    for i in string:
        if i.isalnum()==True or i.isspace()==True:
            str_return+=i
    return str_return

def dic_count(string):
    words=string.lower().split()
    count=dict()
    for i in words:    
        if i in count.keys():
            count[i]+=1
        else:
            count[i]=1
    return count

def find_dic(dic,word):
    if word in dic.keys():
        return dic[word]
    else:
        return '0'

string = input('Nhập văn bản: ')
string = del_spec(string)
dic_find = dic_count(string)
word = input('\nNhập từ bạn muốn biết số lần xuất hiện: ')
time = find_dic(dic_find, word)
print('Từ \"'+word+'\" xuất hiện',time,'lần')