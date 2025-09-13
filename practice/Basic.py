# x=20
# y=30
# print(f"The result is:{x+y}")
# print(f"The result is:{x*y}")

#Exercise 2: Print the Sum of a Current Number and a Previous number
# k=0
# sum=0
# curr=0
# for i in range(11):
#     curr=i
#     prev=i-1
#     print(f"current number is:{curr}")
    
#     print("previous number ",prev)
#     sum=curr+prev
#     print("sum:",sum)

# wrd="abhinaw_singh"
# for i in range(len(wrd)):
#     if i%2==0:
#      print(wrd[i])
# k=len(wrd)
# print(wrd[3::])
# for i in range(3,k,1):
#     print(wrd[i])

# x=123
# last_digit=[]
# while x>0:
#     last_digit=x%10
#     print(last_digit)
#     x=x//10

#print curent and previous value
# for i in range(1,19,1):
#     curr=i
#     prev=i-1
#     print(curr,prev)

# Print characters present at an even index number
# x="abhinaw singh"
# for i in range(len(x)):
#     if i % 2 ==0:
#         print(x[i])
   

#Write a Python code to remove characters from a string from 0 to n and return a new string.
# x="abhinaw singh"
# print(x[3:])
# print(x[:3])

# Check if the first and last numbers of a list are the same
# x=[1,2,3,4,1]
# if x[0]==x[-1]:
#     print('true')
# else:
#     print("false ")
    
# Exercise 7: Find the number of occurrences of a substring in a string
# str_x = "Emma is good developer. Emma is a writer"
# x=str_x.count("Emma")
# print(x)

# exercise 8 print the pattern
# for i in range(6):
#     for x in range(i):
#         print(i,end="")
#     print("\n")

#to check the pelindrome number 
# num= input("enter the digit to check the  pelindrome")
# s=str(num)
# reverse_string=s[::-1]
# print(reverse_string)
# if(s==reverse_string):
#     print("original number is ",num)
#     print("Yes. given number is palindrome number")
# else:
#     print("original number ",num)
#     print("No. given number is not palindrome number")

#Exercise 10: Merge two lists using the following condition
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list: ", end="")
for i in range(len(list1)):
    if(list1[i]%2!=0):
     print(list1[i],end=" ")
     k=list1[i]
for i in range(len(list2)):
    if(list2[i]%2==0):
     print(list2[i],end=" ")


