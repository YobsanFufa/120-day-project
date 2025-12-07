# ==========================================
# Module: Generator
# ==========================================
# Purpose:
# Handles the logic for building the character pool and raising randomness.
# ==========================================

import random
import string

def build_character_pool(use_upper=True, use_lower=True, use_digits=True, use_symbols=True, exclude_ambiguous=False):
    """
    Constructs a string of available characters based on user preferences.
    
    Args:
        use_upper (bool): Include A-Z.
        use_lower (bool): Include a-z.
        use_digits (bool): Include 0-9.
        use_symbols (bool): Include special characters.
        exclude_ambiguous (bool): Remove confusing chars like 'I', 'l', '1', 'O', '0'.
        
    Returns:
        str: A string containing all allowed characters.
    """
    pool = ""
    
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
        
    if exclude_ambiguous:
        # Characters that look alike
        ambiguous_chars = "Il1O0" 
        for char in ambiguous_chars:
            pool = pool.replace(char, "")
            
    return pool

def generate_password(length, character_pool):
    """
    Generates a random password from the provided pool.
    
    Args:
        length (int): Desired length.
        character_pool (str): Valid characters to choose from.
        
    Returns:
        str: The generated password.
    """
    if not character_pool:
        raise ValueError("Character pool is empty! You must select at least one character type.")
        
    # random.choices is available in Python 3.6+ and allows selection with replacement
    password_chars = random.choices(character_pool, k=length)
    return "".join(password_chars)
