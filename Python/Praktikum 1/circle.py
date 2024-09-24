import math

class CircleController:
   phi7 = 22/7
   phi = 3.14
   isPhi7 = True

   def __init__(self, r, phiSelected):
      self.r = r 
      
      if phiSelected == 'a' :
       print('Phi : '+str(self.phi7))
       self.isPhi7 = True
      else:
       print('Phi : '+str(self.phi))
       self.isPhi7 = False
    
   
   def luas(self):
    return math.pow(self.r, 2) * self.phi
   def volume(self):
    return 2 * self.phi *self.r
      


# Membuat boolean untuk mengontrol looping
next = True

# Lopping berdasarkan kondisi bool next
while next == True:

    phiSelected = input('pilih phi \n- a.22/7\n- b.3,14\n')
    circle = CircleController(float(input("masukkan jari jari lingkaran : ")), phiSelected)

    print('luas : '+str(circle.luas()))
    print('volume : '+str(circle.volume()))

# Memberikan input apakah user ingin berhenti? dengan diharapkan value yg diinput adalah string "n"
    nextInput = input("Apa anda ingin mengulangi Program? \n( isi dengan n jika ingin berhenti) \n")

# Melakukan validasi input, jika input == string "n" maka boolean next akan diubah menjadi false
    #not itu sama saja dengan !
    if  nextInput == 'n':
        next = not next

# Dikarenakan bool next tidak memenuhi kriteria untuk looping, maka program akan selesai 
print('Program di hentikan')