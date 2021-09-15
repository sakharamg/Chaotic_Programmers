import json


def processData( input_path, output_path ):
    '''  write your code here '''
    output_data=[{},{}]
    output_data[0]["age_grp"]="21-30"
    output_data[1]["age_grp"]="31-40"
    
    output_data[0]['tid_name']={}
    output_data[1]['tid_name']={}
    
    output_data[0]["mcount"]= 0
    output_data[0]["mbalance"]= 0
    output_data[0]["fcount"]= 0
    output_data[0]["fbalance"]= 0
    output_data[1]["mcount"]= 0
    output_data[1]["mbalance"]= 0
    output_data[1]["fcount"]= 0
    output_data[1]["fbalance"]= 0
    print(input_path)
    print(output_path)
    f = open(input_path,)
    data = json.load(f)
    for person in data:
    	if(person['isActive']==True):
    		if(person['age']>=21 and person['age']<=30):
    			index=0
    		elif(person['age']>=31 and person['age']<=40):
    			index=1
    		output_data[index]['tid_name'][person['tid']]=person['name']
    		if person['gender']=="male":
    			output_data[index]["mcount"]+=1
    			output_data[index]["mbalance"]+=float(person['balance'][1:len(person['balance'])])
    			
    		else:
    			output_data[index]["fcount"]+=1
    			output_data[index]["fbalance"]+=float(person['balance'][1:len(person['balance'])])
    with open(output_path, 'w') as outfile:
    	json.dump(output_data, outfile,indent=4)
    			
if __name__ == "__main__":
    '''
        Remove this comment.
        This is just for you to run and check your code.

        To test your function we will import this file and call your function.
        Before running give appropriate file path for path_to_input_json below. 
    '''
    path_to_input_json = './testcases/q6/q6_input.json'
    path_to_output_json = './testcases/q6/q6_output.json'
    processData( path_to_input_json, path_to_output_json )
    
