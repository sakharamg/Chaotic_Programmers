# Import packages
import sqlite3
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from prettytable import PrettyTable

## NOTE : 
## 1. DO NOT CHANGE THE NAME OF ANY FUNCTION OR ANY ARGUMENT OR CLASS NAME. 
## 2. DO NOT CHANGE ANYTHING IN MAIN FUCNTION.
## 3. WRITE YOUR CODE INSIDE ### START CODE HERE ### and ### END CODE HERE ### ONLY
## 4. ANY DEVIATION IN THE NAMING CONVENTION, THE AUTOGRADER WILL MARK ZERO.

class CSE_Courses:
	def __init__(self):
		"""
		Create the database CSE_DB and tables CSE_Courses, and CSE_Instructors.
		"""
		### START CODE HERE ###
		conn = sqlite3.connect('CSE_DB')
		c = conn.cursor()
		c.execute('''CREATE TABLE CSE_Instructors([Instructor] TEXT,[Research_Interests] TEXT,[Email] TEXT)''')
		c.execute('''CREATE TABLE CSE_Courses([Course_Code] TEXT,[Course_Name] TEXT,[Instructor] TEXT)''')
		conn.commit()
		### END CODE HERE ###

	def get_courses(self,url):
		"""
		This method should scrap all the courses from the url and 
		returns list of lists where each inner list has [Course_Code, Course_Name, Instructor]
		of a course. 

		Arguments:
		url : url from which courses have to be scraped, string

		Returns:
		courses : courses scraped from the url : list of lists

		"""
		assert(isinstance(url,str))
		### START CODE HERE ###
		courses=[]
		URL=url
		r = requests.get(URL)
		soup = BeautifulSoup(r.content, 'html5lib')
		table = soup.findAll('td', attrs = {'class':'greybodytd'})
		col=0
		for cell in table:
			if(col%3==0):
				#cell left
				course_code=cell.a.text.strip()
			elif col%3==1:
				#cell mid
				course_name=cell.text.strip().replace("More Info","").strip()
			else:
				#cell right
				course_instr=cell.text.strip().replace("Prof.","").strip()
				if course_instr=="---":
					course_instr="NA"
				courses.append([course_code,course_name,course_instr])
			col+=1
		### END CODE HERE ###
		assert(isinstance(courses,list) and isinstance(courses[0],list))
		return courses

	def get_instructors(self,url):
		"""
		This method should scrap all the details of instructors from the url and 
		returns list of lists where each inner list has [Instructor, Research_Interests, Email]
		of an instructor.

		Arguments:
		url : url from which details of the instructors have to be scraped, string

		Returns:
		courses : details scraped from the url : list of lists

		"""
		assert(isinstance(url,str))
		### START CODE HERE ###
		details=[]
		session = HTMLSession()
		r = session.get(url)
		r.html.render(timeout=10000000)
		soup = BeautifulSoup(r.html.html, 'html5lib')
		current=soup.find('div', attrs = {'id':'current'})
		for row in current:
			instructor=row.a.text.strip().replace("(Department Head)","").strip()
			interests=row.find('div', attrs = {'class':'body'}).text.strip()
			email_split=row.findAll('div', attrs = {'class':'body'})[1].text.split(',')[0].split('  ')
			email=(email_split[0]+"@"+email_split[1]+"."+email_split[2]+"."+email_split[3]+"."+email_split[4]).strip()
			details.append([instructor,interests,email])
		### END CODE HERE ###
		assert(isinstance(details,list) and isinstance(details[0],list))
		return details

	def insert_CSE_Courses(self,courses):
		"""  
		This method will insert all the courses in the table CSE_Courses
		If you rerun your program, it will insert all the courses again 
		in the table, so if you want to delete the previously added course, 
		you may call delete_data() method from the main function.

		Arguments:
		courses : courses scrapped from the url : list of lists

		Returns:
		Nothing
		"""
		assert(isinstance(courses,list) and isinstance(courses[0],list))
		### START CODE HERE ###
		conn = sqlite3.connect('CSE_DB')
		c = conn.cursor()
		for course in courses:
			c.execute("INSERT INTO CSE_Courses VALUES('"+course[0]+"','"+course[1]+"','"+course[2]+"')")
		conn.commit()
		### END CODE HERE ###

	def insert_CSE_Instructors(self,details):
		"""  
		This method will insert all the details of the instructors in the table CSE_Instructors
		If you rerun your program, it will insert all the details again 
		in the table, so if you want to delete the previously added details, 
		you may call delete_data() method from the main function.

		Note: 1. Remove "(Department Head)" suffix from the Prof. Umesh Bellur name.
			  2. Remove 'Prof. ' prefix from the Instructor column 
			  	 because later this column will act as a key while mapping the tables.

		Arguments:
		details : details scrapped from the url : list of lists

		Returns:
		Nothing
		"""
		assert(isinstance(details,list) and isinstance(details[0],list))
		### START CODE HERE ###
		conn = sqlite3.connect('CSE_DB')
		c = conn.cursor()
		for detail in details:
			c.execute("INSERT INTO CSE_Instructors VALUES('"+detail[0]+"','"+detail[1]+"','"+detail[2]+"')")
		conn.commit()
		### END CODE HERE ###

	def map_data(self):
		"""
		This method will create a new table CSE_Mapped where 'Instructor' column will act as a key.
		In mapped table, keep only these three columns [Course_Code, Instructor, Email] after mapping.

		Arguments:
		Nothing

		Returns:
		Nothing
		"""
		### START CODE HERE ###
		conn = sqlite3.connect('CSE_DB')
		c = conn.cursor()
		c.execute("CREATE TABLE CSE_Mapped AS SELECT Course_Code, CSE_Courses.Instructor, Email FROM CSE_Courses inner join CSE_Instructors on CSE_Courses.Instructor=CSE_Instructors.Instructor")
		conn.commit()
		### END CODE HERE ###

	def print_data(self):
		"""
		This method will print all the courses present in the table CSE_Mapped
		in a tabular format [you may use tabulate or PrettyTable, 
		feel free to use any of your choice, but the output should be in tabular format]

		Arguments:
		Nothing

		Returns:
		Nothing
		"""
		### START CODE HERE ###
		conn = sqlite3.connect('CSE_DB')
		c = conn.cursor()
		c.execute("SELECT * FROM CSE_Mapped")
		cse_mapped_data=c.fetchall()
		myTable = PrettyTable(["Course Code","Instructor","Email"])
		for x in cse_mapped_data:
			myTable.add_row(list(x))
		print(myTable)
		conn.commit()
		### END CODE HERE ###

	def delete_data(self):
		"""
		This method will delete all the records of all three tables.

		Arguments:
		Nothing
		
		Returns:
		Nothing
		"""

		### START CODE HERE ###
		conn = sqlite3.connect('CSE_DB')
		c = conn.cursor()
		c.execute("DELETE FROM CSE_Courses")
		c.execute("DELETE FROM CSE_Instructors")
		c.execute("DELETE FROM CSE_Mapped")
		conn.commit()
		### END CODE HERE ###

if __name__ == "__main__":
	url1 = "https://www.cse.iitb.ac.in/archive/page136"
	url2 = "https://www.cse.iitb.ac.in/people/faculty.php"

	cse = CSE_Courses()
	courses = cse.get_courses(url1)
	details = cse.get_instructors(url2)
	cse.insert_CSE_Courses(courses)
	cse.insert_CSE_Instructors(details)
	#cse.delete_data()
	cse.map_data()
	cse.print_data()
