# imports
import sys
import sqlite3

# NOTE :
# 1. DO NOT CHANGE THE NAME OF ANY FUNCTION OR ANY ARGUMENT OR CLASS NAME.
# 2. ANY DEVIATION IN THE NAMING CONVENTION, THE AUTO-GRADER WILL MARK ZERO.
# 3. Do not import anything else except what is given or imported


if len(sys.argv) != 2:
    print('usage: python Question4.py q2_employee_info.csv')
    exit(0)


class Employee():
    def __init__(self):
        """
        creates the database Employee_DB
        and create the table Employee_Info
         """
        pass

    def populate_table(self):
        """put data from csv to database
        and commit """
        pass

    def print_all(self):
        """ write query to retrieve all  """
        pass

    def highest_salary(self):
        """write code to retrieve
         Highest salary """
        pass

    def second_highest_salary(self):
        """write code to retrieve
        second_Highest salary """
        pass

    def same_city(self):
        """write code to retrieve the ids of persons
        who belong to same city"""
        pass


empl = Employee()
empl.populate_table()
empl.print_all()
empl.highest_salary()
empl.second_highest_salary()
empl.same_city()
