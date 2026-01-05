import re

def check_password_validity():
 
    raw_input = input("Enter passwords separated by commas: ")
    passwords = raw_input.split(",")
    
    valid_passwords = []

    for p in passwords:
  
        p = p.strip()
        
       
        if len(p) < 6 or len(p) > 12:
            continue
        
       
        if not re.search("[a-z]", p):
            continue
            
      
        if not re.search("[A-Z]", p):
            continue
            
       
        if not re.search("[0-9]", p):
            continue
            
      
        if not re.search("[$#@]", p):
            continue
            
       
        valid_passwords.append(p)

   
    print(",".join(valid_passwords))


if __name__ == "__main__":
    check_password_validity()