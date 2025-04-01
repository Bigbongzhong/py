def bitwise_operation(a, b, op):
    if op not in {"&", "|", "^", "<<", ">>"}:
        return "Invalid operator."

    if op == "&":
        return a & b
    elif op == "|":
        return a | b
    elif op == "^":
        return a ^ b
    elif op == "<<":
        return a << b
    elif op == ">>":
        return a >> b if a >= 0 else f"Warning: Right shift of negative numbers is implementation-dependent ({a} >> {b})"

# Example usage
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
op = input("Enter bitwise operator (&, |, ^, <<, >>): ")
print(bitwise_operation(a, b, op))
