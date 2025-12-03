from input_processor import InputProcessor
from parser_validator import ParserValidator
from evaluator import Evaluator
from output_formatter import display_result
from models import ExpressionEvaluationResult

def main():
    raw_expression = input("Enter expression (e.g., 2 + 5 * 3): ")

    # Process input
    processor = InputProcessor()
    expression = processor.process(raw_expression)

    # Parse & validate
    validator = ParserValidator()
    parsed = validator.parse(expression)

    # Evaluate
    evaluator = Evaluator()
    try:
        evaluation = evaluator.evaluate(parsed)
        result = ExpressionEvaluationResult(
            expression_input=raw_expression,   # <-- REQUIRED
            result=evaluation,
            status="SUCCESS",
            error_message=None
        )
    except Exception as e:
        result = ExpressionEvaluationResult(
            expression_input=raw_expression,   # <-- REQUIRED
            result=None,
            status="ERROR",
            error_message=str(e)
        )

    # Display result
    display_result(result)

if __name__ == "__main__":
    main()
