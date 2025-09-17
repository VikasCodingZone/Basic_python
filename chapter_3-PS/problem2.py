#Write a program to fill in a letter temlate given below with name and date 
letter = '''Dear <|Name|>,
you are selected!
<|Date|> '''

print (letter.replace("<|Name|>","vikas").replace("<|Date|>","24 september 2025"))