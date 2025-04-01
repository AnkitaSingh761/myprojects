# Fruit = ["mango","apple","kiwi","banana"]
# print(Fruit)

# name = ["rahul","aman","vinay","aadi"]
# print("Hello",name[0])

# name =["aman","ajay",22,12.4,"sahil"]
# print(name[1][3])


# name = []
# name.append("apple")
# name.append("mango")
# name.append("kiwi")
# name.append("pear")
# print(name)

# name = [23,54,76,87,12]
# name.pop(3)
# print(name)

# list = ["apple","mango","banana"]
# list.append("kiwi")
# print(list)



# tsb=[["Ankita",21],["pardeep",99],["komal",55]]
# print(tsb[0][0][0])


# li=["apple","mango","banana"]
# for i in range(len(li)):
#     print("hello",li[i])


# CHECK A VALUE to PRESENT IN A LIST?
# name = ["apple","banana","kiwi","pear","orange"]
# print("kiwi" in name)


# name = ["amit","ajay","adit","sonal"]
# count=0
# for i in range(len(name)):
#     if name[i]=="adit":
#         print("mil gyaa")
#         # print(name[i])
#     else:
#         count+=1
#         if len(name)==count:
#             print("nhi mila")


# num = [2,4,6,7,9,5]
# count = 0
# for i in range(len(num)):
#     if num[i]== 8:
#         print("true")
#     else:
#         count+=1
#         if len(num)==count:
#             print("false")

# num = [0,1,3,0,4,0,8,0]
#  print(num.count(0))
# count=0
# for i in range(len(num)):
#     if num[i]==0:
#         count+=1
# print(count)


# num = [2,4,5,3,2,5,5,6,3,4,8,6,7]
# count = 0
# for i in range(len(num)):
#     if num[i]==6:
#         count+=1
# print(count)

# num =[2,4,8,6]
# sum = 0
# for i in range(len(num)):
#     sum+=num[i]  
# print(sum)

# li = [1,2,0,4,0,4,7]
# li.sort()
# li.reverse()
# c=li.count(0)
# for i in range (c):
#     li.pop() 
# print(li)


#Find the smallest number in given a list.....
# li = [6,9,67,34,43,8,97]
# snum = li[0]
# for  i in li:
#     if i< snum:
#         snum = i
# print(snum)

# list = [7,9,67,34,43,8,97]
# smallnum = min(list)
# print(smallnum)


# list = [3,54,6,8,56,97,67,43]
# larnum = list[0]
# for i in list:
#     if i > larnum:
#         larnum = i
# print(larnum)

# li = [3,45,65,87,39,74,57]
# largenum = max(li)
# print(largenum)


# list = [4,5,8,3,7,9]
# count = 0
# for i in range(len(list)):
#     if list[i] == 55:
#         print("mil gya")
#     else:
#         count+=1
#         if len(list)==count:
#           print("nhi mila")



# list = [2,4,6,8,9,5]
# cou = list.count(4)
# num = 0
# for i in range (len(list)):
#     if list[i]==88:
#         temp=list[i]
#         list[i]=list[len(list)-1]
#         list[len(list)-1]=temp
#         list.pop()
#         break
#         print("find value")
#     else:
#         num+=1
#         if len(list)==num:
#          print("not find")
    
# print(list)

# list = []
# name = input("enter a name:")
# age = input("enter a age:")
# list.append([name,age])

# name = input("enter a name:")
# age = int(input("enter a age:"))
# list.append([name,age])

# name = input("enter a name:")
# age = int(input("enter a age:"))
# list.append([name,age])

# print("list:",list)


# list = []
# for i in range (1,5):
#     li=[]
#     name = input("enter a name:")
#     age = input("enter a age:")
#     li.append(name)
#     li.append(age)
#     list.append(li)

# print(list)

# userinput= int(input("Enter details of studets"))
# list = []
# for i in range (0,userinput):
#     li = []
#     name = input("enter a name:")
#     age = input("enter a age:")
#     con = input("enter a number:")
#     gen = input("enter a gen:")
#     li.append(name)
#     li.append(age)
#     li.append(con)
#     li.append(gen)
#     list.append(li)
# print(list)



# list = []
# for i in range(1,101):
#     if i%2==0:
#         list.append(i) 
             
# print(list)

# list = []
# for i in range(1,101):
#     if i > 1:
#         for j in range(2,i):
#                 if i%j==0:
#                         break
#         else:
#                 list.append(i)
# print(list)



# list = [2,4,6,7,8,56,87,98,34,23,54,77]
# li=[]

