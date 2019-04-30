import string
import random

def choice(words):
  #assumes words is non-empty
  random.seed
  index = random.randint(0,len(words)-1)
  return words[index]

def do_shaney(text):
  output = ''
  words = text.split()
  end_sentence = []
  dict = {}
  prev1 = ''
  prev2 = ''
  for word in words:
    if prev1 != '' and prev2 != '':
      key = (prev2, prev1)
      if key in dict:
        dict[key].append(word)
      else:
        dict[key] = [word]
        if (prev1[-1:] == '.' or prev1[-1:] == '?' or prev1[-1:] == '!'):
          end_sentence.append(key)
    prev2 = prev1
    prev1 = word
  
  if end_sentence == []:
    print('Sorry, there are no sentences in the text.')
    return
  
  key = ()
  count = 10
  
  while 1:
    if key in dict:
      word = choice(dict[key])
      #print word,
      output += word + ' '
      key = (key[1], word)
      if key in end_sentence:
        #print
        count = count - 1
        key = choice(end_sentence)
        if count <= 0:
          break
    else:
      key = choice(end_sentence)
  return output

print(do_shaney("Astrophysicists have taken an important step toward solving the mystery of how disk galaxies maintain the shape of their spiral arms. Their findings support the theory that these arms are created by a wave of denser matter that creates the spiral pattern as it travels across the galaxy. Nah the density of stars is still pretty low. The brightness makes the arms look stronger than they are, because the compression of gas tends to produce new stars, and the shortest lived stars that dont survive until the arm passes are the brightest."))
