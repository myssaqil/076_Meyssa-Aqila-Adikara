import math

class KubusController:

   def __init__(self, s):
      self.s =s 
      
    
   
   def luas(self):
    return math.pow(self.s, 2) * 6
   def volume(self):
    return math.pow(self.s, 3)
      


# Membuat boolean untuk mengontrol looping
next = True

# Lopping berdasarkan kondisi bool next
while next == True:

   kubus = KubusController(float(input("masukkan rusuk kubus : ")))

   print('luas : '+str(kubus.luas()))
   print('volume : '+str(kubus.volume()))

# Memberikan input apakah user ingin berhenti? dengan diharapkan value yg diinput adalah string "n"
   nextInput = input("Apa anda ingin mengulangi Program? \n( isi dengan n jika ingin berhenti) \n")

# Melakukan validasi input, jika input == string "n" maka boolean next akan diubah menjadi false
    #not itu sama saja dengan !
   if  nextInput == 'n':
        next = not next

# Dikarenakan bool next tidak memenuhi kriteria untuk looping, maka program akan selesai 
print('Program di hentikan')
