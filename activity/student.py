# add your Student class here!

# In this activity you will implement a Student class
#  and a function, get_student_with_more_classes, based on the clues from in the code located in main.py. 
# Think about what attributes and methods are being used and being called in the code.
class Student:
    def __init__(self, name, year, classes):
        self.name = name
        self.year = year
        self.classes = classes
    
    def add_class(self, name_class):
        self.classes.append(name_class)
    
    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        print(self.name + " is a " + self.year + " enrolled in " + str(len(self.classes)) + " classes")
