#! usr/bin/python3


class Employee:
    # Class variables
    location = "United States"
    raise_amount = 0.05

    def __init__(self, first, last, employee_id, pay, location):
        # instance variables
        self.first = first
        self.last = last
        self.employee_id = employee_id
        self.location = Employee.location
        self.pay = pay
        self.location = location

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay += self.pay * self.raise_amount
        return self.pay


employee_1 = Employee(
    first="Saurabh",
    last="Saran",
    employee_id=138184,
    pay=100000,
    location="United States",
)
print(employee_1.fullname())
print("Salary before raise {}".format(employee_1.pay))
employee_1.apply_raise()
print("Salary after raise {}".format(employee_1.pay))
