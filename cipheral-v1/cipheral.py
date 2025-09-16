# cipheral written by mahmutefedara

import pyfiglet

ascii_banner = pyfiglet.figlet_format("+Cipheral+")
print(ascii_banner)

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        elif char in alphabet:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char  # harf değilse direkt ekle
    print('----------------------')
    print('Plain text:', message)
    print('Encrypted/Decrypted text:', encrypted_text)
    print('----------------------')

try:
    while True:
        choice = input("Choose an option ('d' for decryption, 'e' for encryption or 'q' to quit): ")
        if any(c.isdigit() for c in choice):
            print('⚠️ Text should not contain numbers!')
            continue
        if choice not in ('d', 'e', 'q'):
            print('⚠️ Please choose an option!')
            continue
        if choice == 'q':
            print("Goodbye 👋")
            break
        text = input("Enter your text (or 'q' to quit): ")
        if text.lower() == 'q':
            print("Exiting Caesar Cipher... Goodbye!")
            break
        if text == '':
            print("⚠️ Please enter a character to encrypt or 'q' to quit.")
            continue
        if text.isdigit():
            print('⚠️ Please enter a string or "q" to quit.')
            continue
        if any(ch.isdigit() for ch in text):
            print('⚠️ Text should not contain numbers!')
            continue
        try:
            shift = int(input("Enter your shift: "))
        except ValueError:
            print("⚠️ Please enter a valid number for shift.")
            continue

        if choice == 'd':
            shift = -shift

        caesar(text, shift)
        a = input('Do you wish to continue? (y/n): ').lower()
        if a != 'y':
            print("Goodbye 👋")
            break

except KeyboardInterrupt:
    print("\nGoodbye!")
