import Bina

class Merkez(Bina):
  def __init__(self, can=10000, maksimum=20):
    super().__init__(can, "Merkez")
    self.isciler = []
    self.maksimum = maksimum

  def isciUret(self, adet=1):
   if self.can > 0:
    bostakiAlan = self.maksimum - len(self.isciler)
    if adet <= bostakiAlan:
      for i in range(0,adet):
        yeniIsci = Isci()
        self.isciler.append(yeniIsci)
      print(str(adet)+" adet işçi üretildi. İşçi Sayısı: "+str(len(self.isciler)))
    else:
      print("İşçi üretebilmek için merkezinizi geliştirmelisiniz!")
   else:
    print("Merkez binası yok edildi")
