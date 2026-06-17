import re

def parse(tokens):
    errors = []

    # very simple grammar:
    # statement → ID = expression

    pattern = r"IDENTIFIER → (\w+) OPERATOR → = NUMBER → (\d+)"

    for t in tokens.split("\n"):
        if t.startswith("IDENTIFIER") or t.startswith("KEYWORD"):
            continue

    # simple validation (demo-level parser)
    if "=" not in tokens:
        errors.append("Syntax Error: Missing '=' operator")

    return errors if errors else ["Syntax OK"]