class Birim:

  def __init__(self, can=100, x=0, y=0):
    self.can = can
    self.x   = x
    self.y   = y

  def hareketEt(self, x, y):
    self.x = x
    self.y = y
    print(str(x)+","+str(y)+" noktasına gidiliyor")

  def solaGit(self):
    self.hareketEt((self.x-1), self.y)

  def sagaGit(self):
    self.hareketEt((self.x+1), self.y)

  def yukariGit(self):
    self.hareketEt(self.x, (self.y+1))

  def asagiGit(self):
    self.hareketEt(self.x, (self.y-1))
