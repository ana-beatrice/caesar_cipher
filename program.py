from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift,direction):
    cipher_text = ''
    if direction == "decode":
        shift *= -1
    for char in text:
        if char not in alphabet:
            cipher_text += char
        else:
            position = alphabet.index(char)
            new_position  = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"The {direction}d text is {cipher_text}") 
        
end = True
while end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user_input = input("If you want to continue type 'yes' else type 'no'\n")
    shift =  shift % 26
    if user_input == "no":
        end = False


