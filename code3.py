print("Part3: ")
employees = {
    "Engineering Department": {
        "Alice": {
            "Age": 30,
            "Role": "Software Engineer",
        },
        "Bob": {
            "Age": 28,
            "Role": "DevOps Engineer",
        },
    },
    "HR Deprtment": {
        "Charlie": {
            "Age": 35,
            "Role": "HR Manager",
        }
    }
}
print("The company employees are: ")
print(employees)
employees["Engineering Department"]["David"] = {
    "Age": 27,
    "Role": "Data Scientist",
}
print("The company employees after new arrival: ")
print(employees)
def countemployees(company):
    totalemployees = 0
    for number in company.values():
        totalemployees += len(number)
    return totalemployees