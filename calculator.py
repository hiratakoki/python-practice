def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: 0 division"
    return a / b

def power(a, b):
    return a ** b

if __name__ == "__main__":
    print(f"3 + 5 = {add(3, 5)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"10 / 0 = {divide(10, 0)}")
    print(f"2 ** 10 = {power(2, 10)}")