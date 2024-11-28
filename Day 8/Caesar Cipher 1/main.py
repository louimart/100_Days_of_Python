alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# def encrypt(original_text, shift_amount):
#     print(alphabet.index("z"))
#     print(f"Original text: {original_text}")
#     print(f"Shift amount: {shift_amount}")
#     encoded_text = ""

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
#     for letter in original_text:
#         print(f"list of letter: {letter}")
#         if letter == " ":
#             encoded_text += letter
#             continue
#         alphabet_index = alphabet.index(letter)
#         print(f"Alphabet_index: {alphabet_index}")
#         if alphabet_index == alphabet.index("z"):
#             alphabet_index = 0
#             shift_amount -= 1
#             print(f"adjusted shift amount: {shift_amount}")
#             shifted_letter = alphabet[alphabet_index + shift_amount]
#             print(f"Shifted_letter: {shifted_letter}")
#         else:
#             shifted_letter = alphabet[alphabet_index + shift_amount]
#             print(f"Shifted_letter: {shifted_letter}")
#         encoded_text += shifted_letter
#         print(encoded_text)

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

# encrypt(text, shift)

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text=text, shift_amount=shift)