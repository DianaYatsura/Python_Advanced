# Your task is to write a program which allows teachers to create a multiple choice test in a class called Testpaper
# and to be also able to assign a minimum pass mark. The testpaper's subject should also be included. The attributes
# are in the following order:
# 1. subject
# 2. markscheme
# 3. pass_mark
# As well as that, we need to create student objects to take the test itself! Create another class called Student and
# do the following:
# Create an attribute called tests_taken and set the default as  'No tests taken'.
# Make a method called take_test(), which takes in the testpaper object they are completing and the student('s answers.
# Compare what they wrote to the mark scheme, and append to the/create a dictionary assigned to tests_taken in the way as shown
# in the point below.) Each key in the dictionary should be the testpaper subject and each value should be a string in the
# format seen in the examples below (whether or not the student has failed, and their percentage in brackets).

class Testpaper:

    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:

    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, paper, student_answers):
        correct_answers = 0
        total_questions = len(paper.markscheme)

        for i in range(total_questions):
            if student_answers[i] == paper.markscheme[i]:
                correct_answers += 1

        percentage = round((correct_answers / total_questions) * 100)

        result = "Passed!" if percentage >= int(paper.pass_mark.strip('%')) else "Failed!"

        if self.tests_taken == "No tests taken":
            self.tests_taken = {}

        self.tests_taken[paper.subject] = f'{result} ({percentage}%)'


paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
student1 = Student()
print(student1.tests_taken)  # "No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken)  # {"Maths" : "Passed! (80%)"}

paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
student2 = Student()
student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(student2.tests_taken)  # {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}
