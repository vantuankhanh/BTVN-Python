class Student:
    def __init__(self,name,DoB,code):
        self.name = name
        self.DoB = DoB
        self.code = code

    def check(self,object):
        if self.code == object:
            return True
        else:
            return False

    def show(self):
        print(f'{i.code}. {i.name}. DoB: {i.DoB}')
        
class StudentIter:
    def __init__(self,lst):
        self.lst = lst
        self.current = 0
    
    def __next__(self):
        if self.current < len(self.lst.student):
            result = self.lst.student[self.current]
            self.current += 1
            return result
        raise StopIteration

class Student_list:
    def __init__(self):
        self.student = list()
    
    @property
    def show(self):
        for i in self.student:
            print(f'{i.code}. {i.name}. DoB: {i.DoB}')
    
    def add_student(self,student):
        self.student.append(student)

    def __iter__(self):
        return StudentIter(self)

    def sort_code(self):
        self.student = sorted(self.student, key= lambda i:i.code)
        self.show

lst = Student_list()
run = True
while run:
    print('Option:\n\
      1. Show student list\n\
      2. Add student\n\
      3. Update student\'s information\n\
      4. Delete student\n\
      5. Look up for student by code\n\
      6. Sort list by code\n\
      7. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        print('Student List:')
        lst.show
    if choice == '2':
        name = input('Enter student\'s name: ')
        DoB = input('Enter student\'s DoB: ')
        code = input('Enter student\'s code: ')
        lst.add_student(Student(name,DoB,code))
        print('Student has been added.')
    if choice == '3':
        code_check = int(input('Enter student\'s code to update: '))
        check = False
        for i in lst:
            if i.check(code_check):
                check = True
                name_change = input('Enter student\'s name: ')
                DoB_change = input('Enter student\'s DoB: ')
                code_change = input('Enter student\'s code: ')
                i.name = name_change
                i.DoB = DoB_change
                i.code = code_change
                print('Student has been updated')
        if check == False:
            print('Student\'s code is not in list')
    if choice == '4':
        code_check = int(input('Enter student\'s code to delete: '))
        check = False
        for i in lst:
            if i.check(code_check):
                check = True
                del lst.student[code_check-1]
        if check == False:
            print('Student\'s code is not in list')
    if choice == '5':
        code_check = int(input('Enter student\'s code to look up: '))
        check = False
        for i in lst:
            if i.check(code_check):
                check = True
                i.show()
        if check == False:
            print('Student\'s code is not in list')
    if choice == '6':
        lst.sort_code()
    if choice == '7':
        run = False
    else:
        print('Wrong input!!!')