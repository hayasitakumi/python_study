def edit_distance(s, t):
  s = '#' + s
  t = '#' + t
  old = [i for i in range(0, len(s))]
  for t_no in range(1, len(t)):
    new = [t_no]
    for s_no in range(1, len(s)):        
      sell1 = old[s_no - 1] #upper left
      sell2 = old[s_no] #up
      sell3 = new[s_no - 1] #left  
      if s[s_no] == t[t_no]:
        new.append(min([sell1, sell2 + 1, sell3 + 1]))
      else:
        new.append(min([sell1 + 1, sell2 + 1, sell3 + 1]))
    old = new
  return new[-1]

if __name__ == "__main__":
  list = [i for i in range(1, 9)]
  list.append(1)
  print(list)
  for i in range(1,9):
    if list.count(i) >= 2:
      print(i)
  # print(edit_distance('south', 'north'))