#25. 3 logo me se Oldest aur Youngest nikalna
a = int(input("Pehle vyakti ki age: "))
b = int(input("Dusre vyakti ki age: "))
c = int(input("Tisre vyakti ki age: "))

print("Sabse bada (Oldest):", max(a, b, c))
print("Sabse chhota (Youngest):", min(a, b, c))


# 📖 Explanation

# User se 3 logon ki age input me li.

# a → pehle vyakti ki age

# b → dusre vyakti ki age

# c → tisre vyakti ki age

# max(a, b, c) → in teeno me se sabse bada number nikalta hai → matlab oldest.

# min(a, b, c) → in teeno me se sabse chhota number nikalta hai → matlab youngest.

# 🧠 Logic (Simple Words Me)

# max() function hamesha sabse badi value return karta hai.

# min() function hamesha sabse chhoti value return karta hai.