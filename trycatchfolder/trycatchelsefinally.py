try:
    x = int(input("Enter a number "))
    y = int(input("Enter a number"))
    result = x/y

except ZeroDivisionError:
   print("Number is  not divisible")
else:
    print(result)
    print("number is divisible")
finally:
   print("Executed")
