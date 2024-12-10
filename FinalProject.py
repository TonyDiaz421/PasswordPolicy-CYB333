# This program asks the user to enter a password and checks
# whether it meets a simple password policy.
# The policy includes:
# - Minimum and maximum length
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit
# - At least one special character from a defined set

# Define the minimum allowed length for the password
password_min_length = 8    # The password must be at least 8 characters long
# Define the maximum allowed length for the password
password_max_length = 16   # The password must be no more than 16 characters long

# Define what we consider a "special character"
special_characters = "!@#$%^&*()-_=+[]{};:,.<>/?|\\`~"  # Common set of special chars

def is_password_compliant(password: str) -> bool:
    # Check if the password is at least the minimum length
    if len(password) < password_min_length:
        # If it's too short, return False right away
        return False
    # Check if the password exceeds the maximum length
    if len(password) > password_max_length:
        # If it's too long, return False right away
        return False
   
    # Initialize checks to False. We'll turn them True if we find matches.
    has_upper = False   # Will turn True if we find an uppercase letter
    has_lower = False   # Will turn True if we find a lowercase letter
    has_digit = False   # Will turn True if we find a digit
    has_special = False # Will turn True if we find a special character
   
    # Loop through each character in the password
    for char in password:
        # Check if the character is uppercase
        if char.isupper():
            has_upper = True
        # Check if the character is lowercase
        if char.islower():
            has_lower = True
        # Check if the character is a digit
        if char.isdigit():
            has_digit = True
        # Check if the character is in our list of special characters
        if char in special_characters:
            has_special = True

    # After checking all characters, ensure all conditions are met:
    # If any of these is False, it means the password failed that requirement.
    if not has_upper:
        return False
    if not has_lower:
        return False
    if not has_digit:
        return False
    if not has_special:
        return False
   
    # If we reach this point, it means all checks passed
    return True

# Main part of the program
if __name__ == "__main__":
    # Prompt the user to input a password
    user_password = input("Enter a password: ")
   
    # Check if the password meets the policy
    if is_password_compliant(user_password):
        # If it does, print a success message
        print("Your password meets the policy requirements!")
    else:
        # If it doesn't, print a failure message
        print("Your password does NOT meet the policy requirements.")