# Filtering operations using If statement

employees = {
    "E101": {"name": "Alice", "dept": "AI", "salary": 60000},
    "E102": {"name": "Bob", "dept": "Backend", "salary": 55000},
    "E103": {"name": "Charlie", "dept": "AI", "salary": 70000},
    "E104": {"name": "David", "dept": "Frontend", "salary": 50000},
    "E105": {"name": "Eva", "dept": "AI", "salary": 65000}
}


# to print all employees who belong to AI department

for i in employees:
    if employees[i]["dept"] == "AI":
        print(employees[i])

# to print all employees who's salary is greater than 60,000

for i in employees:
    if employees[i]["salary"] > 60000:
        print(employees[i])

# to print employees whose salary is less than or equal to 60000

for i in employees:
    if employees[i]["salary"] <= 60000:
        print(employees[i])

# to print employees who are not in AI department

for i in employees:
    if employees[i]["dept"] != "AI":
        print(employees[i])

# to print employees who's salary is between 55000 and 65000

for i in employees:
    if employees[i]["salary"] >= 55000 and employees[i]["salary"] <= 65000:
        print(employees[i])

# to print employees whos have letter a in their names

for i in employees:
    if "a" in employees[i]["name"]:
        print(employees[i])

# to print employees who have more than 3 character in their name

for i in employees:
    if len(employees[i]["name"]) > 3:
        print(employees[i]) 

# to find employee name with highest salary

high = employees["E101"]["salary"]
employee_id = "E101"

for i in employees:
    if employees[i]["salary"] > high:
        high = employees[i]["salary"]
        employee_id = i

print(employees[employee_id]["name"])

# to calculate average salary of AI employees

sum = 0
average = 0
count = 0

for i in employees:
    if employees[i]["dept"] == "AI":
        sum = sum + employees[i]["salary"]
        count = count + 1
        
average = sum / count
print(sum)
print(average)

# count of total employees

count = 0

for i in employees:
    count = count + 1
    
print(count)

# to create new dictionary containing only employees with salary greater than 60000

newDictionary = {}

for i in employees:
    if employees[i]["salary"] > 60000:
        newDictionary[i] = employees[i]
print(newDictionary)


