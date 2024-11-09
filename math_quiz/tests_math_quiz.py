import unittest
from math_quiz import generate_random_int, select_random_operator, create_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_operator(self):
        # Test if operator selected is one of allowed operators ('+', '-', '*')
        valid_operators = ['+', '-', '*']
        for _ in range(1000):
            operator = select_random_operator()
            self.assertIn(operator, valid_operators)
        pass

    def test_create_math_problem(self):
        # Test if created math problem and solution are correct 
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7), 
            (4, 3, '*', '4 * 3', 12),
            (7, 2, '+', '7 + 2', 9),
            (6, 3, '-', '6-3', 3)
        ]

        for num1, num2, operator, expected_problem, expected_ans in test_cases:
            problem, ans = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_ans)

if __name__ == "__main__":
    unittest.main()
