def readWorkSheet(file_name):
    import csv
    from datetime import datetime as dt
    file = open(file_name)
    #reads the file
    read = csv.reader(file)
    #next skips the
    next(read)
    dict = {}
    for row in read:
        #splitting input when ït see "-" and store in respective var (year month or date)
        year, month, date = (int(i) for i in row[0].split('-'))
        #dt will do formatting we need in output file
        day = dt(year,month,date).weekday()
        if(day%2 == 0 and day != 6):
            dict[row[0]] = 'A'
        elif(day%2 == 1):
            dict[row[0]] = 'B'
        else:
            dict[row[0]] = '-'
    file.close()
    return dict

def calculateOfficeHrs(mapping_dict):
    import csv
    from datetime import datetime as dt
    A = 0
    B = 0
    for e in mapping_dict:
        #calculating officehours for day its give 8 and for night 6 so addign accordingly
        if mapping_dict[e] == 'A':
            A += 8
        elif mapping_dict[e] == 'B':
            B += 6
    return (A,B)

def writeOfficeWorkSheet(mapping_dict, out_file_name):
    import csv
    from datetime import datetime as dt
    file = open(out_file_name,"w")
    write = csv.writer(file)
    A = 0
    B = 0
    write.writerow(("date","office_name","working_hrs"))
    for key in mapping_dict:
        if mapping_dict[key] == 'A':
            A += 8
            write.writerow((key,mapping_dict[key],A))
        elif mapping_dict[key] == 'B':
            B += 6
            write.writerow((key,mapping_dict[key],B)) 
        else:
            write.writerow((key,mapping_dict[key]))
    file.close()