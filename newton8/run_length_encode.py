def run_length_encode(s):
  count = 1
  encode = ''
  try:
    for i in range(len(s)):
      if s[i] == s[i+1]:
        count += 1
      else:
        encode += s[i] + str(count)
        count = 1
  except:
    encode += s[i] + str(count)
  
  return encode
  
if __name__ == "__main__":
  print(run_length_encode('ABBAC'))