import Bina

class Ambar(Bina):
  def __init__(self, can=700):
    super().__init__(can, "Ambar")
    self.yemek = 0

  def yemekTopla(self):
   if self.can > 0:
    if self.olustuMu:
      self.yemek += 10
      print("Ambar'daki yeni yemek sayısı: "+str(self.yemek))
    else:
      print("Henüz ambar oluşturulmadı, kullanamazsınız.")
   else:
    print("Ambar binası yok edildi")
