import math

def encode(message, key):
    encodedText = ''
    for col in range(key):
        i = col
        while (i<len(message)):
            encodedText = encodedText + message[i]
            i += key

    return encodedText

if __name__ == '__main__':
    key = 8
    message = 'Common sense is not so common.'
    encodedText = encode(message,key)
    print(encodedText)