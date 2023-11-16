#სასტუმროში შემოდის 4 ბიჭი და გვინდა თითოეულს დავუპრინტოთ მოგესალმებით დღეში 3-ჯერ

#not advanced way
# print("hello nika")
# print("hello sandro")
# print("hello giorgi")
# print("hello mari")

# print("hello nika")
# print("hello sandro")
# print("hello giorgi")
# print("hello mari")

# print("hello nika")
# print("hello sandro")
# print("hello giorgi")
# print("hello mari")

# print("hello nika")
# print("hello sandro")
# print("hello giorgi")
# print("hello mari")

#advanced way with def-ფუნქცია
# def bichebtan_misalmeba():
#     print("hello nika")
#     print("hello sandro")
#     print("hello giorgi")
#     print("hello mari")

# print("dila")
# bichebtan_misalmeba()
# print("shuadge")
# bichebtan_misalmeba()
# print("sagamo")
# bichebtan_misalmeba()


# number 2 def
#პარამეტრი- ზოგადი სახელი (ჩვენს შემთხვევაში პარამეტრია ,,saxeli")
#არგუმენტი- კონკრეტული სახელი
# def misalmeba(saxeli, age):
#     print("mogesalmebi " +  saxeli)
#     print("Seni asakia " , age) #,იმიტომ დავწერეთ, რომ ინტეჯერი ემატებიდა. სხვანაირად შეგვეძლო დაგვეწერა print("Seni asakia " + str(age))

# misalmeba("nika", 19)
# misalmeba("sandro", 20)
# misalmeba("giorgi", 30)
# misalmeba("mari", 70)


# from turtle import*
# def draw_square():
#     for i in range(4):
#         forward(100)
#         left(90)

# def kalmis_wageba(x,y):
#     penup()
#     goto(x,y)
#     pendown()

# draw_square()
# kalmis_wageba(0,200)

# draw_square()
# kalmis_wageba(-200,200)

# draw_square()
# kalmis_wageba(-200,0)

# draw_square()
# kalmis_wageba(0,200)

# exitonclick()



#RANGES
# numbers= list(range(10))
# print(numbers)
# num=list(range(5))
# print(num[4]) #---> დაიპრნტება მე-4 ციფრი

# print(range(20)== range(0,20))#---> True
        
#in range ნიშნავს რამდენჯერ გვინდა გავუშვათ რამე კოდი ტრმინალში        

numbers=list(range(0,100, 5))
print(numbers)

