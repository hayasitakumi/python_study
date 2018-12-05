def add(t0,t1):

  deno = t0[3] * t1[3]
  mole = []
  mole.append(t0[0] * (t0[2] * t1[3] + t0[1] * t0[3] * t1[3]))
  mole.append(t1[0] * (t1[2] * t0[3] + t1[1] * t1[3] * t0[3]))
  print(mole[0])
  print(mole[1])

if __name__ == '__main__':   
  add((1, 1, 1, 2), (1, 2, 2, 3))
