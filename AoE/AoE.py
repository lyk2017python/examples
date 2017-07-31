import Birim
import Isci
import Asker
import Bina
import Ambar
import Kisla
import Merkez

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
