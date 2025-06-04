import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("Include both uppercase and lowercase letters.")

    # Digits
    if re.search(r'\d', password):
        strength += 1
    else:
        remarks.append("Include at least one digit.")

    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        remarks.append("Include at least one special character (!@#$%^&* etc.).")

    # Output based on strength score
    levels = {
        4: "Very Strong",
        3: "Strong",
        2: "Moderate",
        1: "Weak",
        0: "Very Weak"
    }

    return levels[strength], remarks

# Example usage
if __name__ == "__main__":
    user_input = input("Enter your password: ")
    result, tips = check_password_strength(user_input)
    print(f"Password Strength: {result}")
    if tips:
        print("Suggestions:")
        for tip in tips:
            print(f"- {tip}")
