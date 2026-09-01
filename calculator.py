
def add(a, b):
    """Adderar två olika tal"""
    return a + b

def subtract(a, b):
    """Subtraherar två olika tal"""
    return a - b

def multiply(a, b):
    """Multiplicerar två olika tal"""
    return a * b

def divide(a, b):
    """Dividerar två olika tal"""
    if b == 0:
        raise ValueError("Kan inte dividera med noll")
    return a / b


def main():
    import sys

    if len(sys.argv) != 4:
        print("Användning: python calculator.py <operation> <tal1> <tal2>")
        print("Operationer: add, subtract, multiply, divide")
        sys.exit(1)

    operation = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation not in operations:
        print(f"Okänd operation: {operation}")
        sys.exit(1)

    result = operations[operation](a, b)
    print(result)


if __name__ == "__main__":
    main()