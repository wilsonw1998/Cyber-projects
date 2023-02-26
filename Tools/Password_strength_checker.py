import re

# Function to check password strength
def check_password_strength(password):
    # Define regex patterns
    uppercase_pattern = re.compile('[A-Z]')
    lowercase_pattern = re.compile('[a-z]')
    digit_pattern = re.compile('[0-9]')
    special_char_pattern = re.compile('[^A-Za-z0-9]')

    # Check length
    if len(password) < 8:
        return "Password is too short. Must be at least 8 characters long."

    # Check complexity
    if not uppercase_pattern.search(password):
        return "Password is too simple. Must contain at least one uppercase letter."
    if not lowercase_pattern.search(password):
        return "Password is too simple. Must contain at least one lowercase letter."
    if not digit_pattern.search(password):
        return "Password is too simple. Must contain at least one number."
    if not special_char_pattern.search(password):
        return "Password is too simple. Must contain at least one special character."

    # Check for common phrases
    common_phrases = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "111111", "123123", "admin", "letmein", "welcome", "monkey", "password1", "sunshine", "master", "princess", "baseball", "shadow", "123456789a", "dragon", "football", "iloveyou", "123456a", "1234567a", "asdfgh", "admin123", "letmein123", "666666", "sunshine123", "password123", "123qwe", "welcome123", "superman", "batman", "trustno1", "1234qwer", "michael"]
    for phrase in common_phrases:
        if phrase in password.lower():
            return "Password is too common. Please choose a different password."

    # Password meets all criteria
    return "Password is strong."

# Prompt user to enter password
password = input("Enter password: ")

# Check password strength
strength = check_password_strength(password)
print(strength)
