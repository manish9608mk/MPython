# Example: Instance Methods
#
# - Each object stores its own employee information.
# - putdata() takes input and stores it inside the current object.
# - display() prints the data stored in the current object.
# - self always refers to the object that calls the method.

class employee:

  # Method 1: Store employee details
  def putdata(self):
    self.id = int(input('Enter employee id: '))
    self.name = input('Enter employee name: ')
    self.salary = int(input('Enter employee salary: '))

  # Method 2: Display employee details
  def display(self):
    print('Employee Id: ', self.id) 
    print('Employee name: ', self.name) 
    print('Employee salary: ', self.salary)

# Create the first Employee object.
first_employee = employee()
# Store data inside first_employee.
first_employee.putdata()
# Display the data of first_employee.
first_employee.display()
  
print()
second_employee = employee()
second_employee.putdata()
second_employee.display()

# You can create as many Employee objects as needed.
# Each object stores its own data independently. 