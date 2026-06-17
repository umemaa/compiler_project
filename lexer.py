import re

keywords = {"int", "float", "if", "else", "while", "return"}

operators = {"=", "+", "-", "*", "/", "==", "!=", "<=", ">=", "<", ">"}

symbol_table = {}

token_specification = [
    ("NUMBER",   r'\d+(\.\d+)?'),
    ("ID",       r'[A-Za-z_][A-Za-z0-9_]*'),
    ("OP",       r'==|!=|<=|>=|[+\-*/=<>]'),
    ("SKIP",     r'[ \t]+'),
    ("NEWLINE",  r'\n'),
    ("MISMATCH", r'.'),
]

tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in token_specification)

def analyze_code(code):

    tokens = []
    errors = []
    symbol_table.clear()

    line_num = 1

    for mo in re.finditer(tok_regex, code):

        kind = mo.lastgroup
        value = mo.group()

        if kind == "NUMBER":
            tokens.append(f"NUMBER → {value}")

        elif kind == "ID":
            if value in keywords:
                tokens.append(f"KEYWORD → {value}")
            else:
                tokens.append(f"IDENTIFIER → {value}")

                if value not in symbol_table:
                    symbol_table[value] = "identifier"

        elif kind == "OP":
            tokens.append(f"OPERATOR → {value}")

        elif kind == "NEWLINE":
            line_num += 1

        elif kind == "SKIP":
            continue

        elif kind == "MISMATCH":
            errors.append(f"Lexical Error (line {line_num}) → {value}")

    symbols = "\n".join(symbol_table.keys())

    if not errors:
        errors = ["No lexical errors"]

    return (
        "\n".join(tokens),
        symbols,
        "\n".join(errors)
    )