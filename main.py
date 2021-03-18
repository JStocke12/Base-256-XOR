import base64
import string
import random

char_weights = {**{' ':1, 'e':2, 't':3, 'a':4, 'i':4,
'n':4, 'o':4, 's':4, 'h':5, 'r':6,
'd': 7, 'l':8, 'u':9, 'c':10, 'm':10,
'f':11, 'w':12, 'y':12, 'g':13, 'p':13,
'b':14, 'v':15, 'k':16, 'q':17, 'j':18,
'x': 18, 'z': 19}, **{i:20 for i in string.digits}, **{i:30 for i in string.punctuation if i != ' '}}

class crypto:
  def __init__(self, s):
    self.content = s

  def __repr__(self):
    return repr(self.content)

  def mode_convert(self):
    try:
      if type(self.content) == str:
        self.content = bytes(self.content, "ascii")
      else:
        self.content = self.content.decode("ascii")
      return self
    except:
        pass

  def xor(self, key):
    if type(self.content) == str:
      self.mode_convert()
      self.xor(key)
      self.mode_convert()
    else:
      try:
          key = bytes(key, "ascii")
          key_repeated = key*(len(self.content)//len(key)) + key[:(len(self.content)%len(key))]
          self.content = bytearray(i^j for i,j in zip(self.content,key_repeated))
          return self
      except:
          pass

  def xor_int(self, key):
    if type(self.content) == str:
      self.mode_convert()
      self.xor_int(key)
      self.mode_convert()
    else:
      self.content = bytearray(i^key for i in self.content)
    return

  def xor_rand(self, seed):
    random.seed(seed)
    if type(self.content) == str:
      self.mode_convert()
      self.xor_rand(seed)
      self.mode_convert()
    else:
      self.content = bytearray(i^random.randrange(256) for i in self.content)

'''strlen = int(input("Text Display Length: "))

text = base64.b64decode(open("input.txt", "r").read())

data = {i:crypto(text) for i in range(128)}

data = {k:v.xor_int(k).mode_convert() for k,v in data.items()}

data = {k:v for k, v in sorted(data.items(), key = lambda elem: sum(map(lambda char: char_weights.get(char, 1000), elem[1].content)))}

print('\n'.join([str(i)+": "+elem.content[:strlen] for i,elem in data.items()]))

while True:
    print(repr(data[int(input("Select value for more data: "))]))'''

test = crypto("Hello World!")
test.mode_convert()
test.xor_rand(5)
test2 = test
print(test2)
test.xor_rand(5)
print(test.mode_convert())
