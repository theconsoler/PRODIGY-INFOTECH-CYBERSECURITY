def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            result += shifted_char
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        
        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Shift value must be an integer. Please try again.")
            continue
        
        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        repeat = input("Do you want to perform another operation? (yes/no): ").lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()
