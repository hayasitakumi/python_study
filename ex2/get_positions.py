def get_positions(xs, ys):
  a = []
  for i in ys:
    for j in xs:
      if i == j:
        a.append(xs.index(i))

  return a