# ==========================================
# Main Application: Password Generator
# ==========================================
import sys
from generator import build_character_pool, generate_password
from utils import check_strength, copy_to_clipboard, save_to_history

def get_yes_no(prompt):
    """Helper to get a boolean preference from the user."""
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        # If empty, default to Yes for convenience, or ask again? 
        # Let's be strict for clarity or default to Yes.
        # Professional standard: explicit is better.
        print("Please enter 'y' or 'n'.")

def main():
    print("===========================")
    print("   SECURE PASSWORD GEN   ")
    print("===========================")

    while True:
        # 1. Get Length
        try:
            length_input = input("\nEnter password length (8-64): ").strip()
            if not length_input:
                length = 12 # Default
            else:
                length = int(length_input)
                
            if not 4 <= length <= 128:
                print("Error: Please provide a reasonable length (4-128).")
                continue
        except ValueError:
            print("Error: Invalid number.")
            continue
            
        # 2. Get Preferences
        use_upper = get_yes_no("Include uppercase? (A-Z)")
        use_lower = get_yes_no("Include lowercase? (a-z)")
        use_digits = get_yes_no("Include numbers? (0-9)")
        use_symbols = get_yes_no("Include symbols? (!@#$)")
        exclude_ambiguous = get_yes_no("Exclude ambiguous chars? (e.g. l, 1, O, 0)")
        
        # 3. Build Pool and Generate
        try:
            pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous)
            password = generate_password(length, pool)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again and select at least one character type.")
            continue
            
        # 4. Display Result
        print("\nGenerated password:")
        print(f"   {password}   ")
        print("")
        
        # 5. Advanced Features
        strength = check_strength(password)
        print(f"Password strength: {strength}")
        
        save_to_history(password)
        
        # Clipboard
        if get_yes_no("Copy to clipboard?"):
            if copy_to_clipboard(password):
                print("Copied to clipboard! 📋")
            else:
                print("Clipboard error: 'pyperclip' module likely not installed/working.")
                
        # 6. Loop or Exit
        if not get_yes_no("\nGenerate another?"):
            print("Goodbye! Stay secure. 🔒")
            break

if __name__ == "__main__":
    main()
