import string
import sys
import time
import random

ALPHABET = string.ascii_uppercase


def offset(char, offset):
    return ALPHABET[(ALPHABET.index(char) + offset) % 26]


class Vigenere:
    @staticmethod
    def encrypt(message, key):
        return ''.join(
            map(offset, message, list(map(lambda x: ALPHABET.index(x), key)) * (len(message) // len(key) + 1)))

    @staticmethod
    def decrypt(ciphertext, key):
        return ''.join(map(offset, ciphertext,
                           list(map(lambda x: 26 - ALPHABET.index(x), key)) * (len(ciphertext) // len(key) + 1)))


"""
Encryption function
1. Takes user input for the message in the form of a string
    stores the whole thing as an uppercase string with spaces removed
2. Takes user input for key in the form of a string
    stores the whole thing as an uppercase string with spaces removed
3. Condition key and user_input
    a. If user_input is longer than key
        extend key to match user_input length by duplicating and concatenating
    b. If user_input is shorter than key
        truncate key to match length
    c. else something went wrong display error message & exit program with value 1
        
    
"""


def encryption():
    user_input = str(input("\nPlease enter the user_input you want to encrypt: "))
    user_input = user_input.replace(' ', '').upper()
    key_original = str(input("\nPlease enter the keyword: "))
    key_original = key_original.replace(' ', '').upper()
    key = ''
    encryption = ''

    if len(user_input) > len(key_original):
        for i in range(int(len(user_input) / len(key_original))):
            key += key_original
        key += key_original[:len(user_input) % len(key_original)]

    elif len(user_input) < len(key_original):
        key = key_original[:len(user_input)]

    elif len(user_input) == len(key_original):
        key = key_original

    else:
        print('\nHello IT, have you tried turning it off and on again?')
        sys.exit(1)

    print('\nOriginal user_input: ' + user_input)
    print('\nKeyword: ' + key_original)
    time.sleep(1)  # sleep function to make it look like the program is taking a bit
    print('\nSwapping time and space...')
    time.sleep(2)  # sleep function to make it look like the program is taking a bit
    # find() If substring exists inside the string, it returns the index of first occurrence of the substring.
    # If substring doesn't exist inside the string, it returns -1.
    for i in range(len(user_input)):
        x = alphabet.find(user_input[i])  # The character position of the user_input is saved in the alphabet
        y = alphabet.find(key[i])  # The position of the key character in the alphabet is saved
        summation = x + y  # The sum of both positions is calculated
        modulo = summation % len(alphabet)  # The sum module is calculated with respect to the length of the alphabet
        encryption += alphabet[modulo]  # The encrypted character is concatenated with 'encryption'

    print('Message Encrypted: ' + encryption)
    print()


def decryption():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = str(input("\nPlease enter the message you want to decrypt: "))
    message = message.replace(' ', '').upper()  # The message is saved in uppercase and without spaces #
    key_original = str(input("\nPlease enter a keyword: "))
    key_original = key_original.replace(' ', '').upper()  # The key is saved in uppercase and without spaces #
    key = ''
    decoded = ''
    if len(message) > len(key_original):  # If the message length is greater than that of the key ... #
        for i in range(int(len(message) / len(key_original))):  ## The key is extended, duplicating it and ##
            key += key_original  ## concatenate ##
        key += key_original[:len(message) % len(key_original)]  ## length is same as message  ##

    elif len(message) < len(key_original):  # If the length of the message is less than that of the key ...
        key = key_original[:len(message)]  # The key is truncated to have the same length as the message #

    elif len(message) == len(key_original):  # If the message length is the same as the key ... #
        key = key_original  # The password is saved as it is in 'key_original #

    else:
        print('\nHello IT, have you tried turning it off and on again?')
        sys.exit(1)

    print('Original message: ' + message)
    print('Keyword: ' + key_original)
    time.sleep(1)  # sleep function to make it look like the program is taking a bit
    print('\nI swear it\'s almost done...')
    time.sleep(2)  # sleep function to make it look like the program is taking a bit
    for i in range(len(message)):
        x = alphabet.find(message[i])  # The character position of the encrypted message is saved in the alphabet
        y = alphabet.find(key[i])  # The position of the key character in the alphabet is saved
        subtraction = x - y  # The subtraction of both positions is calculated
        modulo = subtraction % len(alphabet)  # The subtraction module is calculated with respect to the length of
        # the alphabet
        decoded += alphabet[modulo]  # The decrypted character is concatenated with 'decrypted'

    print('Decrypted message: ' + decoded)



def userInterface():
    user_choice = str(input("\nWould you like to: \n1.Encrypt\n2.Decrypt\n3.Exit Program\n> "))

    if user_choice not in ('1', '2', '3'):
        print('Invalid input.')
        userInterface()

    if user_choice == '1':
        message = str(input("\nPlease enter the message you want to decrypt: "))
        message = message.replace(' ', '').upper()  # The message is saved in uppercase and without spaces #
        key_original = str(input("\nPlease enter a keyword: "))
        key_original = key_original.replace(' ', '').upper()  # The key is saved in uppercase and without spaces #
        key = ''
        decoded = ''
        if len(message) > len(key_original):  # If the message length is greater than that of the key ... #
            for i in range(int(len(message) / len(key_original))):  ## The key is extended, duplicating it and ##
                key += key_original  ## concatenate ##
            key += key_original[:len(message) % len(key_original)]  ## length is same as message  ##

        elif len(message) < len(key_original):  # If the length of the message is less than that of the key ...
            key = key_original[:len(message)]  # The key is truncated to have the same length as the message #

        elif len(message) == len(key_original):  # If the message length is the same as the key ... #
            key = key_original  # The password is saved as it is in 'key_original #

        else:
            print('\nHello IT, have you tried turning it off and on again?')
            sys.exit(1)

        print('Original message: ' + message)
        print('Keyword: ' + key_original)

        encrypted = Vigenere.encrypt(message, key)
        print(encrypted)

    elif user_choice == '2':
        decryption()
    elif user_choice == '3':
        print('Goodbye')
        sys.exit(0)


def main():
    while True:
        userInterface()
        while True:
            answer = str(input('Do you want to run the program again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print('Invalid input.')

        if answer == 'y':
            continue
        else:
            print('Goodbye!')
            break


if __name__ == "__main__":
    main()
