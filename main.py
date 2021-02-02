import base64

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
    return self

text = base64.b64decode(open("input.txt", "r").read())

data = {i:crypto(text) for i in range(128)}

data = {k:v.xor_int(k).mode_convert() for k,v in data.items()}

print('\n'.join([str(i)+": "+elem.content[:10] for i,elem in data.items()]))

while True:
    print(repr(data[int(input("Select value for more data: "))]))
