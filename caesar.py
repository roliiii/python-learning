
def caesar(inputString, mode='encode', key=13):

    if(mode != 'encode'):
        key = key * -1

    inputString = inputString.upper()
    translated = '' 
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key % len(LETTERS)
    for char in inputString:
        if char in LETTERS:
            index = LETTERS.find(char)

            index = index + key
            if(index < 0):
                index = len(LETTERS) + index
            elif(index >= len(LETTERS)):
                index = index - len(LETTERS)

            translated = translated + LETTERS[index]
        else:
            translated = translated + char
    return translated

def encode(inputString, key=13):
    return caesar(inputString, 'encode', key)


def decode(inputString, key=13):
    return caesar(inputString, 'decode', key)

encoded = encode('This is a secret!',200)
print(encoded)
print(decode(encoded,200))