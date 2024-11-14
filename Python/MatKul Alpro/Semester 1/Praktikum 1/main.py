import math











#Membuat class/object
# class Controller:
#     #constructor mengambil var nama sebagai tambahan
#     def __init__(self, publicName):
#         self.publicName = publicName
#         print(publicName)

# # Method/function mendapatkan hasil dari umur dengan mengambil parameter umur
#     def getAge(self, age):
#     #   Melakukan validasi umur
#       if age < 18: 
#          return self.publicName+' masih remaja'
#       elif age >18 & age <= 60:
#          return self.publicName+' orang dewasa'
#       elif age > 60:
#          return self.publicName+' lansia'
#       else: 
#          return self.publicName+' belum lahir'



# name = input('Masukan nama : ')
# age = input('Masukan umur (hanya angka) : ')

# object = Controller(name)


# print(object.getAge(21))


# next = True


# print('halo \ndek' +str(3))

# while next == True:

#     n = int(input("Masukan jumlah :"))
#     # print(bool(n))


#     #mendapatkan jumlah string
#     # n = len(input())

#     for i   in range(1, n +1, +1):
#         print(  '*' * i  )
        
#     for i   in range(n, 0, -1):
#         print('*' * i )

#     for i   in range(1, n +1, +1):
#         val = n-i
#         print(  ' ' * val + "*" * i )

#     for i   in range(n, 0, -1):
#         val = n-i
#         print(  ' ' * val + "*" * i )

#     print("")


#     for i   in range(1, n +1, +1):
#         val = n-i
#         print(  ' ' * val + "" * i + '' * i )

#     for i   in range(n, 0, -1):
#         val = n-i
#         print(  ' ' * val + "" * i  + '' * i)


#     for i in range(1, n + 1):
#         val = n-i
#         print(' ' * val+ '*' * (2 * i - 1))

#     for i in range(n - 1, 0, -1):
#         val = n-i
#         print(' ' * val + '*' * (2 * i - 1))

#     nextInput = input("Apa anda ingin melanjutkan dengan value lain? \n( isi dengan n jika ingin berhenti) \n")

#     #not itu sama saja dengan !
#     if  nextInput == 'n':
#         next = not next

# print('Program di hentikan')