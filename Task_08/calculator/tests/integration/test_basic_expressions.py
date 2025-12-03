import unittest
from src.calculator.models import ExpressionEvaluationResult
from src.calculator.input_processor import InputProcessor
from src.calculator.parser_validator import ParserValidator
from src.calculator.evaluator import Evaluator
from src.calculator.output_formatter import OutputFormatter

class TestBasicExpressionsIntegration(unittest.TestCase):
    def setUp(self):
        self.input_processor = InputProcessor()
        self.parser_validator = ParserValidator()
        self.evaluator = Evaluator()
        self.output_formatter = OutputFormatter()

    def evaluate_expression(self, expression_string: str) -> ExpressionEvaluationResult:
        result_obj = ExpressionEvaluationResult(expression_input=expression_string)
        try:
            processed_expr = self.input_processor.process(expression_string)
            parsed_expr = self.parser_validator.parse(processed_expr)
            evaluated_result = self.evaluator.evaluate(parsed_expr)
            result_obj.result = evaluated_result
            result_obj.status = "SUCCESS"
        except (ValueError, ZeroDivisionError) as e:
            result_obj.error_message = str(e)
            result_obj.status = "ERROR"
        return result_obj

    def test_addition(self):
        result = self.evaluate_expression("5+3")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 8.0)

    def test_subtraction(self):
        result = self.evaluate_expression("10-4")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 6.0)

    def test_multiplication(self):
        result = self.evaluate_expression("2*6")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 12.0)

    def test_division(self):
        result = self.evaluate_expression("15/3")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 5.0)

    def test_combined_operations_precedence(self):
        # 2 + 3 * 4 = 2 + 12 = 14
        result = self.evaluate_expression("2+3*4")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 14.0)

    def test_parentheses(self):
        # (2+3)*4 = 5 * 4 = 20
        result = self.evaluate_expression("(2+3)*4")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 20.0)

    def test_float_numbers(self):
        result = self.evaluate_expression("5.5+2.5")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, 8.0)

    def test_negative_numbers(self):
        result = self.evaluate_expression("-5+3")
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.result, -2.0)

if __name__ == '__main__':
    unittest.main()
