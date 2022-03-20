import json

# conversion of json into python file this can be done by json.loads()
print("-----conversion of json into python file this can be done by json.loads()-----")

x = '{"Name":"Harini", "age": 33, "Occupation":"Manager"}'
y = json.loads(x)

print(y["Occupation"])
print(type(x))
print(type(y))

# conversion of python into json file this can be done by json.dumps()
print("-----conversion of python into json file this can be done by json.dumps()-----")

per_dic = {
    "Name": "Adithi",
    "Age": 3,
    "Occupation": "kid"
}

j_per = json.dumps(per_dic)
print(j_per)
print(type(per_dic))
print(type(j_per))



data = {"key1" : "value1", "key2" : "value2"}
data1 = json.dumps(data)
print(data1)

#   Access the value of key2 from the following JSON
print("-----Access the value of key2 from the following JSON-----")

sampleJson = """{"key1": "value1", "key2": "value2"}"""
sample1 = json.loads(sampleJson)
print(sample1["key2"])

# PrettyPrint following JSON data
print("-----PrettyPrint following JSON data-----")

sampleJson = {"key1": "value1", "key2": "value2"}
print(sampleJson)
PrettyPrintJson = json.dumps(sampleJson, indent=2)
print(PrettyPrintJson)

# Sort JSON keys in and write them into a file
print("-----Sorting JSON keys in and write them into a file-----")

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

print("Started writing JSON data into a file")
with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")



sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sampleJson1 = json.loads(sampleJson)
print(sampleJson1["company"]["employee"]["payble"]["salary"])


