def gcd(t0,t1):
  
  divisors0 = []
  for i in range(1,t0+1):
    if t0 % i == 0:
      divisors0.append(i)
      
  divisors1 = []
  for i in range(1,t1+1):
    if t1 % i == 0:
      divisors1.append(i)
  
  for divisor0 in divisors0:
    if divisor0 in divisors1:
      GCdivisor = divisor0
  return GCdivisor

def add(t0,t1):
  b = t0[3] * t1[3]
  a0 = t0[0] * (t0[2] * t1[3] + t0[1] * t0[3] * t1[3])
  a1 = t1[0] * (t1[2] * t0[3] + t1[1] * t1[3] * t0[3])
  a = a0 + a1
  
  if a < 0:
    s = -1
  else:
    s = 1
    
  a = abs(a)
  n = a / b
  a = a % b

  if a == 0:
    b = 1
    return (s,int(n),a,b)
  
  divisor = gcd(a,b)
  
  a = a / divisor
  b = b / divisor

  return (s,int(n),a,b)


def sub(t0,t1):
  b = t0[3] * t1[3]
  a0 = t0[0] * (t0[2] * t1[3] + t0[1] * t0[3] * t1[3])
  a1 = t1[0] * (t1[2] * t0[3] + t1[1] * t1[3] * t0[3])
  a = a0 - a1
  
  if a < 0:
    s = -1
  else:
    s = 1
    
  a = abs(a)
  n = a / b
  a = a % b

  if a == 0:
    b = 1
    return (s,int(n),a,b)
  
  divisor = gcd(a,b)
  
  a = a / divisor
  b = b / divisor

  return (s,int(n),a,b)


def mul(t0,t1):
  b = t0[3] * t1[3]
  a0 = t0[2]+t0[3]*t0[1]
  a1 = t1[2]+t1[3]*t1[1]
  a = a0 * a1

  if t0[0] * t1[0] < 0:
    s = -1
  else:
    s = 1
    
  n = a / b
  a = a % b

  if a == 0:
    b = 1
    return (s,int(n),a,b)
  
  divisor = gcd(a,b)
  
  a = a / divisor
  b = b / divisor
  return (s,int(n),a,b)

def div(t0,t1):
  
  a0 = t0[2]+t0[3]*t0[1]
  a1 = t1[2]+t1[3]*t1[1]
  b = t0[3] * a1
  a = a0 * t1[3]

  if t0[0] * t1[0] < 0:
    s = -1
  else:
    s = 1
  n = a / b
  a = a % b

  if a == 0:
    b = 1
    return (s,int(n),a,b)
  
  divisor = gcd(a,b)
  
  a = a / divisor
  b = b / divisor
  return (s,int(n),a,b)
