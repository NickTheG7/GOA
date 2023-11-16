# str="some text"
# x=len(str) #---> len არის რამდენი მნიშვნელი ან ასო ან რიცხვია გამოყენებული ტექსტში ან რიცხვში, სპესებიც ითვლება, ამიტომ გამოვიდა 9.
# print(x)
#len-length-სიგრძე
#len სიაში თვლის ელემენტების რაოდენობას ან ის ითვლის string-ში სიმბოლოების რაოდენობას


# #append
# list=[1,2,3]
# list.append(21) #---> append-ი ამატებს სიის ბოლოში იმას, რასაც მივუთითებთ
# print(list)



# #0
# words.insert(1, "is") #amatebs sasurvel elements siis sasurvel poziciaze
# #სად ჩაჯდეს #რა ჩაჯდეს
# print(words)


# შექმენით სია დედიკოსგან და მამიკოსგან,

# შუაში ჩასვით თქვენი თავი,
# ხოლო ბოლოში ჩასვით კიდევ ერთი საყვარელი ადამიანი

# list=["nino","zaza"] #--->ესეთ ლისთებს სულ ვწერთ [] მსგავსი ფრცხილებით
#         #0     #1
# list.insert(1, "nikoloz")#---> ნომერი 1-ის ნაცვლად ჩაჯდება ნიკოლოზი და ზაზა გადაინაცვლებს მარჯვნივ
# list.append("sandro")
# print(list)
#append და insert-ი მუშაობს მხოლოდ [] მსგავსი ფრჩილების სიის დროს და არა ესეთი ფრჩხილებიანი სიის დროს



# #index ფუნქცია
# x=["a","r","8","op"]
# print(x.index("a"))


# #min and max
# nums=[1,2,3,4,5,6,7,8]
# res=min(nums)+max(nums)
# print(res)



# nums = [4, 5, 6]
# msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
# print(msg)



#შექმენით თქვენი ოჯახის წევრებისგან სია

# და ჩააფორმატეთ მათი სახელები ამ წინადადებაში:

# "ჩემი დედიკოა ----, ჩემი მამიკოა ----, მე ვარ  ----"

# family=["nino","zaza","nikolozi"]
# msg="NAMES: {nino} {zaza} {me}". format (family[0],family[1],family[2])