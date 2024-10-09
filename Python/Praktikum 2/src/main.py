# Import file lain
from src.controllers import topping_controller
from src.models import topping_model
from src import services


# Variable class/object
# Memanggil class dari file yang telah di import sebelumnya 
toppingCtrl = topping_controller.ToppingController()
toppingModel = topping_model.TopingModel
services = services.Services()

# Variable int
# Membuat variable finalPrice untuk menyimpan harga total, dan melakukan operasi jika dibutuhkan
finalPriceInt = 0
 


# data Array/List

# Mengambil data list toping dari controller
toppings = toppingCtrl.getTopings();


# Pemanis :D
print('============== Welcome to our store ==============\n ')
print('Choose your toppings : ')

# Menampilkan semua topping yang tersedia dengan looping
for topping in toppings:
    print(f'{topping[toppingModel.id]}. {topping[toppingModel.name]} - {services.formatToIdr(topping[toppingModel.additionalPrice])}')

# Membuat Boolean untuk mengontrol looping 
loopInputToping = True

# Lopping berdasarkan bool loopInputToping, looping dilakukan agar ketika ada input yg salah program tidak dilanjutkan dan mengulangi flow ini.
while loopInputToping == True:
    # User menginput id dari topping
    selectedTopingId = input('\nmasukkan id/nomor toping yang ingin dipilih : ')
    # Hasil input di pass ke controller dengan method getToppingByid
    topping = toppingCtrl.getToppingById(toppings,selectedTopingId)

    # Validasi jika kembalian dari method tidak null/none maka looping di hentikan dan harga final ditambahkan harga dari topping
    if(topping != None):
        loopInputToping = False
        print('=======================================================')
        print(f'Kamu memilih topping {topping[toppingModel.name]} dengan tambahan harga {services.formatToIdr(topping[toppingModel.additionalPrice])}')
        finalPriceInt += topping[toppingModel.additionalPrice]
    else:
        print('!!! invalid id topping !!!')


#buat variabel sebagai daftar menu 
crust = ['Original crust', 'Stuffed crust ', 'Sausage crust', 'Cheese crust']
print("choose your crust : ")
print("1. Original crust - Rp 25.000")
print("2. Stuffed crust - Rp 30.000")
print("3. Sausage crust - Rp 35.000")
print("4. Cheese crust - Rp 40.000")

# buat print menanyakan ingin memilih crust apa
chooseCrust = int(input("masukkan crust yang kamu inginkan : "))

# buat variabel crust berisi harganya
original_crust = 25000
stuffed_crust = 30000
sausage_crust = 35000
cheese_crust = 40000

#membuat if elif sebagai langkah lanjutkan dari input user
#jika input user = 1
if chooseCrust == 1 :
    finalPriceInt += original_crust
#jika input user = 2    
elif chooseCrust == 2 :
    finalPriceInt += stuffed_crust
#jika input user = 3    
elif chooseCrust == 3 :
    finalPriceInt += sausage_crust
#jika input user = 4    
elif chooseCrust == 4 :
    finalPriceInt += cheese_crust

#pengurangan input user 
crustSelected = None
if(chooseCrust > 0 and chooseCrust < len(crust)):
    crustSelected = crust[chooseCrust-1]



# daftar menu
size = [
    'reguler', 'medium', 'large'
]

print("choose your pizza size: ")
print("1. reguler - Rp 60.000")
print("2. medium - Rp 70.000")
print("3. large - Rp 80.000")

# buat print ingin pizza size apa 
chooseSize = int(input("masukkan size yang kamu inginkan : "))

# buat variabel size
reguler = 60000
medium = 70000
large = 80000


if chooseSize == 1 :
    finalPriceInt += reguler
elif chooseSize == 2 :
    finalPriceInt += medium
elif chooseSize == 3 :
    finalPriceInt += large 

sizeSlected = None
if(chooseSize > 0 and chooseSize < len(size)):
    sizeSlected = chooseSize[chooseSize-1]

extraCheese = input(f'apakah anda mau menambahkan keju ? +{services.formatToIdr(10000)} (ya/no) :') 

if extraCheese == "ya":
    finalPriceInt += 10000



print(f"\n\n======================= Order anda berhasil dibuat =======================\n")
print(f"Topping : {topping[toppingModel.name]}")
if(crustSelected != None):
    print(f"Crust : {crustSelected}")
if(sizeSlected !=None):
    print(f"Size : {sizeSlected}")
print(f"tambahan keju : {extraCheese}")
print(f"total pesanan anda adalah : {services.formatToIdr(finalPriceInt)}\n")
print("========================= Terima kasih sudah membeli =========================")

