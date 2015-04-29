import random
from datetime import datetime


def verify_input(a, b):
    try:
        return int(input("What is the sum of {} and {}? ".format(a, b)))
    except ValueError:
        print("Answer must be integer")
        return verify_input(a, b)
    
def duration(start, end):
    delta = end - start
    return delta.seconds

def grade(a, b, answer):
    if (answer == a + b):
        return "right"
    else:
        return "wrong"
    
def print_grade(a, b, answer):
    print("{} is {}!".format(answer, grade(a, b, answer)))
    
class MathQuiz:
    def __init__(self):
        self.total_questions = 5
        self.times = []
        self.grades = []
    
    def run(self):
        "Runs the quiz itself and stores time info and grades"
        for count in range(self.total_questions):
            a = random.randint(1, 10)
            b = random.randint(1, 10)

            start = datetime.now()
            answer = verify_input(a, b)
            end = datetime.now()

            print_grade(a, b, answer)
            self.grades.append(grade(a, b, answer))
            self.times.append(duration(start, end))
        
    def __str__(self):
        """Creates summary"""
        summary = ""
        for n in range(self.total_questions):
            summary += "Question #{} took about {} seconds to complete and was {}.\n".format(n+1, self.times[n], self.grades[n])
        summary += "You took {} seconds to finish the quiz\n".format(sum(self.times))
        summary += "Your average time was {} seconds per question\n".format(sum(self.times) / self.total_questions)
        return summary
    
    def print_summary(self):
        print(self)

if __name__ == "__main__":
    quiz = MathQuiz()
    quiz.run()
    quiz.print_summary()