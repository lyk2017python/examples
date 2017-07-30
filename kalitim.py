class Pokemon:
  def __init__(self, adi, soyadi):
    self.adi = adi
    self.soyadi = soyadi

class Digimon(Pokemon):
  def __init__(self, adi, soyadi, form):
    super().__init__(adi,soyadi)
    self.form = form

  def isimYaz(self):
    print(self.adi)

  def bilgiler(self):
    print("FORM:", self.form)

class Senior(Pokemon):
  def __init__(self, adi, soyadi, saldiriGucu):
    super().__init__(adi, soyadi)
    self.saldiriGucu = saldiriGucu

  def saldir(self):
    print(self.adi+" "+str(self.saldiriGucu)+" ile saldiriyor!")

class Junior(Digimon):
  def __init__(self, adi, soyadi, ozelGuc):
    super().__init__(adi, soyadi, 1)
    self.ozelGuc = ozelGuc

  def bilgiler(self):
    super().bilgiler()
    print("ÖZEL GÜÇ:", self.ozelGuc)

j = Junior("Junior", "Nesnesi", "ozel")
j.bilgiler()

s = Senior("Senior", "Poke", 100)
s.saldir()










