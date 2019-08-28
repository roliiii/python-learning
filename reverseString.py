message = list('1234')

i =  0
j = len(message) - 1
while i < j:
    message[i], message[j] = message[j], message[i]
    i = i + 1
    j = j - 1 

print("".join(message))