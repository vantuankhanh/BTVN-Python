EVdict={'hello':'xin chào','name':'tên'}

def translate(dic,word):
    for i in dic.keys():
        if i==word.lower():
            return dic[i]
        else:
            return None
               
word = input('Nhập từ cần tra: ')
trans = translate(EVdict, word)
if trans:
    print(word,'nghĩa là',trans)
else:
    print('Từ không có trong từ điển')