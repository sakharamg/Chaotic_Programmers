from stackapi import StackAPI
import pandas as pd
import sys

#inp is a list of tags(input)
def function_q4(inp):
    #Write your code here
    SITE = StackAPI('stackoverflow')
    SITE.page_size = 50
    SITE.max_pages = 1
    tags = ";".join(inp)
    file_name = "_".join(inp)
    tags = str.lower(tags)
    file_name = str.lower(file_name) + ".csv"
    questions = SITE.fetch('search/advanced', min = 200, tagged=tags, sort='votes', order = 'desc', accepted = 'True')
    results = questions['items']


    with open(file_name, 'w') as file:
        file.write('question_id,tags,total_answers,link,accepted_answer\n')
        for question in results:
            question_id = str(question['question_id'])
            tags ="'"+"','".join(question['tags'])+"'"
            total_ans = str(question['answer_count'])
            q_link = question['link']
            accepted_ans = q_link + "/#" + str(question['accepted_answer_id'])
            output_line = question_id + "," +  "\"[" + tags + "]\"," + total_ans + "," + q_link + "," + accepted_ans + "\n"
            file.write(output_line)


if __name__=="__main__":
    n=len(sys.argv)  
    inp = []
    for i in range(1,n):
        inp.append(sys.argv[i])
    function_q4(inp)
