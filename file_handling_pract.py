import json
# creating a file
print("-----Creating a file-----")

x = open("Adithi.txt", 'w')
x.write("Welcome to the new world..!!\n This is a text file to test..!")
x.close()

x = open("Adithi.txt", 'r')
print(x.read(5))
print(x.read(10))
x.close()

print("----reading the content using for loop----")
x = open("Adithi.txt", 'r')
for i in x:
    print(i)

# writing file content to file using append mode
print("-----writing file content to file using append mode-----")

x = open("Adithi.txt", 'a')
x.write("now the file has more content")
x.close()

x = open("Adithi.txt", 'r')
print(x.read())
x.close()

"""y = open("Myfiles.txt", 'x')
print(y.read())"""


employee = {"name":"Ram", "Occupation":"CEO"}
emp = json.loads(employee)

f = open("employee.json", "r")
data = json.loads(f.read())
for i in data['employee']:
    print(i)
