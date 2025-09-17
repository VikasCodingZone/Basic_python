a = (1,2,3,1,5,6,1)  # Counts how many times a value appears in the tuple.
print(a.count(1))

a1= ("vikas","ke","pass","ek","bike","hai") 
print(a1.index("bike"))#Returns the index of the first occurrence of a value.

#Built-in Functions You Can Use with Tuples

#Although tuples have only 2 direct methods, you can use many Python built-ins:

#len() → Returns length of tuple

t = (10, 20, 30)
print(len(t))   # 3


#min() / max() → Returns smallest/largest element

t = (5, 2, 8, 1)
print(min(t))   # 1
print(max(t))   # 8


#sum() → Returns sum of elements

t = (1, 2, 3, 4)
print(sum(t))   # 10


#sorted() → Returns a sorted list (not a tuple!)

t = (3, 1, 4, 2)
print(sorted(t))   # [1, 2, 3, 4]


#in operator → Checks if element exists

t = ("a", "b", "c")
print("b" in t)   # True


# So, tuple ke direct methods:

#count()

#index()
