from decorators.decorators import expected_type
class User():
    name = ''  # validation ascii
    language = ''
    course = ''
    grade = ''

    def __init__(self, name='', language=''):
        self.name = name
        self.language = language

    def __str__(self):
        return f"Name = {self.name} and language = {self.language}"
    #@expected_type(str)
    def chose_course(self, course):
        self.course = course
    #@expected_type(int)
    def set_grade(self, grade):
        self.grade = grade

