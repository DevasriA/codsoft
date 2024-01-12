import random,string

def generate(length, uppercase, digits, punctuation):
    
    chars = string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if punctuation:
        chars += string.punctuation
    
    password = ''.join(random.sample(chars, length))

    return password

def get_length():
    
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a valid positive length.")
            return get_length()
        return length
    except ValueError:
        print("Please enter a valid numeric value")
        return get_length()

def get_preferences():
    
    include_uppercase = input("Do you want to include Uppercase Letters? (y/n): ").lower() == 'y'
    include_digits = input("Include Digits? (y/n): ").lower() == 'y'
    include_punctuation = input("Include Punctuation? (y/n): ").lower() == 'y'
    
    return include_uppercase, include_digits, include_punctuation

def disp(password):

    print("\nGenerated Password: ", password)

def main():
    print("Welcome to the Password Generator.....")
    
    length = get_length()

    include_uppercase, include_digits, include_punctuation = get_preferences()

    password = generate(length, include_uppercase, include_digits, include_punctuation)
    
    disp(password)

if __name__ == "__main__":
    main()

