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

class Isci(Birim):

  def __init__(self, ismi="Basit İşçi", can=100, x=0, y=0):
    super().__init__(can, x, y)
    self.ismi = ismi

  def calis(self):
    print(self.ismi+" çalışıyor...")

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

class Bina:

  def __init__(self, can=5000, ismi = ""):
    self.can = can
    self.olustuMu = False
    self.ismi = ismi

  def olustur(self):
    self.olustuMu = True

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

merkez = Merkez()
kisla  = Kisla()
ambar  = Ambar()

ambar.yemekTopla()
ambar.olustur()
ambar.yemekTopla()
ambar.yemekTopla()

kisla.askerUret()
kisla.askerUret()
kisla.askerUret()
kisla.askerUret()
kisla.askerUret()
kisla.askerUret()

ilkAsker = kisla.askerler[0]
ilkAsker.solaGit()
ilkAsker.solaGit()
ilkAsker.yukariGit()
ilkAsker.sagaGit()
ilkAsker.asagiGit()

dusmanKislasi = Kisla()
dusmanKislasi.askerUret()

dusmanAsker = dusmanKislasi.askerler[0]
dusmanAsker.ismi = "Düşman Askeri"

ilkAsker.saldir(dusmanAsker)
dusmanAsker.savun()
print("Düşman Askerinin Canı: "+str(dusmanAsker.can))

merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()
merkez.isciUret()

ilkIsci = merkez.isciler[0]
ilkIsci.calis()

for i in range(0,3000):
  dusmanAsker.saldir(merkez)
merkez.isciUret()
