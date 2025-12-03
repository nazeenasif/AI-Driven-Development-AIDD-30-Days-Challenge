from pyparsing import infixNotation, opAssoc, Word, alphanums, Suppress, ParseException

class ParserValidator:
    def __init__(self):
        number = Word(alphanums + ".")
        
        # Just define the operators and precedence, no lambdas
        self.expression = infixNotation(number, [
            (Suppress("^"), 2, opAssoc.RIGHT),
            (Suppress("*"), 2, opAssoc.LEFT),
            (Suppress("/"), 2, opAssoc.LEFT),
            (Suppress("+"), 2, opAssoc.LEFT),
            (Suppress("-"), 2, opAssoc.LEFT),
            (Suppress("%"), 2, opAssoc.LEFT),
        ])

    def parse(self, expression_string: str):
        try:
            return self.expression.parse_string(expression_string, parse_all=True)[0]
        except ParseException as e:
            raise ValueError(f"Invalid expression syntax: {e}")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred during parsing: {e}")
