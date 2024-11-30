#! usr/bin/python3

"""
Static methods are used to define methods which do not have any binding
on Instance or class objects/variables but used for doing an operation  

"""


class Employee:
    # Class variables
    location = "United States"
    raise_amount = 0.05

    def __init__(
        self,
        first,
        last,
        pay,
        employee_id=None,
    ):
        # instance variables
        self.first = first
        self.last = last
        self.employee_id = employee_id
        self.location = Employee.location
        self.pay = pay

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay += self.pay * Employee.raise_amount
        return self.pay

    @classmethod
    def set_raise_amount(cls, amount):
        """
        Changes class variable value on the go

        """
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        """
        This is a class constructor

        It creates an Employee class instance object from a string
        """
        first, last, pay = string.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


if __name__ == "__main__":
    import datetime

    employee_str_1 = "Saurabh-Saran-100000"
    employee_str_2 = "Neha-Saran-150000"
    employee_str_3 = "Neerja-Saran-200000"

    ## Creating instances by calling the class method (from_string)
    employee_1 = Employee.from_string(employee_str_1)
    employee_2 = Employee.from_string(employee_str_2)
    employee_3 = Employee.from_string(employee_str_3)

    # Employee 1
    print(employee_1.fullname())
    print("Salary before raise {}".format(employee_1.pay))
    employee_1.apply_raise()
    print("Salary after raise {}".format(employee_1.pay))
    ## Changing the raise_amount class variable value to 1.05 using classmethod set_raise_amount
    print("*" * 100)
    Employee.set_raise_amount(1.05)
    print("Salary before raise amount change {}".format(employee_1.pay))
    employee_1.apply_raise()
    print("Salary after raise amount change {}".format(employee_1.pay))
    print("#" * 100)

    # Employee 2
    print(employee_2.fullname())
    print("Salary before raise {}".format(employee_2.pay))
    employee_2.apply_raise()
    print("Salary after raise {}".format(employee_2.pay))
    ## Changing the raise_amount class variable value to 1.05 using classmethod set_raise_amount
    print("*" * 100)
    Employee.set_raise_amount(1.05)
    print("Salary before raise amount change {}".format(employee_2.pay))
    employee_2.apply_raise()
    print("Salary after raise amount change {}".format(employee_2.pay))
    print("#" * 100)

    # Employee 3
    print(employee_3.fullname())
    print("Salary before raise {}".format(employee_3.pay))
    employee_3.apply_raise()
    print("Salary after raise {}".format(employee_3.pay))
    ## Changing the raise_amount class variable value to 1.05 using classmethod set_raise_amount
    print("*" * 100)
    Employee.set_raise_amount(1.05)
    print("Salary before raise amount change {}".format(employee_3.pay))
    employee_3.apply_raise()
    print("Salary after raise amount change {}".format(employee_3.pay))
    print("#" * 100)

    my_date = datetime.date(2024, 11, 29)
    print(Employee.isworkday(my_date))


"""
Saurabh Saran
Salary before raise 100000
Salary after raise 105000.0
****************************************************************************************************
Salary before raise amount change 105000.0
Salary after raise amount change 215250.0
####################################################################################################
Neha Saran
Salary before raise 150000
Salary after raise 307500.0
****************************************************************************************************
Salary before raise amount change 307500.0
Salary after raise amount change 630375.0
####################################################################################################
Neerja Saran
Salary before raise 200000
Salary after raise 410000.0
****************************************************************************************************
Salary before raise amount change 410000.0
Salary after raise amount change 840500.0
####################################################################################################
[Finished in 181ms]
"""
