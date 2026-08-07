# Dictionary of Dictionaries

employees = {
    "E101": {"name": "Alice", "dept": "AI", "salary": 60000},
    "E102": {"name": "Bob", "dept": "Backend", "salary": 55000},
    "E103": {"name": "Charlie", "dept": "AI", "salary": 70000},
    "E104": {"name": "David", "dept": "Frontend", "salary": 50000},
    "E105": {"name": "Eva", "dept": "AI", "salary": 65000}
}

# to access values
print(employees["E101"]["name"]) # prints Alice
print(employees["E101"]["dept"]) # prints AI
print(employees["E101"]["salary"]) # prints bob


#Looping
# Level-1 printing

# to print only employee ids
for i in employees:
    print(i)  # only print keys ie id in this example

# to print employee names
for i in employees:
    print(employees[i]["name"]) 

# to print all department names
for i in employees:
    print(employees[i]["dept"])

# to print all salaries
for i in employees:
    print(employees[i]["salary"])

# to print everything
for i in employees:
    print(employees[i])
