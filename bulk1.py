import csv
import sys
csv.field_size_limit(sys.maxsize)
with open('Consumer_Complaints.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
         print(', '.join(row))

        #print(', '.join(col))
