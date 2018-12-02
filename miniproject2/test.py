def test():
  '''期待される動作:
  >>> from project import search_labs
  >>> search_labs('画像認識')
  []
  >>> search_labs('ビッグデータ')
  [('情報工学科', '中野淳研究室')]
  >>> search_labs('データマイニング')
  [('情報工学科', '元木光雄研究室'), ('情報工学科', '林亮子研究室'), ('応用バイオ学科', '相良純一研究室')]
  '''


if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)