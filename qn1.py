
def validate_passwords(input_string):
 #enter comma separated value   
    passwords = [p.strip() for p in input_string.split(",")]
    valid_passwords = []

    for pwd in passwords:
        
        if len(pwd) < 6 or len(pwd) > 12:
            continue
        
        
        if not re.search("[a-z]", pwd):
            continue
            
        
        if not re.search("[A-Z]", pwd):
            continue
            
       
        if not re.search("[0-9]", pwd):
            continue
        
        if not re.search("[$#@]", pwd):
            continue
            
       
        valid_passwords.append(pwd)

    
    return ",".join(valid_passwords)

if __name__ == "__main__":
    raw_input = input("Enter passwords separated by commas: ")
    result = validate_passwords(raw_input)
    print(f"Valid Passwords: {result}")