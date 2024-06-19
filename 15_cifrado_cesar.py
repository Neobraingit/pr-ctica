'''
Codificador cifrado César:
Escribe un programa que implemente un cifrado César simple. 
'''

def caesar_cipher(text, shift):
    encrypted = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_ord = ord(char) + shift_amount
            if char.islower():
                if new_ord > ord('z'):
                    new_ord = 26
                else: 
                    if new_ord > ord('Z'):
                        new_ord -= 26
                encrypted.append(chr(new_ord))
            else:
                encrypted.append(char)
        return''.join(encrypted)
text = input('Enter a string: ')
shift = int(input('Enter the shift value: '))
encoded_text =caesar_cipher(text, shift)
print (f'The encoded text is: {encoded_text}')