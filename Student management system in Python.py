class Student:
    def __init__(self,name,DoB,code):
        self.name = name
        self.DoB = DoB
        self.code = code
    
class Student_list:
    def __init__(self) -> list:
        pass

    def show(self):
        for i in self:
            print(f'{self.code}. {self.name}. DoB: {self.DoB}')
    
    def add(self,object):
        self.append(object)

    def check(self,object):
        if object in self:
            return True
        else:
            return False
    
    def update(self,object):
        if self.check(object):
            name