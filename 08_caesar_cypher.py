"""
## paint area calculator
##
import math
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

## Prime number checker
##
import math
def prime_checker(number):
    is_prime = True
    for i in range(2, math.floor(number/2)):
        if number % i == 0:
            is_prime = False
            print(f"The number's lowest common denominator is {i}")
            break
    if is_prime:
        print("the number is prime")

n = int(input("Check this number: "))
prime_checker(number=n)
"""
## Caesar's cipher
##
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

""""
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text = cipher_text + alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    decipher_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        decipher_text = decipher_text + alphabet[new_position]
    print(f"The encoded text is {decipher_text}")
"""

def caesar(input_text, shift_amount, cipher_direction):
    output_text = ""
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
            if cipher_direction == "decode":
                new_position = position - shift_amount
            output_text = output_text + alphabet[new_position]
        else:
            output_text = output_text + char
    print(f"Here's the {direction}d result: {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again.")
    if result != "yes":
        should_continue = False
