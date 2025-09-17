#String me kuch special symbols directly use nahi kar सकते (जैसे ", ', \n, \t),
# unhe likhne के लिए हम escape sequence characters use करते हैं।

# \n → New Line (next line me le jata hai)

name = "i am belongs to bihar \nbut i am from indore "
print(name)

#\t → Tab space (4–8 spaces ka gap deta hai)
name = "name\tvikas"
name1 = "age\t20" 
print(name)
print(name1)

#\\ → Backslash print karne ke liye

name = ("This is a backslash: \\")
print(name)

#\' → Single quote print karne ke liye
name = "this is my \'pen\'"
print (name)

#\" → double quote print karne ke liye
name ="My name is \"vikas\""
print (name)

#\r → Carriage Return (line ki starting par cursor le aata hai)
name = "hello \r world"
print (name)


#Example  \n = newline , \t = tab , \ singlequote , \\ backlash
