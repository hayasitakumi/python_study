import csv
def read_csv(filename):
  a = []
  b = []

  with open(filename,encoding = 'utf-8') as f:
    reader = csv.reader(f,delimiter = ',')
    for i,row in enumerate(reader):
      if i == 0:
        a.extend(row)
      else:
        b.append(row)

  list = (a,b)
  return list