def build_dict(records, positions):
  dict = {}
  for record in records:
    list = []
    for position in positions:
      list.append(record[position])

    for i in list:
      record.remove(i)

    dict[tuple(list)] = record
  return dict