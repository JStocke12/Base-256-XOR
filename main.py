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

test = crypto(base64.b64decode("FionYiQrMDE2MTY3JCQxYiojNCdiNionKzBiICcrLCViIzFiLy02JzFiISMuLicmYmg3LCEuJyQ2MWhsYhYqJzEnYiMwJ2IvKyUqNi47YjEvIy4ueWItLCdiMScnJjUnKyUqNmItJGI1IzYnMDE2NyQkYiotLiYxYiNiNiMuJ2ItJGI2KicvYi4rKSdiNyw2LWI2NS1iJC0uLi01JyZiIDtiNjUnLDY7bzY1LWIsIzclKjYxbGIPLTE2YjcsIS4nJDYxYi4rLCliNi0lJzYqJzBiNi1iLyMpJ2I1KiM2YiMwJ2IhIy4uJyZiaCA3LikgKzYxaGxiFio3MW5iNionYjUjNicwMTY3JCRiIDcuKSArNmIgJzE2IywmMWItJGI2NS1iNSM2JzAxNjckJGI3LCEuJyQ2MW5iNionYjEtNzAxNjckJGIgNy4pICs2Yi0kYjY1LWIxLTcwMTY3JCRiNywhLickNjFuYiMsJmIxLWItLGxiahEtLydiKSssJjFuYjE3ISpiIzFiMTcsMTY3JCRuYiknJzJiIy4tLCd5Yi02KicwMW5iMTchKmIjMWIrMC0sbmIhLissJWI2LSUnNionMGIrLGIrIScxYjUqJyxiKyxiNionYiQjMTZiMTYjLCYrLCV5YiMsJmI2KicwJ2IjMCdiOyc2Yi8tMCdiOy0pJzUjOzFsa2IVKicsYjcsLispJ2IhLickNjFiLissKWIrLGIjYiA3LikgKzZuYjYqJztiLyMpJ2JoICssJissJTFobGIWKjcxbmI1IzYnMGIrMWIjYiArLCYrLCViLSRiNjUtYjUjNicwMTY3JCRiNywhLickNjFiNSs2KmItLCdiMS03MDE2NyQkYjcsIS4nJDZuYjUqKy4nYiNiIDcuKSArNmItJGItLCdiLSRiNionYiQtMCcxNjckJDFiLyMpKywlYjcyYiQuJzEqYi8jO2IqIzQnYiNiNiotNzEjLCZiNiotNzEjLCZiLTBiLy0wJ2I3LCEuJyQ2MWItJGI2KicxJ2I2NS1iJCswMTYxNjckJDFiNi0lJzYqJzBiNSs2KmIhLSMuMTY3JCRiIywmYiEqLSknMTY3JCRs"))

test.xor_int(66)

test.mode_convert()

open("out.txt", "w").write(test.content)