import Bina

class Kisla(Bina):
  def __init__(self, can=1500, maksimum=5):
    super().__init__(can, "Kışla")
    self.askerler = []
    self.maksimum = maksimum

  def askerUret(self):
   if self.can > 0:
    if len(self.askerler) < self.maksimum:
      yeniAsker = Asker()
      self.askerler.append(yeniAsker)
      print("Kışladaki asker sayısı: "+str(len(self.askerler)))
    else:
      print("Kışlada yer yok, asker üretilemiyor!")
   else:
    print("Kışla binası yok edildi")
