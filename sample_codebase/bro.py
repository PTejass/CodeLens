import re

def check_password_strength(password=):
    # Define validation rules using regular expressions
    length_check = len(password) >= 8
    uppercase_check = re.search(r'[A-Z]', password)
    lowercase_check = re.search(r'[a-z]', password)
    digit_check = re.search(r'\d', password)
    special_check = re.search(r'[\W_]', password)
    
    # Calculate score
    checks = [length_check, uppercase_check, lowercase_check, digit_check, special_check]
    score = sum(checks)
    
    # Determine strength
    if score < 3:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"
        
    return strength, score, checks

def check_passwords_from_file(filename):
    print(f"Checking passwords in {filename}...\n")
    try:
        with open(filename, 'r') as file:
            passwords = file.readlines()
            
        for i, password in enumerate(passwords, start=1):
            pwd = password.strip()
            if not pwd:
                continue
            
            strength, score, checks = check_password_strength(pwd)
            print(f"Password {i}: {pwd} -> Strength: {strength} ({score}/5 requirements met)")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

def main():
    # 1. Interactive Password Checker
    user_pwd = input("Enter a password to test its strength (or type 'exit' to quit): ")
    if user_pwd.lower() != 'exit':
        strength, score, checks = check_password_strength(user_pwd)
        print(f"\nResult: {strength} (Score: {score}/5)")
        print(f"Details:")
        print(f"- At least 8 characters: {'✓' if checks[0] else '✗'}")
        print(f"- Uppercase letter (A-Z): {'✓' if checks[1] else '✗'}")
        print(f"- Lowercase letter (a-z): {'✓' if checks[2] else '✗'}")
        print(f"- Number (0-9): {'✓' if checks[3] else '✗'}")
        print(f"- Special character: {'✓' if checks[4] else '✗'}")

if __name__ == "__main__":
    main()
