class Pegawai:
  def __init__(self, nama,gaji=0):
    self.nama = nama
    self.gaji = gaji
  def tunjangan(self, persen):
    self.gaji = self.gaji + (self.gaji * persen)
  def kerja(self):
    print(self.nama, "pekerjaannya")
  def __repr__(self):
    return "<pegawai:\n nama= %s, gaji = %s" %(self.nama, self.gaji)
class Koki(Pegawai):
  def __init__(self, nama):
    Pegawai.__init__(self, nama, 100000)
  def kerja(self):
    print(self.nama, "Membuat Makanan")
class pelayan(Pegawai):
  def __init__(self, nama):
    Pegawai.__init__(self, nama, 50000)
  def kerja(self):
    print (self.nama, "Melayani Costumer")
class PizzaRobot(Koki):
  def __inti__(self, nama):
    Koki.__init__(Self, nama)
  def kerja(self):
    print(self.nama, "Membuat Pizza")
 
if __name__ == "__main__":
  agus = PizzaRobot("Agus")
  print(agus)
  agus.kerja()
  agus.tunjangan(0.20)
  print(agus)
  print
  
  for kelas in Pegawai, Koki, pelayan, PizzaRobot:
  objek = kelas(kelas.__name__)
  objek.kerja()
