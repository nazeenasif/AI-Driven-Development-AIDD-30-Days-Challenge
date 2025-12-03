import unittest
from src.calculator.models import ExpressionEvaluationResult
from src.calculator.input_processor import InputProcessor
from src.calculator.parser_validator import ParserValidator
from src.calculator.evaluator import Evaluator
from src.calculator.output_formatter import OutputFormatter

class TestExtendedExpressionsIntegration(unittest.TestCase):
    def setUp(self):
        self.input_processor = InputProcessor()
        self.parser_validator = ParserValidator()
        self.evaluator = Evaluator()
        self.output_formatter = OutputFormatter()

    def evaluate_expression(self, expression_string: str) -> ExpressionEvaluationResult:
        result_obj = ExpressionEvaluationResult(expression_input=expression_string)
        try:
            processed_expr = self.input_processor.process(expression_string)
            # The parser_validator.parse now directly returns the evaluated result or raises an exception
            evaluated_result = self.parser_validator.parse(processed_expr)
            result_obj.result = evaluated_result
            result_obj.status = "SUCCESS"
        except (ValueError, ZeroDivisionError) as e:
            result_obj.error_message = str(e)
            result_obj.status = "ERROR"
        return result_obj

    def test_exponentiation(self):
        result = self.evaluate_expression("2^3")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 8.0)

    def test_modulo(self):
        result = self.evaluate_expression("10%3")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 1.0)

    def test_combined_extended_operations(self):
        # 2 + 3 ^ 2 * 2 = 2 + 9 * 2 = 2 + 18 = 20
        result = self.evaluate_expression("2+3^2*2")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 20.0)

        # (5 + 3) % 3 = 8 % 3 = 2
        result = self.evaluate_expression("(5+3)%3")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 2.0)

    def test_invalid_expression_syntax(self):
        result = self.evaluate_expression("2++3")
        self.assertEqual(result.status, "ERROR")
        self.assertIn("Invalid expression syntax", result.error_message)

    def test_division_by_zero(self):
        result = self.evaluate_expression("10/0")
        self.assertEqual(result.status, "ERROR")
        self.assertIn("Division by zero", result.error_message)

    def test_modulo_by_zero(self):
        result = self.evaluate_expression("10%0")
        self.assertEqual(result.status, "ERROR")
        self.assertIn("Modulo by zero", result.error_message)

if __name__ == '__main__':
    unittest.main()
