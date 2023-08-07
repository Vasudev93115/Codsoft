import random
import string

def generate_password(length=12, complexity="medium"):
    characters = ""

    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    password_length = int(input("Enter the desired password length: "))
    
    print("\nComplexity Levels:")
    print("1. Low (Letters and Digits)")
    print("2. Medium (Letters, Digits, and Punctuation)")
    print("3. High (Letters, Digits, Punctuation, and Whitespace)")
    complexity_choice = int(input("Choose the complexity level (1/2/3): "))
    
    complexity_mapping = {
        1: "low",
        2: "medium",
        3: "high"
    }
    
    complexity = complexity_mapping.get(complexity_choice, "medium")
    
    password = generate_password(password_length, complexity)
    
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
