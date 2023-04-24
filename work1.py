import datetime


class Homework:

    def __init__(self, text: str, deadline: datetime.timedelta = datetime.timedelta(days=1)):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.today()

    def is_active(self) -> bool:
        return (datetime.datetime.today() - self.created).days < self.deadline


class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, Homework):
        if not Homework.is_active():
            print("You are late")
            return None
        return Homework


class Teacher:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, deadline: datetime.timedelta.days = datetime.timedelta(days=1)):
        hw = Homework(f"{text}", deadline)
        return hw


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)
