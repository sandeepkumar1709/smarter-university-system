import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.controllers.quizzes_controller import QuizzesController

from datetime import datetime, timedelta


class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        This function tests the functionality if there is no input given for title of the quiz(i.e. None)
        Expected functionality is that the quiz ID should be None then neccessary actions will be taken based on the return type
        
        This is crashing at quizzes_controller.py at line #63 in add_quiz()
        """

        # add the quiz with Empty title where the case of giving no inputs in the title

        #This is crashing the application and giving error as "TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'"
        quiz1_id = self.ctrl.add_quiz(None, "Sample Quiz", datetime.now(), datetime.now() + timedelta(minutes=90))
        # So at this point the quiz id should be returned None since there is no input given title
        self.assertIsNone(quiz1_id, "The quiz id should not be None")



        
    def test_expose_failure_02(self):
        """
        This function tests if utf-8 characters are provided in title of the answer 
        Expected functionality is that it should return valid answer ID 

        #this is crashing at utils.py", line 11, in generate_id called by quizzes_controller.py", line #91 in add_answer  
        """
        # Adding the quiz with valid parameters
        quiz_id = self.ctrl.add_quiz("Title", "Sample Quiz", datetime.now(), datetime.now() + timedelta(minutes=90))

        #Adding the quiz question with valid parameters and valid quiz ID
        question_id = self.ctrl.add_question(quiz_id,"Question Title","Text of the question")

        #Adding the answer with valid question id but passing utf-8 characters inside text of answers

        #this is crashing while generating the id for answer since there are utf-8 characters, crashing the app is not expected
        
        answer_id = self.ctrl.add_answer(question_id,"Answer \ud834 content","yes")
        self.assertIsNotNone(answer_id,"Answer Id should be None")


    def test_expose_failure_03(self):
        """
        This function tests if invalid path for quizzes data is provided.
        Expected functionality is that there shouldn't be any quiz details when searched for quiz id when the invalid path is provided

        This is crashing at data_loader.py, line 20, in save_data() method
        """
        # Providing invalid path for data(where quizzes are stored)
        self.ctrl = QuizzesController('a\\b\\c\\uizzes_test.json')
        # Adding the quiz with valid details
        # It is crashing for below with error ' No such file or directory: 'data\\a\\b\\c\\uizzes_test.json'
        quiz_id = self.ctrl.add_quiz("Quiz Title", "text of the quiz", datetime.now(), datetime.now() + timedelta(minutes=90))
        # fetching the quiz details based on the quiz id returned 
        quiz_details = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertIsNone(quiz_details,"Quiz should have it's details")
        
        

    def test_expose_failure_04(self):
        """
        This function tests if utf-8 characters are provided in title of the question 
        Expected functionality is that it should return valid question ID

        This is crashing at utils.py", line 11, in generate_id called by quizzes_controller.py", line #78 in add_question
        """

        # Providing the quiz details with title, text(this also contains utf-8 characters) and opening time and due time
        quiz_id = self.ctrl.add_quiz("Title", "Sampl \ud834 e Quiz", datetime.now(), datetime.now() + timedelta(minutes=90))
        # Providing the question details with title, text(this also contains utf-8 characters) and text of the question

        #this is crashing while generating the id for question since there are utf-8 characters which is not expected
        question_id = self.ctrl.add_question(quiz_id,"Question \ud834 True","Text of the question")
        self.assertIsNotNone(question_id,"question Id should not be None")



    def test_expose_failure_05(self):
        """
        This function tests the functionality if the input for title of the quiz is integer/float(i.e. None)
        Expected functionality is that the quiz ID should not be None

        This is crashing at quizzes_controller.py at line #63 in add_quiz()
        """

        # add the quiz with integer title 

        #This is crashing the application and giving error as "TypeError: unsupported operand type(s) for +: 'int' and 'str'"

        quiz1_id = self.ctrl.add_quiz(1, "Sample Quiz", datetime.now(), datetime.now() + timedelta(minutes=90))
        # So at this point the quiz id should be returned with valid value
        self.assertIsNotNone(quiz1_id, "The quiz id should not be None")



if __name__ == '__main__':
    unittest.main()