import csv
a = [1231,312312,3123123]
b = [1, 2, 3]
wtr = csv.writer(open('out.csv', 'w'), delimiter=',', lineterminator='\n')



wtr.writerow(['hello'])
