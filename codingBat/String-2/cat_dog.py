'''

Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

'''

def cat_dog(str):
  cat = dog = 0
  for words in range(len(str)-1):
    if str[words:(words+3)] == 'cat':
      cat += 1
    elif str[words:(words+3)] == 'dog':
      dog += 1
    else:
      continue
  if cat == dog:
    return True
  else:
    return False
