name = (input("Enter your name"))
age = int(input("Enter your age"))
if name == 'a' or 'f' and age <= 20:
    print("Brilliant")
elif name =='y' or 'z' and age >= 20:
    print("Excellent")
else:
    print("Noresult")



#Write a basic python program to ask for 10 roll no, class, name and age

rnum =int(input("Enter the roll number of 10 students/n"))
list=[]
for i in range(10):
   data =int(input())
   list.append(data)
print(list)


tupleform=[]
for i in range(1):
    x = int(input("Enter the class name"))
    tupleform.append(x)
    mytuple = tuple(tupleform)  #converting list into tuple
print(mytuple)



Name = (input("Enter the name of the students"))
dict={}
string= input()
dict[Name] = string
print(dict)

Age = int(input("Enter the age of the students"))
dict={}
integer=int(input())
dict[Age]=integer
print(dict)

