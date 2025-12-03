# Tasks: Calculator Expression Evaluation

**Feature Spec**: specs/1-calculator-expression/spec.md
**Implementation Plan**: specs/1-calculator-expression/plan.md
**Created**: 2025-12-02

## Dependencies

- User Story 1 must be completed before User Story 2.

## Parallel Execution Opportunities

- Within each User Story phase, tasks marked with `[P]` can be executed in parallel.

## Implementation Strategy

This feature will be implemented incrementally, prioritizing the core functionality (basic arithmetic) first to deliver an MVP, followed by robust error handling and extended operations. Test-Driven Development (TDD) will be applied throughout.

## Phase 1: Setup

- [x] T001 Create project structure (`src/`, `tests/`) in the root directory
- [x] T002 Install `pyparsing` library into the project environment

## Phase 2: Foundational

- [x] T003 Define `ExpressionEvaluationResult` data structure in `src/calculator/models.py`

## Phase 3: User Story 1 - Evaluate Basic Arithmetic Expression (Priority: P1)

**Goal**: User can input a simple arithmetic expression (e.g., "2+3") and get the correct result.

**Independent Test**: Provide valid expressions; verify numerical output.

- [x] T004 [P] [US1] Implement `InputProcessor` to receive and normalize expressions in `src/calculator/input_processor.py`
- [x] T005 [P] [US1] Implement `pyparsing`-based `ParserValidator` for basic operations (+, -, *, /) and operator precedence in `src/calculator/parser_validator.py`
- [x] T006 [P] [US1] Implement `Evaluator` for basic arithmetic operations in `src/calculator/evaluator.py`
- [x] T007 [P] [US1] Implement `OutputFormatter` to present results in `src/calculator/output_formatter.py`
- [x] T008 [P] [US1] Write unit tests for `InputProcessor` in `tests/unit/test_input_processor.py`
- [x] T009 [P] [US1] Write unit tests for `ParserValidator` (basic ops) in `tests/unit/test_parser_validator_basic.py`
- [x] T010 [P] [US1] Write unit tests for `Evaluator` (basic ops) in `tests/unit/test_evaluator_basic.py`
- [x] T011 [US1] Write integration tests for User Story 1 (end-to-end basic expressions) in `tests/integration/test_basic_expressions.py`

## Phase 4: User Story 2 - Handle Invalid Expressions & Extended Operations (Priority: P2)

**Goal**: User inputs invalid expressions and receives informative errors; system correctly evaluates expressions with exponents and modulo.

**Independent Test**: Provide various invalid expressions and extended operations; verify error messages and correct numerical output.

- [x] T012 [P] [US2] Enhance `ParserValidator` to include exponents (^) and modulo (%) operators in `src/calculator/parser_validator.py`
- [x] T013 [P] [US2] Enhance `Evaluator` to handle exponents (^) and modulo (%) operations in `src/calculator/evaluator.py`
- [x] T014 [P] [US2] Enhance `ParserValidator` for invalid syntax error handling in `src/calculator/parser_validator.py`
- [x] T015 [P] [US2] Enhance `Evaluator` for mathematical error handling (e.g., division by zero) in `src/calculator/evaluator.py`
- [x] T016 [P] [US2] Write unit tests for `ParserValidator` (exponents, modulo, error cases) in `tests/unit/test_parser_validator_extended.py`
- [x] T017 [P] [US2] Write unit tests for `Evaluator` (exponents, modulo, error cases) in `tests/unit/test_evaluator_extended.py`
- [ ] T018 [US2] Write integration tests for User Story 2 (invalid expressions, extended ops) in `tests/integration/test_extended_expressions.py`

## Phase 5: Polish & Cross-Cutting Concerns

- [ ] T019 Refine error messages for user clarity across `src/calculator/*.py`
- [ ] T020 Review code for readability and adherence to Python style guides across `src/calculator/*.py`
