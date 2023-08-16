class Employee:
    # def __init__(self):
    #     print("A new employee is being created")
    #     self.first_name = "Amsu"
    #     self.last_name = "Warner"
    
    # def __init__(self, fName, lName):
    #     print("A new employee is being created")
    #     self.first_name = fName
    #     self.last_name_name = lName
    
    # OPTIONAL VALUES
    def __init__(self, fName="", lName=""):
        print("New employee is being created")
        self.first_name = fName
        self.last_name = lName
    
    def __str__(self):
        return "This is an employee"
    
    def __repr__(self):
        return f"firstName = {self.first_name}, lastName = {self.last_name}"

emp = Employee()