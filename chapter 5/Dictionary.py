#Dictiontery is  a collection of key value pairs
my_dict ={} # empty dictionary
my_dict ={ "vikas":78,  #vikas is a key and 78 is a value
        "shubham":80, #It is a mutable,It is a unordered,It is a indexed
        "shweta":82,
        "vartika":84,
        786:"Number"


}
# print(my_dict)
# print(my_dict.values()) #return a list of value 78,80,82..
# print(my_dict.items()) # return a list of (key,value)tuple
print(my_dict.get("vikas")) #print none
print(my_dict["vikas"]) #print return error
# print(my_dict.keys())#return a list of count dictioary keys like vikas,shubham,shweta
# print(my_dict.pop("shweta"))# Remove by key
# my_dict.update({"vikas":88,"Tanu":98})
# print(my_dict)

# my_dict = {
#     "name": "Vikas",
#     "age": 21,
#     "city": "Indore"
# }
# print(my_dict["name"])
# print(my_dict.get("age"))

# my_dict["age"] = 22          # Update
# my_dict["college"] = "IPS"   # Add new key-value pair
# print(my_dict)

# my_dict.pop("city")     # Remove by key
# my_dict.popitem()       # Remove last inserted
# del my_dict["age"]      # Delete by key
# print(my_dict) 

# student = {"name": "Vikas", "age": 21, "marks": 88}

# print(student.keys())     # dict_keys(['name', 'age', 'marks'])
# print(student.values())   # dict_values(['Vikas', 21, 88])
# print(student.items())    # dict_items([('name','Vikas'), ('age',21), ('marks',88)])
# student.update["age"]=25
# print(student)

