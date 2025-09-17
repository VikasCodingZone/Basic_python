#🔸Typecasting ka matlab hota hai ek data type ko
#  doosre data type me badalna (convert karna)
a = 91
t = type(a) #<class 'int'>
print(t)

c ="91.5"
d= float(c) # < class 'float'>
s =type(d)
print(s)

#convert to integer
a = "123"
b = int(a)
print(b + 1)  # Output: 124

#convert to float 
a = "3.14"
b = float(a)
print(b + 1)  # Output: 4.14

#convert to string
a = 10
b = str(a)
print(b + "1")  # Output: 101

#🔹 list(), tuple(), set() → list/tuple/set me badalne ke liye
s = "hello"
print(list(s))  # output ['h', 'e', 'l', 'l', 'o']
