import unittest
from datetime import datetime
import math_quiz

class TestMathQuiz(unittest.TestCase):

    def test_duration(self):
        """Test that duration is calculated correctly"""
        time1 = datetime(2015,5,2,11,58,15)
        time2 = datetime(2015,5,2,11,58,30)
        self.assertEqual(math_quiz.duration(time1, time2), 15)

    def test_grade(self):
        """Tests accurate grading"""
        self.assertEqual(math_quiz.grade(1,1,2), "right")
        self.assertEqual(math_quiz.grade(1,1,3), "wrong")

    def test_math_quiz_result(self):
        """Tests summary prints accurate results"""
        quiz = math_quiz.MathQuiz()
        quiz.times = [1, 2, 3, 4, 5]
        quiz.grades = ['right', 'right', 'wrong', 'wrong', 'wrong']
        expected = "Question #1 took about 1 seconds to complete and was right.\n"
        expected += "Question #2 took about 2 seconds to complete and was right.\n"
        expected += "Question #3 took about 3 seconds to complete and was wrong.\n"
        expected += "Question #4 took about 4 seconds to complete and was wrong.\n"
        expected += "Question #5 took about 5 seconds to complete and was wrong.\n"
        expected += "You took 15 seconds to finish the quiz\n"
        expected += "Your average time was 3.0 seconds per question\n"
        self.assertEqual(str(quiz), expected)

if __name__ == "__main__":
    unittest.main()