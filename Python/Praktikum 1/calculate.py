# Calculation

# Membuat Class Untuk Controller dan menyimpan segala method / reuseable func controller ini 
class CalculateController:
   #  Membuat constructor untuk menerima global parameter dan setting class ketika di panggil
    def __init__(self, bilangan, secondaryBilangan):
      # hasil Passing dari parameter disimpan didalam variable
      self.bilangan = int(bilangan)
      self.secondaryBilangan = int(secondaryBilangan)
    
   #  Membuat reuseable func/method

   # Method penjumlahan 
    def summation(self):
       return self.bilangan + self.secondaryBilangan
    # Method pengurangan 
    def subtraction(self):
       return self.bilangan - self.secondaryBilangan
    # Method perkalian 
    def multiplication(self):
       return self.bilangan * self.secondaryBilangan
    # Method pemabgian 
    def distribution(self):
       return float(self.bilangan) / float(self.secondaryBilangan)
      

# Membuat boolean untuk mengontrol looping
next = True

# Lopping berdasarkan kondisi bool next
while next == True:

   # Membuat input bilangan yang akan di operasikan
   bilangan = input("masukkan bilangan pertama : ")
   secondaryBilangan = input("masukkan bilangan kedua : ")

# Mendefinisikan Controller/class dan mempasing hasil input ke parameter yg dibutuhkan oleh controller
   calculate = CalculateController(bilangan, secondaryBilangan)

# Melakukan cetak seluruh operasi dan setiap operasi memanggil method masing masing
   print('Hasil Penjumlahan : ' + calculate.summation())
   print('Hasil Pengurangan : ' + calculate.subtraction())
   print('Hasil Perkalian : ' + calculate.multiplication())
   print('Hasil Pembagian : ' + calculate.distribution())

# Memberikan input apakah user ingin berhenti? dengan diharapkan value yg diinput adalah string "n"
   nextInput = input("Apa anda ingin mengulangi Program? \n( isi dengan n jika ingin berhenti) \n")

# Melakukan validasi input, jika input == string "n" maka boolean next akan diubah menjadi false
    #not itu sama saja dengan !
   if  nextInput == 'n':
        next = not next

# Dikarenakan bool next tidak memenuhi kriteria untuk looping, maka program akan selesai 
print('Program di hentikan')
