import Birim

class Asker(Birim):

  def __init__(self, saldiriGucu=7, ismi="Basit Asker", can=100, x=0, y=0):
    super().__init__(can, x, y)
    self.saldiriGucu = saldiriGucu
    self.ismi = ismi

  def saldir(self, hedef):
    if hedef.can > 0:
      hedef.can -= self.saldiriGucu
      print(self.ismi+" "+hedef.ismi+" birimine "+str(self.saldiriGucu)+" hasar verdi.")
      print(hedef.ismi+" kalan canı: "+str(hedef.can))
    else:
      print(hedef.ismi+" biriminin canı olmadığı için saldıramazsınız.")

  def savun(self):
    if self.can > 0:
      self.can += 5
      print(self.ismi+" birimi 5 can arttırdı")
    else:
      print(self.ismi+" birimi ölü")
