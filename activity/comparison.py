# add your get_student_with_more_classes function here!

def get_student_with_more_classes(Student1, Student2):

    if Student1.get_num_classes() > Student2.get_num_classes(): 
        return Student1.name

    else:
        return Student2.name



