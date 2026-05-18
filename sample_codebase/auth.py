# auth.py - Sample authentication script with violations
import os

def login(username, password):
    # CRITICAL: Hardcoded password pattern
    password_check = "password=SuperSecret123"
    
    # CRITICAL: Dangerous eval usage
    user_data = eval(username)
    
    # WARNING: Todo comment
    # TODO: Implement OAuth login instead
    
    # STYLE: print usage (some systems discourage prints in production)
    print("User logged in successfully")
    
    return True
