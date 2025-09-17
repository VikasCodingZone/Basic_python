friend = ["vikas","shubham","shweta",91,2.10,True,"Pandey"]
print(friend[2])

L1 = [5,6,3,2,8,7,9,1,4]  # element ko short kar deta hai accending order me 
L1.sort()
print(L1)

L1 = [5,6,3,2,8,7,9,1,4]  # element ko revers kar deta hai
L1.reverse()
print(L1)

friend = ["vikas","shubham","shweta","Pandey"]  # list me add kiya hai new name 
friend.append("vartika")
print(friend)

L1 = [5,6,3,2,8,7,9,1,4]  # element me kahi bhi insert karva sakte hai insert method ka us karke
L1.insert(9,11)
print(L1)

friend = ["vikas","shubham","shweta","Pandey"]  # element me kahi bhi insert karva sakte hai insert method ka us karke
friend.insert(1,"Tanu")
print(friend)


friend = ["vikas","shubham","shweta","Pandey"]  # element me kahi bhi remove karva sakte hai remove method ka us karke
friend.remove("shubham")
print(friend)


friend = ["vikas","shubham","shweta","Pandey"] #Removes and returns the element at a given index (default: last).
removed = friend.pop(1)
print(friend)
print("Removed:",removed)

friend = ["vikas","shubham","shweta","Pandey"]  # all clear
friend.clear()
print(friend)

friend = ["vikas","shubham","shweta","Pandey"]  # element ki indexing batata hai 
print(friend.index("shubham"))\


L1 = [5,2,6,3,2,8,7,9,2,1,4,2]
print(L1.count(2))