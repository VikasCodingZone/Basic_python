# Programming me string ka matlab hota hai characters ka sequence
#  (jaise "Hello", "Python123").
#String functions वो functions (ya methods) hote हैं jo string par operations karne ke काम aate हैं 
# – jaise length nikalna, uppercase/lowercase karna, replace karna, split karna, etc.

#len() → string ki length (characters ki total sankhya) deta hai

name = "vikaskushwaha"
print (len(name))

#upper() → string ko uppercase me convert karta hai
name ="vikaskushwaha"
print (name.upper())

#lower() → string ko lowercase me convert karta hai
name ="VIKASKUSHWAHA"
print (name.lower())

#capitalize() → first character ko capital bana deta hai
name ="vikaskushwaha"
print (name.capitalize())

#title() → har word ka first letter capital
name = "vikas kushwaha"
print (name.title())

#strip() → extra spaces hata deta hai
name = "    vikaskushwaha    "
print (name.strip())

#replace() → ek word ko dusre se replace karta hai

name ="i like java "
print (name.replace("java","python"))

#split() → string ko list me tod deta hai

name = "apple ,banana,mango"
print (name.split(","))

#find() → string me word ki position (index) deta hai
name= "vikaskushwaha"
print(name.find("kush"))


#count() → kitni baar word/character aaya hai
name = "vikaskushwaha"
print (name.count("a"))