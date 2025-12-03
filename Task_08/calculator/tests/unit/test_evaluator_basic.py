import unittest
from src.calculator.evaluator import Evaluator
from pyparsing import ParseException

class TestEvaluatorBasic(unittest.TestCase):
    def setUp(self):
        self.evaluator = Evaluator()

    def test_basic_addition(self):
        parsed_expr = ['5', '+', '3']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 8.0)

    def test_basic_subtraction(self):
        parsed_expr = ['10', '-', '4']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 6.0)

    def test_basic_multiplication(self):
        parsed_expr = ['2', '*', '6']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 12.0)

    def test_basic_division(self):
        parsed_expr = ['15', '/', '3']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 5.0)

    def test_division_by_zero(self):
        parsed_expr = ['10', '/', '0']
        with self.assertRaises(ZeroDivisionError):
            self.evaluator.evaluate(parsed_expr)

    def test_operator_precedence(self):
        # Pyparsing should structure this as ['2', '+', ['3', '*', '4']]
        parsed_expr = ['2', '+', ['3', '*', '4']]
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 14.0) # 2 + 12

    def test_float_numbers(self):
        parsed_expr = ['5.5', '+', '2.5']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 8.0)

    def test_single_number(self):
        self.assertEqual(self.evaluator.evaluate("123"), 123.0)
        self.assertEqual(self.evaluator.evaluate(["45.6"]), 45.6)

    def test_nested_subtraction(self):
        # (5 - 2) - 1 = 3 - 1 = 2
        parsed_expr = [['5', '-', '2'], '-', '1']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 2.0)

    def test_unary_minus_as_part_of_number(self):
        # Assuming parser treats -5 as a number token
        parsed_expr = ['-''5', '+', '3'] # Represents -5 + 3
        self.assertEqual(self.evaluator.evaluate(parsed_expr), -2.0)

if __name__ == '__main__':
    unittest.main()
