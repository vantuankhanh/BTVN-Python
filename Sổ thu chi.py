def add_item(list_item,item):
    list_item.append(item)

def find_item(list_item,item):
    result=-1
    for i in range(len(list_item)):
        if list_item[i]['name']==item:
            result=i
    return result

def remove_item(list_item,item):
    if find_item(list_item, item)>-1:
        del list_item[find_item(list_item, item)]
    else:
        print(item,'not in list')

expenses=list()
run=True
print('Your expenses:',expenses)
while run:
    print("What do you want to do? -\n"\
            "1. Add\n" \
            "2. Remove")
    option = input("Select option 1 or 2: ")
    if option in ['1','2']:
        name_item = input("Item name: ")
        if option=='1':
            cost_item=input('Input your expense: ')
            day_item=input('Input the day of expense: ')
            item=dict({'name':name_item,'cost':cost_item,'date':day_item})
            add_item(expenses,item)
            print('Your expenses:',expenses)
        else:
            remove_item(expenses, name_item)
            print('Your expenses:',expenses)
    else:
        print('Wrong option')
    print('Do you want to continue? (y/n)',end='')
    con=input()
    if con=='n':
        run=False