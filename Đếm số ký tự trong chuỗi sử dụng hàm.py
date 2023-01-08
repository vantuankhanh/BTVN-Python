def count_str(string):
    a=0
    for i in string:
        a+=1
    return a

string=input('Input string to count: ')
print(count_str(string))