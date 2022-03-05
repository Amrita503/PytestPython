#5fruits name in list
fruitslist=["Apple", "Banana", "Grapes", "Kiwi", "Orange"]
print(fruitslist)
print(fruitslist[:6])

#5 country name in tuple

Countrytuple = ("Nepal", "India", "USA", "China", "Iraq")
print(Countrytuple)


#5country name in dictionary
DictionaryName = {'Firstname1':'Hari', 'Lastname1': 'Paudel',
                   'Firstname2': 'Shayam', 'Lastname2': 'Kc',
                    'Firstname3': 'Gita',  'Lastname3': 'CK',
                     'Firstname4': 'Rita',  'Lastname4': 'Yadav',
                      'Firstname5': 'Sita',   'Lastname5': 'KM'}
print(DictionaryName)
print(DictionaryName['Firstname1'])
print(DictionaryName['Lastname5'])

fruitslist.append("Gauva")
print(fruitslist)
#In tuple we cant add, remove beacuse they are immutable

DictionaryName["Address"] = "LakeCoveway"
DictionaryName["Age"] = 50
print(DictionaryName)


#Check the length of  list, tuple and dictionary
print((len(fruitslist)))
print((len(Countrytuple)))
print((len(DictionaryName)))

#For loop

for i in fruitslist:
 print(i)
for i in Countrytuple:
 print(i)
 for i in DictionaryName:
     print(i)

for i in "Apple":
    print(i)

#while loop
c = 0
while (c < 5):
    c = c+1;
    print(fruitslist)
    print(Countrytuple)
    print(DictionaryName)

 #Do while loop
 # Python dosent have do while loop  it is not excuted in python.
