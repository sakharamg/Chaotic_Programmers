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
        self.connection = sqlite3.connect('employeeDB.db')
        self.cursor = self.connection.cursor()


        table_creation_query = '''CREATE TABLE IF NOT EXISTS employeeInfo (
                                Name TEXT,
                                ID INTEGER,
                                Salary INTEGER,
                                City TEXT);'''

        self.cursor.execute(table_creation_query)
        self.connection.commit()
    def populate_table(self):
        """put data from csv to database
        and commit """
        csv_file = sys.argv[1]
        data_to_insert = []
        with open(csv_file, 'r') as file:
            next(file) #To remove header
            for line in file:
                current_row = line.split(",")
                data = (current_row[0], current_row[1], current_row[2], current_row[3][:-1]) #Last column has new line, which is being removed
                data_to_insert.append(data)
        self.cursor.executemany("INSERT INTO employeeInfo(Name, ID, Salary, City) VALUES (?, ?, ?, ?)", data_to_insert)
        self.connection.commit()

    def print_all(self):
        """ write query to retrieve all  """
        select_all_query = """ SELECT * from employeeInfo;"""
        self.cursor.execute(select_all_query)
        results = self.cursor.fetchall()
        print("Name\tId\tSalary\tCity")
        for row in results:
            print(row[0], row[1], row[2], row[3], sep="\t")
    def highest_salary(self):
        """write code to retrieve
         Highest salary """
        highest_salary_query = """ SELECT Name from employeeInfo where Salary = (SELECT max(Salary) from employeeInfo);"""
        self.cursor.execute(highest_salary_query)
        results = self.cursor.fetchall()
        result_str = ""
        for row in results:
            result_str += (row[0] + " ")
        print(result_str[:-1])

    def second_highest_salary(self):
        """write code to retrieve
        second_Highest salary """
        second_salary_query = """ SELECT Name from employeeInfo where Salary = (SELECT max(Salary) from employeeInfo where Salary != (Select max(Salary) from employeeInfo)); """
        self.cursor.execute(second_salary_query)
        results = self.cursor.fetchall()
        result_str = ""
        for row in results:
            result_str += (row[0] + " ")
        print(result_str[:-1])

    def same_city(self):
        """write code to retrieve the ids of persons
        who belong to same city"""
        same_city_query = """SELECT ID from employeeInfo where City in (SELECT City from employeeInfo group by City having count(*) > 1); """
        self.cursor.execute(same_city_query)
        results = self.cursor.fetchall()
        result_str = ""
        for row in results:
            result_str += (str(row[0]) + " ")
        print(result_str[:-1])


empl = Employee()
empl.populate_table()
empl.print_all()
empl.highest_salary()
empl.second_highest_salary()
empl.same_city()
