# #  #global variable
# # x=12
# # def my_function():
# #     y=122
# #     print(x+y)

# # my_function()

# # s="12"
# # d=12+1
# # print(int(s))
# # print(str(d))
# # print(type(d))

# # #single value input
# # name=input("enter your name")
# # print("hello",name) 
# # #multiple value input
# # # y=input ("enter your name: ").split()
# # # print(y)

# # x=12
# # y=23
# # a=[12,20,23,90]

# # if(x not in a):
# #     print("not present")
# # else:
# #     print("present")
# # a=12
# # c=12
# # if(a is c):
# #     print("yes correct")

# # else:
# #     print("not correct")

# for x in "abhinaw singh":
#  print(x)

# a="hello sir!"
# print(len(a))

# txt="the best things in life are free"
# print ("free" in txt)

# if "fee" in txt:
#  print("yes")
# else:
#  print("no" not in txt)

#quotes inside quotes
# print("hey bro myself abhinaw 'singh'")
# k="abhnaw "
# print(len(k))

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(0, "orange")
# print(thislist)

# list=["abhi","singh"]
# list1=["mango","gas","king","dev"]
# list.extend(list1)
# print(list)


# x=["1","2","7","4"]
# y=[]
# for i in x:
#     print(i)
#     y.append(i)

# print(y)

# newlist=[x for x in range(10)]
# print(newlist)

# for x in range(12):
#     print(x)

#function and recursion

# def avg():
#     a=int(input("enter your number 1:"))
#     b=int(input("enter your number 2:"))
#     c=int(input("enter your number 3:"))

#     avg=(a+b+c)/3
#     print(avg)

# avg()

#factorial
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return (n * fact(n-1))

# print(f"the factorial of the number is {fact(8)}")


# def fun(nums):
#     i=0
#     for num in nums:
#         if num>i:
#             i=num
#     return i
# print(fun([12,3,4,323,212,3]))

#fereinheight to celcius
# def f_to_c() :
#  f=int(input("enter temperature in f "))
#  c=5*(f-32)/9
#  print(f"celcius ={c}deg ")

# f_to_c()

# def sum(n):

#  if n==0:
#     return 0
#  return n+sum(n-1)


# print(sum(6))

# def rem(l, word):
#     n = []
#     for item in l:
#         if item != word:
#             n.append(item.replace(word, ""))
#     return n

# l = ["abhinaw", "singh", "video", "oranges"]
# print(rem(l, "o"))



