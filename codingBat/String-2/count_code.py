'''

Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2


'''

def count_code(str):
  count = 0
  if len(str) < 4:
      return 0
  else:
    for i in range(len(str)-3):
      word = str[i:(i+4)]
      if word[0] == 'c' and word[1] == 'o' and word[3] == 'e':
        count += 1
      else:
        continue
  return count