# for i in range(len(list)):
#     if list[i]%2==1:
#         li.append(list[i])
# list=li
# print(list)
# 
        
# num=1
# num2=3
# for i in range(1,25):
#    print(num)
#    print(num2)
#    num2+=1
#    num+=1
#    print(num)
#    print(num2)
#    num2+=3
#    num+=3


# FIND SUM OF ALL THE ITEMS IN A LIST.......
# num = [3,4,5,8,9,2]
# sum = 0
# for i in range(len(num)):
#     sum+=num[i]
# print(sum)

# WRITE A PROGRAM MULTIPLY ALL ITEMS IN A LIST......
# num = [3,2,5,4,8]
# multi = 1
# for i in range(len(num)):
#     multi*= num[i]
# print(multi)

# TO GET THE LARGEST NUMBER FROM THE LIST.........
# num = [3,54,65,87,35,54]
# lnumber = num[0]
# for i in num:
#      if i > lnumber:
#         lnumber = i
# print(lnumber)


#  TO GET THE SMALLEST NUMBER FROM THE LIST......
# list = [87,56,34,65,98,34]
# snumber = list[0]
# for i in list:
#     if i < snumber:
#         snumber = i
# print(snumber)


# WRITE A PYTHON PROGRAM TO REMOVE DUPLICATE FROM A LIST.......
# list = [2,4,64,6,7,4,6,4,8,9]     #NOT SOLVE ANSWER
# unique = []
# for i in list:
#     if i not in unique: 
#         unique.append(i)
#         unique = list
# print(unique)





#  TO CHECK IF A LIST IS EMPTY OR NOT..........
# list = []
# if not list:
#   print("list empty")
# else:
#     print("not empty")


# WRITE PROGRAM TO CLONE OR COPY A LIST..........
# list  = [2,4,6,3,9,7,]
# a = list.copy()
# print(a)
# print(list)




# list = [ ["a",1,"m"],
#         ["b",2,"f"],
#         ["c",3,"m"],
#         ["d",4,"f"]]
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         print(list[i][j], end = " ")
#     print()
# print(list)



# li = [[["x",2,"f"],["y",3,"f"],["z",4,"m"]],
#       [["a",5,"f"],["b",6,"m"],["c",7,"f"]],
#       [["p",8,"m"],["q",9,"f"],["r",8,"m"]],
#       [["j",2,"m"],["k",4,"m"],["l",6,"f"]]]
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         for k in range(len(li[j])):
#             print(li[i][j][k], end = " ")
#         print()
#     print()
# print(li)




# li = [[["x",2,"f"],["y",3,"f"],["z",4,"m"]],
#        [["a",5,"f"],["b",6,"m"],["c",7,"f"]],
#        [["p",8,"m"],["q",9,"f"],["r",8,"m"]],
#        [["j",2,"m"],["k",4,"m"],["l",6,"f"]]]
# findvalue = "z"
# newvalue = "aman"
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         for k in range(len(li[j])):
#             if li[i][j][k]== findvalue:
#                 li[i][j][k]= newvalue
#             print(li[i][j][k], end = " ")
#         print()
#     print()
# print(li)



# program to find the list of worlds that are longer than n from a given list of world...

# list = ["python", "is", "a", "popular", "programming", "language"]
# n = 3
# new = []
# for i in list:
#     if len(i) > n:
#         new.append(i)
# print(new)

# Write a python function that takes two lists & returns True if they have at least one common member....
# a = [1,2,3,4,5,6]
# b = [2,7,8,9,0,1]

# for i in a:
#     if i[a]==
     





# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.....]
# list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# list.pop(0)
# list.pop(4)
# print(list)


# Write a Python program to print the numbers of a specified list after removing even numbers from it.
# num = [7, 8, 120, 25, 44, 20, 27]
# li = []
# for i in range(len(num)):
#     if num[i]%2==0:
#         li.append(num[i])
# num = li
    
# print(num)
        

# Write a Python program to check if each number is prime in a given list of numbers. Return 
# True if all numbers  are not prime otherwise False.....
# list = [3,5,7,11,13]
# for i in range(len(list)):
#     if i==2 or i==3 or i==5 or i==7:
#         print("true")
#     elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
#         print("true")
#     else:
#         print("false")
         



 


    













    
    
    
    

            








        










    






# n = int(5)
# print(n)
# x = 2.8
# print(x)
# x = float(2.8)
# print(x)







    

    
         




    



# num = [1,3,5,6,8]
# total = 0
# for i in range(len(num)):
#     total+= num[i]
# print(total)
