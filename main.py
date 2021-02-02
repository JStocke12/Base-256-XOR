import base64

class crypto:
  def __init__(self, s):
    self.content = s

  def __repr__(self):
    return repr(self.content)

  def mode_convert(self):
    if type(self.content) == str:
      self.content = bytes(self.content, "ascii")
    else:
      self.content = self.content.decode("ascii")

  def xor(self, key):
    if type(self.content) == str:
      self.mode_convert()
      self.xor(key)
      self.mode_convert()
    else:
      key = bytes(key, "ascii")
      key_repeated = key*(len(self.content)//len(key)) + key[:(len(self.content)%len(key))]
      self.content = bytearray(i^j for i,j in zip(self.content,key_repeated))

  def xor_int(self, key):
    if type(self.content) == str:
      self.mode_convert()
      self.xor_int(key)
      self.mode_convert()
    else:
      self.content = bytearray(i^key for i in self.content)

data = [crypto(base64.b64decode(open("input.txt", "r").read())).xor_int(i) for i in range(256)]

[elem.mode_convert() for elem in data]

print('\n'.join([str(i)+": "+repr(elem)[:10] for elem,i in zip(data, range(len(data)))]))

while True:
    print(repr(data[int(input("Select value for more data: "))]))
