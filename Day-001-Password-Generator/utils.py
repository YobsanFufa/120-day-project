# ==========================================
# Module: Utilities
# ==========================================
# Purpose:
# Contains helper functions that support the main application.
# - Password strength estimation
# - Clipboard operations (using pyperclip)
# - Saving history to a file
# ==========================================

import math
import datetime

# Try to import pyperclip, but handle the case where it might not be installed.
try:
    import pyperclip
    HAS_CLIPBOARD = True
except ImportError:
    HAS_CLIPBOARD = False

def check_strength(password):
    """
    Estimates the strength of a password based on length and character variety.
    
    Args:
        password (str): The password to analyze.
        
    Returns:
        str: "Weak", "Medium", "Strong", or "Very Strong"
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    # Calculate variety score (0-4)
    variety_score = sum([has_upper, has_lower, has_digit, has_special])

    # Basic logic for strength classification
    if length < 8 or variety_score < 2:
        return "Weak ⚠️"
    elif length < 12 or variety_score < 3:
        return "Medium 😐"
    elif length < 16 or variety_score < 4:
        return "Strong 💪"
    else:
        return "Very Strong 🔥"

def copy_to_clipboard(text):
    """
    Copies the provided text to the system clipboard.
    
    Args:
        text (str): String to copy.
        
    Returns:
        bool: True if successful, False otherwise.
    """
    if HAS_CLIPBOARD:
        try:
            pyperclip.copy(text)
            return True
        except Exception:
            return False
    return False

def save_to_history(password):
    """
    Appends the password to a history file with a timestamp.
    
    Args:
        password (str): The generated password.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {password}\n"
    
    try:
        with open("Day-001-Password-Generator/history.txt", "a") as f:
            f.write(entry)
    except FileNotFoundError:
        # If running from inside the directory, try local path
         with open("history.txt", "a") as f:
            f.write(entry)
