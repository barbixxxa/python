'''

Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

'''

def count_hi(str):
  x = 0
  for words in range(len(str)-1):
    if str[words:(words+2)] == 'hi':
      x = x + 1
  return x
