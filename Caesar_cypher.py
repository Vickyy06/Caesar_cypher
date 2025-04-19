import string

LETTERS = string.ascii_uppercase
NUM_LETTERS = len(LETTERS)

def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            index = LETTERS.find(char.upper())
            new_index = (index + key) % NUM_LETTERS
            new_char = LETTERS[new_index]
            ciphertext += new_char if is_upper else new_char.lower()
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            index = LETTERS.find(char.upper())
            new_index = (index - key) % NUM_LETTERS
            new_char = LETTERS[new_index]
            plaintext += new_char if is_upper else new_char.lower()
        else:
            plaintext += char
    return plaintext

def main():
    print("\n*** CAESAR CIPHER PROGRAM ***\n")

    choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
    
    if choice not in ('e', 'd'):
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    try:
        key = int(input("Enter the key (1-26): "))
        if not 1 <= key <= 26:
            raise ValueError
    except ValueError:
        print("Invalid key. Please enter an integer from 1 to 26.")
        return

    text = input("Enter the text: ")

    if choice == 'e':
        result = encrypt(text, key)
        print(f"\nCIPHERTEXT: {result}")
    else:
        result = decrypt(text, key)
        print(f"\nPLAINTEXT: {result}")

if __name__ == "__main__":
    main()
