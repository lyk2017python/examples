import Birim

class Isci(Birim):

  def __init__(self, ismi="Basit İşçi", can=100, x=0, y=0):
    super().__init__(can, x, y)
    self.ismi = ismi

  def calis(self):
    print(self.ismi+" çalışıyor...")
