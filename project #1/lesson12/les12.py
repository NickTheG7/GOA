# my_str="nika is the CEO of GOA"
# if " " in my_str:
#     print (my_str.replace(" ",""))



my_str="nika is the CEO of GOA"
new_str=""
for char in my_str:
    if char != " ":
        new_str += char
print(new_str)
