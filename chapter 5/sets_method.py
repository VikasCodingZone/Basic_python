# add()

# Ek element set me add karne ke liye.

s = {1, 2, 3}
s.add(4)
print(s)   # {1, 2, 3, 4}

# update()

# Multiple elements (list, tuple, set) add karne ke liye.

s = {1, 2}
s.update([3, 4, 5])
print(s)   # {1, 2, 3, 4, 5}

# remove()

# Element delete karega, agar element na mila to error dega.

s = {1, 2, 3}
s.remove(2)
print(s)   # {1, 3}

# discard()

# Remove karega, lekin agar element na ho to error nahi dega.

s = {1, 2, 3}
s.discard(5)   # no error
print(s)       # {1, 2, 3}

# pop()

# Random element hata kar return karega.

s = {10, 20, 30}
x = s.pop()
print(x)   # 10 (randomly remove hota hai)
print(s)   # {20, 30}

# clear()

#Set ko empty kar dega.

s = {1, 2, 3}
s.clear()
print(s)   # set()

# union()

# Do sets ka union (combine) karega.

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))   # {1, 2, 3, 4, 5}

# intersection()

# Common elements nikalta hai.

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))   # {2, 3}

#  difference()

# Jo elements pehle set me hain lekin dusre me nahi.

a = {1, 2, 3, 4}
b = {2, 4}
print(a.difference(b))   # {1, 3}
# 10. issubset() / issuperset()

# Check karta hai ki ek set dusre me included hai ya nahi.

a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))    # True
print(b.issuperset(a))  # True