import unittest
from src.calculator.parser_validator import ParserValidator
from pyparsing import ParseException

class TestParserValidatorExtended(unittest.TestCase):
    def setUp(self):
        self.parser = ParserValidator()

    def test_exponentiation(self):
        # 2 ^ 3 = 8
        self.assertEqual(self.parser.parse("2^3"), 8.0)
        # 3 ^ 2 = 9
        self.assertEqual(self.parser.parse("3^2"), 9.0)
        # 2 ^ 3 ^ 2 = 2 ^ 9 = 512 (right-associativity)
        self.assertEqual(self.parser.parse("2^3^2"), 512.0)

    def test_modulo(self):
        # 10 % 3 = 1
        self.assertEqual(self.parser.parse("10%3"), 1.0)
        # 15 % 4 = 3
        self.assertEqual(self.parser.parse("15%4"), 3.0)

    def test_combined_extended_operations(self):
        # 2 + 3 ^ 2 * 2 = 2 + 9 * 2 = 2 + 18 = 20
        self.assertEqual(self.parser.parse("2+3^2*2"), 20.0)
        # (5 + 3) % 3 = 8 % 3 = 2
        self.assertEqual(self.parser.parse("(5+3)%3"), 2.0)

    def test_invalid_syntax_error_handling(self):
        with self.assertRaisesRegex(ValueError, "Invalid expression syntax"): # Ensure specific error message
            self.parser.parse("2++3")
        with self.assertRaisesRegex(ValueError, "Invalid expression syntax"): # Ensure specific error message
            self.parser.parse("abc")
        with self.assertRaisesRegex(ValueError, "Invalid expression syntax"): # Ensure specific error message
            self.parser.parse("5 + * 3")

    def test_mathematical_error_handling_division_by_zero(self):
        with self.assertRaisesRegex(ZeroDivisionError, "Division by zero"): # Ensure specific error message
            self.parser.parse("10/0")
        with self.assertRaisesRegex(ZeroDivisionError, "Division by zero"): # Ensure specific error message
            self.parser.parse("5/(3-3)")

    def test_mathematical_error_handling_modulo_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Modulo by zero"): # Ensure specific error message
            self.parser.parse("10%0")
        with self.assertRaisesRegex(ValueError, "Modulo by zero"): # Ensure specific error message
            self.parser.parse("5%(3-3)")

if __name__ == '__main__':
    unittest.main()
