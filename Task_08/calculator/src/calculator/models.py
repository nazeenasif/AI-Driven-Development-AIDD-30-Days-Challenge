from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ExpressionEvaluationResult:
    expression_input: str
    result: Optional[float] = None
    error_message: Optional[str] = None
    status: str = "SUCCESS"
