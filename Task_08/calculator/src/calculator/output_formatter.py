from models import ExpressionEvaluationResult

class OutputFormatter:
    def format_result(self, result: ExpressionEvaluationResult) -> str:
        """
        Formats the expression evaluation result for display.
        """
        if result.status == "SUCCESS":
            return str(result.result)
        else:
            return f"Error: {result.error_message}"

    def display(self, result: ExpressionEvaluationResult):
        """
        Prints the formatted result directly to the console.
        """
        print(self.format_result(result))


# Create a single formatter instance
formatter = OutputFormatter()

def display_result(result: ExpressionEvaluationResult):
    formatter.display(result)
