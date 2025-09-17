#string is a sequence of characters enclosed quotes
#string is a data type in python..
name = "vikas" 
print(name)
 
 # Ab kuch example ...
a = 'Vikas' #single quotes string
b = "vikas" #double quotes string
c = '''vikas''' #triple quotes string means multiple line of string like poem
print(a)
print(b)
print(c)

nameshort = name[0:3] #index 0 to 3 last wala number consider nahi hoga 
# ex deeta hu man lo "vikas" ki length hai 5  to use numbering kuch yese karenge 0 1 2 3 4 or aager 
# piche se karna ho tub numbering nagetive chalega -5 -4 -3 -2 -1
nameshort2 = name[-5 : -1]
nameshort3 = name[1:5] 
print (nameshort)
print (nameshort2)
print (nameshort3)
print (nameshort3[:3])#is same as print (nameshort3[0:3]) jaha jage khali hai mtlb vo uski lenght hai..
print (nameshort3 [1:])#is same as print (nameshort3[1:5])

#slicing with skip value 
word = "amazing"
word[0:4:2]
print (word)