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


class Developer(Employee):
    """Developer is a sub-class of Employee class"""

    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.language = prog_language

    @classmethod
    def from_string(cls, string):
        """
        This is a class constructor

        It creates an Employee class instance object from a string
        """
        first, last, pay, lang = string.split("-")
        return cls(first, last, int(pay), lang)


class Manager(Employee):
    """Manager is a sub-class of Employee class"""

    def __init__(self, first, last, pay, level=None):
        super().__init__(first, last, pay)
        self.level = level

    @classmethod
    def from_string(cls, string):
        """
        This is a class constructor

        It creates an Employee class instance object from a string
        """
        first, last, pay, level = string.split("-")
        return cls(first, last, pay, level)


if __name__ == "__main__":
    import datetime

    employee_str_1 = "Saurabh-Saran-100000"
    employee_str_2 = "Neha-Saran-150000"
    employee_str_3 = "Neerja-Saran-200000"

    ## Creating instances by calling the class method (from_string)
    employee_1 = Employee.from_string(employee_str_1)
    employee_2 = Employee.from_string(employee_str_2)
    employee_3 = Employee.from_string(employee_str_3)

    my_date = datetime.date(2024, 11, 30)
    print(Employee.isworkday(my_date))

    employee_str_4 = "John-Lee-100000-Python"
    employee_str_5 = "Quoc-Hoang-200000-Java"

    employee_4 = Developer.from_string(employee_str_4)
    employee_5 = Developer.from_string(employee_str_5)

    # Employee 4
    print(employee_4.fullname())
    print(employee_4.location)
    print(employee_4.language)

    # Employee 5
    print("-" * 100)
    print(employee_5.fullname())
    print(employee_5.location)
    print(employee_5.language)
    print("#" * 100)


    employee_str_6 = "Tom-Booth-100000-M2"
    employee_str_7 = "Jeff-Mcauley-200000-M3"

    employee_6 = Manager.from_string(employee_str_6)
    employee_7 = Manager.from_string(employee_str_7)

    # Employee 4
    print(employee_6.fullname())
    print(employee_6.location)
    # print(employee_6.language)   ## this will not work since subclass Manager is not inheriting from Developer subclass
    print(employee_6.level)
    # isworkday() method is also available to Manager subclass
    print(Manager.isworkday(day=datetime.date(2024, 12, 1)))
    
