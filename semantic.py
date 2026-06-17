def semantic_analysis(tokens):
    declared = set()
    errors = []

    for line in tokens.split("\n"):
        if "IDENTIFIER →" in line:
            name = line.split("→")[1].strip()
            declared.add(name)

    if len(declared) == 0:
        errors.append("Semantic Error: No variables declared")

    return errors if errors else ["Semantic OK"]