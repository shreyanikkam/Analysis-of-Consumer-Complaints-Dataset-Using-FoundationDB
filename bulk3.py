import csv
import sys
csv.field_size_limit(sys.maxsize)
try:
    risk = open('Consumer_Complaints.csv', 'r').read() #find the file

except:
    while risk != "Consumer_Complaints.csv":  # if the file cant be found if there is an error
     print("Could not open", risk, "file")
     risk = input("\nPlease try to open file again: ")
else:
    with open("Consumer_Complaints.csv") as f:
        reader = csv.reader(f, delimiter=' ', quotechar='|')

        data = []
        for row in reader:
             #print(', '.join(row)
            #print row[3]
            for col in (1,18):
                data.append(row)
                data.append(col)
        for item in data:
            print(item) #print the rows and columns
