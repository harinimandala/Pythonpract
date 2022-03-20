import json

employee = {"Emp1":
    {
    "Emp_Name": "Ram",
    "Emp_designation": "CEO",
    "Emp_email": "Ram@gmail.com",
    "Emp_location": "India",
    "Emp_marital_status": "True"
    },
    'Emp2':
        {
    "Emp_Name": "Lakshman",
    "Emp_designation": "Finance",
    "Emp_email": "None",
    "Emp_location": "USA"
    }
}

print(employee)
print(type(employee))

j_emp = json.dumps(employee)
print(j_emp)
print(type(j_emp))

with open("j_emp", "w") as f:
    f.write(j_emp)
    print(type(j_emp))
    f.close()
# json file
print("-----Json file-----")

Family = '{"Name":"Harini","Age":33,"Occupation":"Manager","Licence": "true"}'
data = json.loads(Family)
print(type(data))
print(data)

data = json.dumps(Family)
print(type(data))
print(data)


# Model of json file
print("-----Model of json file-----")

Cities_type = '''{
   "city": {
    {
        "Name": "Hyderabad",
        "Abbrevation": "Hyd",
        "Code": 92,
        "Metropolitan": "true"
    },
    {
        "Name": "Banglore",
        "Abbrevation": "BNLR",
        "Code": 31,
        "Metropolitan": "true"
    },
    {
        "Name": "Lb Nagar",
        "Abbrevation": "LB",
        "Code": 12,
        "Metropolitan": "false"
    }
   }
}'''
print(type(Cities_type))
print(Cities_type)
print(Cities_type["city"]["Name"])




