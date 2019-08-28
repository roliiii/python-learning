a = [[1,2,3],[3,4,5]]
print(a[1][2]) #5

b = [1,2] + [3,4]
print(b) #[1, 2, 3, 4]
b = b*5
print(b) #[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
b += [5,6,7,8]
print(b)
b = filter(lambda x: x % 2 == 0, b)

intToString = lambda x: str(x)
b = map(intToString,b)

print("".join(b)) #242424242468