import csv

f = open('Data/seoul.csv', 'r', encoding = 'cp949')
data = csv.reader(f, delimiter = ',')
print(data)
f.close()



f = open('Data/seoul.csv', encoding = 'cp949')
data = csv.reader(f)
for row in data:
    print(row)
f.close()