#Addition and Deletion in set
'''setexam = {"Jan", "Feb", "Mar", "Apr", "May"}
setexam.update(["June", "July", "Aug", "Sep"])
print("Set after adding multiple elements", setexam)
setexam.pop()
print("Set after using pop function", setexam)'''


#Dictionary
'''
EmployeeDetail = {
    "Name": "Sandhya",
    "Profile": "QA",
    "EmplyeeID": "123",
    "CompanyName": "S&PGlobal"
    }

print("Fetching key value using get method", EmployeeDetail.get("Name"))
print("Fetching key value simply via", EmployeeDetail["Profile"])

#Different functions to get the key and values using loops

for x in EmployeeDetail:
    print("Print all keys in the EmployeeDetails Dic", x)

for x in EmployeeDetail:
    print("Print all values in the EmployeeDetails Dic", EmployeeDetail[x])


for x in EmployeeDetail.values():
    print("Print all values using values function of the dictionary", x)

#Print all keys and Values all together used in a dictionary using items function
for x,y in EmployeeDetail.items():
     print(x, y)'''

#ShortHandIf

a = 10
b = 100
#print("A") if a > b else print("B")

i = 1
while i < 6:
    print("Print values of until it met the condition", i)
    if i == 3:
        break
        print("Statement Break")
    i += 1


#use of Continue Condition within Loop



i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print("Use of continue statment", i)


#Use of break and continue statement in a for loop condition

#EmpName = {"Sandhya", "Neha", "Akanksha"}
#for x in E








