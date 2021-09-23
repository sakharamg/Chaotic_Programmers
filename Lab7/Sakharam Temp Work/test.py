import requests
from bs4 import BeautifulSoup

URL="https://www.cse.iitb.ac.in/archive/page136"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
table = soup.findAll('td', attrs = {'class':'greybodytd'})
col=0
courses=[]
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
	
