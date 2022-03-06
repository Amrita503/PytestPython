#Write a python program To have a tuple of 5 names Try to add 6th value within tuple,Does program crash ? Have try catch and give the reasonable message saying 6
try:
     tuplevalue=("Amrita", "shyam", "gita", "rita", "kelly")
     tuplevalue.append("Hari")
     print(tuplevalue)
except:
   print("New name can not  be added")


# write try catch program for the program not to crash by saying, no cannot be divided by zero
try:
   num1 = int(input("Enter a number "))
   num2 = int(input("Enter a number"))
   result = num1/num2
   print(result)
except ZeroDivisionError:
   print("Number is  not divisible")
finally:
    print("Try and excpet is not executed")

#Write a program  try, catch and finally for divisble of the number:
try:
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter a number"))
    result = num1//num2
    print(result)
except ZeroDivisionError:
   print("Number is  not divisible")
finally:
      x= int(input("Enter a number "))
      y= int(input("Enter a number"))
      result = x/y
      print("Executed")


# write a program to input fname and lname and do it by try except else and finally
try:
    fname = input("enter first name")
    lname = input("enter last name")
    Age = int(input("Enter your age"))

except:
    print("No fname , lname or age are found")
else:
    print(fname)
    print(lname)
    print(Age)
    print("Found fname lname and age")
finally:
    print("try and excpet is not excuted ")