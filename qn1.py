import re

def check_password_validity():
    # Get input from user
    raw_input = input("Enter passwords separated by commas: ")
    passwords = raw_input.split(",")
    
    valid_passwords = []

    for p in passwords:
        # Strip whitespace just in case the user added spaces after commas
        p = p.strip()
        
        # Check length requirements
        if len(p) < 6 or len(p) > 12:
            continue
        
        # Check for lowercase letter
        if not re.search("[a-z]", p):
            continue
            
        # Check for uppercase letter
        if not re.search("[A-Z]", p):
            continue
            
        # Check for digits
        if not re.search("[0-9]", p):
            continue
            
        # Check for special characters [$#@]
        if not re.search("[$#@]", p):
            continue
            
        # If all checks pass, add to valid list
        valid_passwords.append(p)

    # Print the result as a comma-separated string
    print(",".join(valid_passwords))

# Run the program
if __name__ == "__main__":
    check_password_validity()