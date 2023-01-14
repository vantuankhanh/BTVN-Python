list_sp={'0001':'sp1','0002':'sp2'}

def show_list(lst):
    print('Danh sách sản phẩm hiện tại:')
    for i in lst.keys():
        print(i,':',lst[i])

def show_item(lst,id_item):
    if id_item in lst.keys():
        print(id_item,':',lst[id_item])
    else:
        print('ID không có trong danh sách')

def add_item(lst):
    id_item=input('Nhập ID bạn muốn thêm vào: ')
    if id_item in lst.keys():
        print('ID đã có trong danh sách')
    else:
        item=input('Nhập tên sản phẩm: ')
        if item in lst.values():
            print('Sản phẩm đã có trong danh sách')
            choice=''
            while True:
                choice=input('Bạn có muốn tiếp tục? (y/n): ')
                if choice.lower() not in ['y','n']:
                    print('Bạn đã nhập sai cú pháp')
                else: break
            if choice=='y':
                lst[id_item]=item
        else:
            lst[id_item]=item
    
def update_id(lst,id_item):
    id_item=input('Nhập ID cần cập nhật: ')
    if id_item in lst.keys():
        print(id_item,'hiện là:',lst[id_item])
        new_item=input('Bạn muốn đổi thành: ')
        lst[id_item]=new_item
    else:
        print('ID không có trong danh sách')
        
    
def delete_item(lst):
    id_item=input('Nhập ID bạn muốn xóa: ')
    if id_item in lst.keys():
        show_item(lst, id_item)
        while True:
            choice=input('Bạn có muốn tiếp tục? (y/n): ')
            if choice.lower()=='y':
                del lst[id_item]
                break
            elif choice.lower()=='n':
                break
            else:
                print('Bạn đã nhập sai cú pháp')
    else:
        print('ID không có trong danh sách')

show_list(list_sp)
print()
while True:    
    print('Option:\n1 - Hiển thị sản phẩm theo ID\n\
2 - Thêm sản phẩm mới vào danh sách\n\
3 - Cập nhật sản phẩm trong danh sách\n\
4 - Xoá một sản phẩm khỏi danh sách\n\
5 - Thoát')
    choice=input('Lựa chọn của bạn: ')
    if choice in ['1','2','3','4','5']:
        if choice=='1':
            id_item=input('Nhập ID cần tra: ')
            show_item(list_sp, id_item)
        elif choice=='2':
            add_item(list_sp)
        elif choice=='3':
            update_id(list_sp, id_item)
        elif choice=='4':  
            delete_item(list_sp)
        elif choice=='5':      
            break
        else: print('Bạn đã nhập sai cú pháp')
    list_sp=dict(sorted(list_sp.items(),key=lambda x:x[0]))
    show_list(list_sp)
    choice=input('Bạn có muốn tiếp tục? (y/n): ')
    if choice.lower()=='n':
        break
    elif choice.lower()!='n' and choice.lower()!='y':
        print('Bạn đã nhập sai cú pháp')