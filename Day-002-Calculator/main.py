# ==========================================
# Main Application: CLI Calculator
# ==========================================
# Purpose:
# User interface for the calculator. Handles input parsing and history logging.
# ==========================================

from operations import add, subtract, multiply, divide, power, sqrt
import datetime

HISTORY_FILE = "Day-002-Calculator/history.txt"

def log_history(entry):
    """Appends the calculation string to the history file with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_entry = f"[{timestamp}] {entry}\n"
    
    # Try local path if main path fails (versatility for different running contexts)
    try:
        with open(HISTORY_FILE, "a") as f:
            f.write(formatted_entry)
    except FileNotFoundError:
         with open("history.txt", "a") as f:
            f.write(formatted_entry)

def get_number(prompt):
    """Helper to get a float number from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    print("===========================")
    print("   PROFESSIONAL CALC V1   ")
    print("===========================")
    print("Options: add, sub, mul, div, pow, sqrt, exit")

    while True:
        choice = input("\nEnter operation: ").strip().lower()
        
        if choice == 'exit':
            print("Goodbye! 👋")
            break
            
        if choice not in ['add', 'sub', 'mul', 'div', 'pow', 'sqrt']:
            print("Invalid operation. Try again.")
            continue
            
        try:
            if choice == 'sqrt':
                num = get_number("Enter number: ")
                result = sqrt(num)
                equation = f"√{num} = {result}"
            else:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                
                if choice == 'add':
                    result = add(num1, num2)
                    equation = f"{num1} + {num2} = {result}"
                elif choice == 'sub':
                    result = subtract(num1, num2)
                    equation = f"{num1} - {num2} = {result}"
                elif choice == 'mul':
                    result = multiply(num1, num2)
                    equation = f"{num1} * {num2} = {result}"
                elif choice == 'div':
                    result = divide(num1, num2)
                    equation = f"{num1} / {num2} = {result}"
                elif choice == 'pow':
                    result = power(num1, num2)
                    equation = f"{num1} ^ {num2} = {result}"

            print(f"Result: {result}")
            log_history(equation)
            
        except ValueError as e:
            print(f"Math Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
