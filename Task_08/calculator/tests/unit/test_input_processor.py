import unittest
from src.calculator.input_processor import InputProcessor

class TestInputProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = InputProcessor()

    def test_strip_whitespace(self):
        self.assertEqual(self.processor.process(" 5 + 3 "), "5 + 3")
        self.assertEqual(self.processor.process("\t10 - 4\n"), "10 - 4")

    def test_empty_string(self):
        self.assertEqual(self.processor.process(" "), "")
        self.assertEqual(self.processor.process(""), "")

    def test_valid_string_no_whitespace(self):
        self.assertEqual(self.processor.process("2*6"), "2*6")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            self.processor.process(123)  # type: ignore
        with self.assertRaises(TypeError):
            self.processor.process(None) # type: ignore

if __name__ == '__main__':
    unittest.main()
