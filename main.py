import sys
from calculator import Calculator

def main():
    calc = Calculator()

    if len(sys.argv) != 4:
        print("Error: Please provide three command-line arguments.")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        choice = int(sys.argv[3])
    except (ValueError, IndexError):
        print("Error: Invalid arguments.")
        sys.exit(1)

    if choice == 1:
        result = calc.add(a, b)
        print(f"Result: {result}")
    elif choice == 2:
        result = calc.subtract(a, b)
        print(f"Result: {result}")
    elif choice == 3:
        result = calc.multiply(a, b)
        print(f"Result: {result}")
    elif choice == 4:
        try:
            result = calc.divide(a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {str(e)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
