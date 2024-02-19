class Animal:
    def __init__(self, species, language):
        self.spec = species
        self.lang = language
    def print_info(self):
        print(self.spec, self.lang)
    def speak(self):
        print('I am a ', self.spec, 'and I', self.lang)
    def __repr__(self):
        return 'Animal(\''+self.spec+'\',\''+self.lang+'\')'
    def __str__(self):
        return 'I am a '+self.spec+' and I '+self.lang+"."
class Bird(Animal):

    # this __init__ method Extends __init__ of the parent class
     def __init__(self, length_beak, species ='animal', language ='make sounds'):
        self.lb = length_beak
        super().__init__(species, language) #sends the arguments into a parent class(since unspecified(super()) it will send it to class Animal)
     def speak(self):
         print(self.lang*3)
         super().speak()
class Point(object):
    pass

tweety = Bird(1.5, "bird", "chirp")
#print(tweety.speak)
def f(b):
    a = 6
    return a*b
a = 0 
print(f(3))
print('a is', a)