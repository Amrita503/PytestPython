# call the Function program

def add():
    print("Hi world")
add()

def function(x,y,z):
    multiplication= x*y*z
    print(multiplication)
function(3,4,5)


def name(fname,lname,age):
    print("My name is"+ fname+lname)
    print("My age is" + str(age))
name("Amrita","Paudel",27)


def function_name(fname):
    print("My name is" + fname + "Curently, I am Living in usa.")
function_name("Hari")
function_name("shyam")
function_name("Gita")


#return function program

def multi(x):
     multiplication= x*(x-1)
     return multiplication
values = multi(5)
#print(values)


def division(x,y):
    divisionnum= x/y
    return divisionnum
#division(10,5)

print(division(10,5))

#Recursive function:

def factorial(y):
    print(y)
    if y==0:
        return
    else:
       factorial(y-1)
factorial(5)

def function_multiplication(x):
    return 6*(x)
function_multiplication(5)
print(function_multiplication(5))

def factorialvalue(x):
      if (x>1):
          x = x * factorialvalue(x-1)
      return x

print(factorialvalue(3))


def getfact(x):
    if (x>1):
        x = x * getfact(x-1)
    return x

print(getfact(5))



def login(username, password):
    print("login with %s and %s" %(username,password))

login("Amrita.sharma@gmail.com", "Manakamana12")
