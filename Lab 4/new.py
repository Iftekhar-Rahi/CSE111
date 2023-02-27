course=['CSE230: 40', 'CSE220: 4.0', 'MAT110: 4.0']
for i in course:
  key, value = i.split(": ")
  value =float(value)
  print(key)
  print(value)