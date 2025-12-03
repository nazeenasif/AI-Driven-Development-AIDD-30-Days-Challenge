import unittest
from src.calculator.parser_validator import ParserValidator
from pyparsing import ParseException

class TestParserValidatorBasic(unittest.TestCase):
    def setUp(self):
        self.parser = ParserValidator()

    def test_basic_addition(self):
        parsed = self.parser.parse("5+3")
        self.assertEqual(parsed.as_list(), ['5', '+', '3'])

    def test_basic_subtraction(self):
        parsed = self.parser.parse("10-4")
        self.assertEqual(parsed.as_list(), ['10', '-', '4'])

    def test_basic_multiplication(self):
        parsed = self.parser.parse("2*6")
        self.assertEqual(parsed.as_list(), ['2', '*', '6'])

    def test_basic_division(self):
        parsed = self.parser.parse("15/3")
        self.assertEqual(parsed.as_list(), ['15', '/', '3'])

    def test_operator_precedence_multiplication_then_addition(self):
        parsed = self.parser.parse("2+3*4")
        # Pyparsing should structure this as ['2', '+', ['3', '*', '4']]
        self.assertEqual(parsed.as_list(), ['2', '+', ['3', '*', '4']]))

    def test_operator_precedence_parentheses(self):
        # For this basic parser, explicit parentheses are handled implicitly by pyparsing's structure
        # Let's test a scenario where precedence is changed by implicit grouping
        parsed = self.parser.parse("(2+3)*4")
        self.assertEqual(parsed.as_list(), [['2', '+', '3'], '*', '4'])

    def test_invalid_expression_syntax(self):
        with self.assertRaises(ValueError):
            self.parser.parse("2++3")
        with self.assertRaises(ValueError):
            self.parser.parse("abc")
        with self.assertRaises(ValueError):
            self.parser.parse("5 + * 3")

    def test_float_numbers(self):
        parsed = self.parser.parse("5.5+2.5")
        self.assertEqual(parsed.as_list(), ['5.5', '+', '2.5'])

    def test_negative_numbers(self):
        parsed = self.parser.parse("-5+3")
        # Pyparsing might parse -5 as a number directly or as unary minus.
        # For `infix_notation` with `Word(alphanums + ".")`, it treats `-5` as a number.
        self.assertEqual(parsed.as_list(), ['-''5', '+', '3'])

if __name__ == '__main__':
    unittest.main()
