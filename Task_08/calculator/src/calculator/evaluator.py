class Evaluator:
    def evaluate(self, parsed_expression) -> float:
        """
        Recursively evaluates a parsed expression from pyparsing.
        """
        from pyparsing import ParseResults

        # Convert ParseResults to list
        if isinstance(parsed_expression, ParseResults):
            parsed_expression = parsed_expression.asList()

        # If it’s a single number as string
        if isinstance(parsed_expression, str):
            return float(parsed_expression)

        # If it’s already a number
        if isinstance(parsed_expression, (int, float)):
            return float(parsed_expression)

        # List handling
        if isinstance(parsed_expression, list):
            # Base case: single item
            if len(parsed_expression) == 1:
                return self.evaluate(parsed_expression[0])

            current_value = self.evaluate(parsed_expression[0])
            i = 1

            # Loop safely, ensuring next index exists
            while i < len(parsed_expression) - 1:
                operator = parsed_expression[i]
                next_value = self.evaluate(parsed_expression[i + 1])

                if operator == '+':
                    current_value += next_value
                elif operator == '-':
                    current_value -= next_value
                elif operator == '*':
                    current_value *= next_value
                elif operator == '/':
                    if next_value == 0:
                        raise ZeroDivisionError("Division by zero")
                    current_value /= next_value
                elif operator == '^':
                    current_value **= next_value
                elif operator == '%':
                    if next_value == 0:
                        raise ValueError("Modulo by zero")
                    current_value %= next_value
                else:
                    raise ValueError(f"Unknown operator: {operator}")

                i += 2

            return current_value

        raise ValueError(f"Cannot evaluate expression: {parsed_expression}")
