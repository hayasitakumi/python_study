import csv
import re

def natural_join(infile1, infile2, outfile):
  with open(infile1, encoding='utf-8') as f:
    d1 = {}
    header = []
    reader = csv.reader(f)
    for i, row in enumerate(reader):
      if i == 0:
        field1 = row
      else:
        d1[int(row[0])] = row[0:]

  with open(infile2, encoding='utf-8') as f:
    d2 = {}
    reader = csv.reader(f)
    for i, row in enumerate(reader):
      if i == 0:
        field2 = row
      else:
        d2[int(row[0])] = row[1:]

  for x in field1 + field2:
    if x not in header:
      header.append(x)

  with open(outfile, 'w', encoding='utf-8',newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)
    for key1 in d1:
      for key2 in d2:
        if key1 == key2:
          writer.writerow(d1[key1] + d2[key2])
 
if __name__ == '__main__':
  natural_join('student.csv', 'grade.csv', 'output.csv')