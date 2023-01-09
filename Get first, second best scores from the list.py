a=[]
while True:
    b=input('Nhập số bạn muốn thêm vào list, nếu không muốn nhập nữa hãy nhập n: ')
    if b=='n':
        break
    elif b.isnumeric()==True:
        a.append(int(b))
    else:
        print('Bạn đã nhập sai cú pháp')
if len(a)<2:
    print('Không thể thực hiện do list không đủ 2 phần tử')
else:
    a.sort()
    print('Hai số lớn nhất của list lần lượt là',a[-1],'và',a[-2])