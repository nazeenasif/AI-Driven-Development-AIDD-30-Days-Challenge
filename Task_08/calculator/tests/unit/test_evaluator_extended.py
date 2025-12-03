import unittest
from src.calculator.evaluator import Evaluator

class TestEvaluatorExtended(unittest.TestCase):
    def setUp(self):
        self.evaluator = Evaluator()

    def test_exponentiation(self):
        parsed_expr = ['2', '^', '3']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 8.0)
        parsed_expr = ['3', '^', '2']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 9.0)
        # Right-associativity for exponentiation is handled by pyparsing, so we expect
        # it to be parsed as ['2', '^', ['3', '^', '2']]
        parsed_expr_nested = ['2', '^', ['3', '^', '2']]
        self.assertEqual(self.evaluator.evaluate(parsed_expr_nested), 512.0)

    def test_modulo(self):
        parsed_expr = ['10', '%', '3']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 1.0)
        parsed_expr = ['15', '%', '4']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 3.0)

    def test_division_by_zero_error(self):
        parsed_expr = ['10', '/', '0']
        with self.assertRaisesRegex(ZeroDivisionError, "Division by zero"):
            self.evaluator.evaluate(parsed_expr)
        # Test with sub-expression resulting in zero
        parsed_expr_nested = ['5', '/', ['3', '-', '3']]
        with self.assertRaisesRegex(ZeroDivisionError, "Division by zero"):
            self.evaluator.evaluate(parsed_expr_nested)

    def test_modulo_by_zero_error(self):
        parsed_expr = ['10', '%', '0']
        with self.assertRaisesRegex(ValueError, "Modulo by zero"):
            self.evaluator.evaluate(parsed_expr)
        # Test with sub-expression resulting in zero
        parsed_expr_nested = ['5', '%', ['3', '-', '3']]
        with self.assertRaisesRegex(ValueError, "Modulo by zero"):
            self.evaluator.evaluate(parsed_expr_nested)

    def test_combined_extended_operations_eval(self):
        # 2 + 3 ^ 2 * 2 = 2 + 9 * 2 = 2 + 18 = 20
        parsed_expr = ['2', '+', ['3', '^', '2'], '*', '2'] # Pyparsing structure for this
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 20.0)

        # (5 + 3) % 3 = 8 % 3 = 2
        parsed_expr = [['5', '+', '3'], '%', '3']
        self.assertEqual(self.evaluator.evaluate(parsed_expr), 2.0)

if __name__ == '__main__':
    unittest.main()
