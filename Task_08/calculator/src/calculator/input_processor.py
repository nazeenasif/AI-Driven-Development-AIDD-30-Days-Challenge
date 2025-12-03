class InputProcessor:
    def process(self, expression: str) -> str:
        """
        Receives and normalizes the raw string expression.
        For now, normalization is a simple strip.
        """
        if not isinstance(expression, str):
            raise TypeError("Input expression must be a string.")
        return expression.strip()
