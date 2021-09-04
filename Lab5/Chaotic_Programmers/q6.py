def read(input_file):
    """
    input
    ------------
    input_file: path of input file
    
    return
    ------------
    dictionary (format given in document)
    """
    
    # read the input_file
    # fill the body of "read" function
    #
    output={} # save the output of the program in a dictionary named output
    count=0 #count will be used to set label of each entry as asked in assignment
    data = open(input_file, "r") # read the input file
    for row in data: # for each row in the file
    	count+=1
    	if row[-1]=='\n': #remove any newline entries at the end
    		#[:-1] means index from 0th until last excluding last, -1 signifies last
    		# if row[a:b] then ath to b-1th elements are selected so here [:-1] from start to second last elements are selected 
    		row=row[:-1] 
    	if len(row)==9: #If the row has only roll no.(roll no are of length 9) then call the decode function 
    		output[count]=decode(row) # store the result returend by decode function into output
    	else: # If its not roll number then encode it
    		output[count]=encode(row)
    return output

def decode(input_line):
    """
    input
    ------------
    input_line: [type: string] individual line read from input file

    return
    ------------
    tab separated decoded string
    """

    # fill the body of "decode" function
    #
    # The decode function converts/decodes roll number into a descriptive info from roll number
    # rollno	student_ID	Year	Course	Deparment
    # e.g. 213051234 is decoded into
    # 213051234	1234	2021	MTech	CSE
    
    # Output contains the final decoded string
    #Append roll no and year to output
    output=input_line+"\t"+"20"+input_line[0:2]+"\t"
    
    #Check 3rd digit to obtain course id and append to output
    if int(input_line[2])==0:
    	output+="BTech\t"
    elif int(input_line[2])==1:
    	output+="MSc\t"
    elif int(input_line[2])==3:
    	output+="MTech\t"
    elif int(input_line[2])==4:
    	output+="PhD\t"
    else:
    	output+="MBA\t"
    
    # Check the 4th and 5th digit (i.e. 2rd and 4th index of numpy array) and append Department name accordingly
    if int(input_line[3:5])==1:
    	output+="Aerospace"
    elif int(input_line[3:5])==2:
    	output+="Chemical"
    elif int(input_line[3:5])==3:
    	output+="Chemistry"
    elif int(input_line[3:5])==4:
    	output+="Civil"
    elif int(input_line[3:5])==5:
    	output+="CSE"
    elif int(input_line[3:5])==9:
    	output+="Mathematics"
    elif int(input_line[3:5])==10:
    	output+="Mechanical"
    elif int(input_line[3:5])==12:
    	output+="Physics"
    else:
    	output+="CSRE"
    
    return output

def encode(input_line):
    """
    input
    ------------
    input_line: [type: string] individual line read from input file

    return
    ------------
    encoded string
    """

    # fill the body of "encode" function
    #
    # From 		student id, year, course and dept name return the rollno
    # Index in numpy: 	      0       1      2          3
    #Split the tab seperated description
    values = input_line.split("\t")
    
    # The last two digits of year fetches the first two digits of rollno
    output=values[1][2:4]
    
    # The Course name gives the 3rd digit of rollno
    if values[2]=='BTech':
    	output+='0'
    elif values[2]=='MSc':
    	output+='1'
    elif values[2]=='MTech':
    	output+='3'
    elif values[2]=='PhD':
    	output+='4'
    else:
    	output+='9'
    	
    # The department name is the 4th and 5th digit of rollno
    if values[3]=='Aerospace':
    	output+='01'
    elif values[3]=='Chemical':
    	output+='02'
    elif values[3]=='Chemistry':
    	output+='03'
    elif values[3]=='Civil':
    	output+='04'
    elif values[3]=='CSE':
    	output+='05'
    elif values[3]=='Mathematics':
    	output+='09'
    elif values[3]=='Mechanical':
    	output+='10'
    elif values[3]=='Physics':
    	output+='12'
    else:
    	output+='31'
    
    # The student id is finally appended to obtain the exact rollno
    output+=values[0]
    
    return output

# use this to test your function
# do not modify it
# do not submit the file after uncommenting the code below 
if __name__=="__main__":
    out_dict = read(input())
    for key, value in out_dict.items():
        print(value)
