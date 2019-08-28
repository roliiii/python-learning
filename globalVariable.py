valami = 'This is a global string'

def a():
    print(valami)

def b():
    valami='local'
    print(valami)

def c():
    global valami
    valami = 'sajt'
    print(valami)

print(valami) 
a()
print(valami)
b()
print(valami)
c()
print(valami)

#result:
#This is a global string
#This is a global string
#This is a global string
#local
#This is a global string
#sajt
#sajt