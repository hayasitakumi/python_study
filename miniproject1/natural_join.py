import csv

def natural_join(infile1, infile2, outfile):
  d1 = []
  d2 = []
    
  header = [] 
  header_no_stu = []
  header_no_gra = []

  student_list = []
  grade_list = []

  stu_d = {}
  gra_d = {}

  with open(infile1, encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, stu_row in enumerate(reader):
      if i == 0:
        field1 = stu_row
      else:
        d1.append(stu_row)

  with open(infile2, encoding='utf-8',) as f:
    reader = csv.reader(f)
    for i, gra_row in enumerate(reader):
      if i == 0:
        field2 = gra_row
      else:
        d2.append(gra_row)
  
  for i,f1 in enumerate(field1):
    for j,f2 in enumerate(field2):
      if f1 == f2:
        if f1 not in header:
          header_no_stu.append(i)
          header_no_gra.append(j)

  for d1_line in d1:
    key_list = []
    value_list = []
    for j,d1_str in enumerate(d1_line):
      if j in header_no_stu:
        key_list.append(d1_str)
      else:
        value_list.append(d1_str)
    student_list.append(d1_line)
    key_tuple = tuple(key_list)
    stu_d[key_tuple] = value_list

  for d2_line in d2:
    key_list = []
    value_list = []
    for j,d2_str in enumerate(d2_line):
      if j in header_no_gra:
        key_list.append(d2_str)
      else:
        value_list.append(d2_str)
    grade_list.append(d2_line)
    key_tuple = tuple(key_list)
    gra_d[key_tuple] = value_list
    

  for x in field1 + field2:
    if x not in header:
      header.append(x)

  output = []
  for i,stu_key in enumerate(stu_d):
    for gra_key in gra_d:
      if stu_key == gra_key:
         output.append(student_list[i]  + gra_d[gra_key])
         
  outcount = 0
  for i,out in enumerate(output):
    outcount = i

  with open(outfile, 'w', encoding='utf-8',newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)

    for i,out in enumerate(output):
      if i != outcount:
        writer.writerow(out)
      else:
        writer.writerow(out)