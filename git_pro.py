
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    @property
    def set_name(self, name:str):
        self.name = name
    @property
    def get_name(self):
        return self.name
    @property
    def set_name(self, age:int):
        self.age = age
    @property
    def get_age(self):
        return self.age
        
    def sayHelloToSamu(self):
        print("Hello Samu!")