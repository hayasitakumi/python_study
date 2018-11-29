# def common_elements(xs, ys):
#   a = []
#   for i in xs:
#     for j in ys:
#       if i == j:
#         a.append(j)

#   return a

def ce(xs, ys):
  return list(set(xs) & set(ys))

  # '''期待される動作:
  #   >>> year = ce([1, 2, 3], [3, 1, 4])
  #   >>> year
  #   000
  # '''

if __name__ == '__main__':
  common_elements([1, 2, 3], [3, 1, 4])
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)