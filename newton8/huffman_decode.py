def huffman_decode(code, s):
  key = ''
  decode = ''
  
  for bit in s:
    key += bit
    if key in code:
      decode += code[key]
      key = ''
  return decode

if __name__ =="__main__":
  print(huffman_decode({'0': 'A', '10': 'B', '110': 'C', '111': 'D'}, '010100'))